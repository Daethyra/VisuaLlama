# Merged Database Operations and Optimization Module

import asyncio
import sqlite3
import logging
from threading import RLock
from typing import Any, List, Tuple, Union
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(filename='database_operations.log', level=logging.INFO)

class DatabaseAgent:
    """
    DatabaseAgent is a class responsible for handling database operations and optimizations.
    It includes caching, CRUD operations, and asynchronous query execution.
    """
    def __init__(self, db_name: str, pool_size: int = 5, query_timeout: int = 5):
        """
        Initializes a new DatabaseAgent instance.
        
        :param db_name: The name of the SQLite database.
        :param pool_size: The size of the connection pool.
        :param query_timeout: The timeout for database queries.
        """
        self.db_name = db_name
        self.pool_size = int(os.getenv('CONNECTION_POOL', pool_size))  # Dynamic Connection Pooling from .env
        self.query_timeout = query_timeout
        self.conn_pool = asyncio.Queue()
        self.lock = RLock()
        self.cache_size = int(os.getenv('CACHE_SIZE', 10))  # Caching from .env
        self.cache = {}
        self.init_conn_pool()

    def init_conn_pool(self):
        """
        Initializes the connection pool with SQLite database connections.
        """
        for _ in range(self.pool_size):
            conn = self._create_connection()
            self.conn_pool.put_nowait(conn)
            
    def _create_connection(self) -> sqlite3.Connection:
        """
        Creates and returns a new SQLite database connection.
        
        :return: sqlite3.Connection
        """
        conn = sqlite3.connect(self.db_name, timeout=self.query_timeout)
        return conn

    # Caching Mechanism
    def cache_query(self, query, result):
        """
        Caches the result of a SQL query.
        
        :param query: The SQL query string.
        :param result: The result of the SQL query.
        """
        if len(self.cache) >= self.cache_size:
            self.cache.pop(next(iter(self.cache.keys())))
        self.cache[query] = result

    def get_cached_result(self, query):
        """
        Retrieves the cached result for a given SQL query.
        
        :param query: The SQL query string.
        :return: Cached result or None if not found.
        """
        return self.cache.get(query, None)

    async def __aenter__(self) -> 'DatabaseAgent':
        """
        Asynchronous context manager entry. Acquires a database connection.
        
        :return: self
        """
        self.conn = await self._acquire_connection()
        logging.info(f"Connected to database {self.db_name}")
        return self

    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """
        Asynchronous context manager exit. Releases the database connection back to the pool.
        
        :param exc_type: Exception type.
        :param exc_value: Exception value.
        :param traceback: Traceback object.
        """
        await self._release_connection(self.conn)
        logging.info("Connection released back to pool.")

    async def _acquire_connection(self) -> sqlite3.Connection:
        """
        Acquires a database connection from the connection pool.
        
        :return: sqlite3.Connection object.
        """
        with self.lock:
            conn = await self.conn_pool.get()
            return conn

    async def _release_connection(self, conn: sqlite3.Connection) -> None:
        """
        Releases a database connection back to the connection pool.
        
        :param conn: The sqlite3.Connection object to be released.
        """
        with self.lock:
            await self.conn_pool.put(conn)

    async def begin(self) -> None:
        """
        Begins a database transaction.
        """
        await asyncio.to_thread(self.execute_query, "BEGIN TRANSACTION;")

    async def commit(self) -> None:
        """
        Commits the current database transaction.
        """
        await asyncio.to_thread(self.conn.commit)

    async def rollback(self) -> None:
        """
        Rolls back the current database transaction.
        """
        await asyncio.to_thread(self.conn.rollback)

    async def execute_query(self, query: str, parameters: Union[Tuple[Any], List[Any]] = None) -> None:
        """
        Executes a write query on the database.
        
        :param query: The SQL query string.
        :param parameters: Optional parameters to be used in the SQL query.
        """
        try:
            await asyncio.to_thread(self.conn.execute, query, parameters)
            await asyncio.to_thread(self.conn.commit)
            logging.info(f"Executed query: {query}")
        except sqlite3.Error as e:
            await asyncio.to_thread(self.conn.rollback)
            logging.error(f"Failed to execute query {query}: {e}")
            raise

    async def execute_read_query(self, query: str, parameters: Union[Tuple[Any], List[Any]] = None) -> List[Tuple[Any]]:
        """
        Executes a read query on the database and caches the result.
        
        :param query: The SQL query string.
        :param parameters: Optional parameters to be used in the SQL query.
        :return: List of tuples containing query results.
        """
        try:
            cursor = await asyncio.to_thread(self.conn.execute, query, parameters)
            result = await asyncio.to_thread(cursor.fetchall)
            self.cache_query(query, result)  # Caching the result
            return result
        except sqlite3.Error as e:
            logging.error(f"Failed to read data: {e}")
            raise

    async def execute_multiple_queries(self, queries: str) -> None:
        """
        Executes multiple SQL queries in a single transaction.
        
        :param queries: String containing multiple SQL queries separated by semicolons.
        """
        try:
            await asyncio.to_thread(self.conn.executescript, queries)
            await asyncio.to_thread(self.conn.commit)
            logging.info(f"Executed multiple queries.")
        except sqlite3.Error as e:
            await asyncio.to_thread(self.conn.rollback)
            logging.error(f"Failed to execute multiple queries: {e}")
            raise

    async def execute_prepared_statement(self, query: str, parameters: Union[Tuple[Any], List[Any]]) -> None:
        """
        Executes a prepared SQL statement.
        
        :param query: The SQL query string.
        :param parameters: Parameters to be used in the SQL query.
        """
        try:
            await asyncio.to_thread(self.conn.execute, query, parameters)
            await asyncio.to_thread(self.conn.commit)
            logging.info(f"Executed prepared statement: {query}")
        except sqlite3.Error as e:
            await asyncio.to_thread(self.conn.rollback)
            logging.error(f"Failed to execute prepared statement {query}: {e}")
            raise

    async def execute_batch_operations(self, query: str, parameters_list: List[Union[Tuple[Any], List[Any]]]) -> None:
        """
        Executes batch operations on the database.
        
        :param query: The SQL query string template.
        :param parameters_list: List of parameter tuples or lists to be used in the SQL query.
        """
        try:
            cursor = await asyncio.to_thread(self.conn.cursor)
            await asyncio.to_thread(cursor.executemany, query, parameters_list)
            await asyncio.to_thread(self.conn.commit)
            logging.info(f"Executed batch operations.")
        except sqlite3.Error as e:
            await asyncio.to_thread(self.conn.rollback)
            logging.error(f"Failed to execute batch operations: {e}")
            raise

    async def validate_data(self, query: str, parameters: Union[Tuple[Any], List[Any]] = None) -> bool:
        """
        Placeholder for data validation logic.
        
        :param query: The SQL query string.
        :param parameters: Optional parameters to be used in the SQL query.
        :return: True if data is valid, False otherwise.
        """
        # Placeholder for data validation logic
        return True

    async def handle_schema(self, schema_sql: str) -> None:
        await self.execute_multiple_queries(schema_sql)
        
    # For CRUD Operations
    async def create(self, table_name, columns):
        """
        Creates a new table in the database.
        
        :param table_name: The name of the table to create.
        :param columns: The columns and their data types.
        """
        query = f"CREATE TABLE {table_name} ({columns});"
        await self.execute_query(query)

    async def read(self, table_name, conditions=None):
        """
        Reads data from a table.
        
        :param table_name: The name of the table to read from.
        :param conditions: Optional SQL WHERE conditions.
        :return: List of tuples containing query results.
        """
        query = f"SELECT * FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        return await self.execute_read_query(query)

    async def update(self, table_name, updates, conditions):
        """
        Updates records in a table.
        
        :param table_name: The name of the table to update.
        :param updates: The columns and their new values.
        :param conditions: SQL WHERE conditions for the update.
        """
        query = f"UPDATE {table_name} SET {updates} WHERE {conditions}"
        await self.execute_query(query)

    async def delete(self, table_name, conditions):
        """
        Deletes records from a table.
        
        :param table_name: The name of the table to delete from.
        :param conditions: SQL WHERE conditions for the deletion.
        """
        query = f"DELETE FROM {table_name} WHERE {conditions}"
        await self.execute_query(query)

    # For Database Initialization
    async def initialize_database(self, schema_sql):
        """
        Initializes the database with a given schema.
        
        :param schema_sql: The SQL script for database schema.
        """
        await self.execute_multiple_queries(schema_sql)