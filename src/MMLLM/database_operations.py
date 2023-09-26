# Proceeding with implementing additional improvements to the DatabaseAgent class

import sqlite3
import logging
from threading import RLock
from typing import Any, List, Tuple, Union

logging.basicConfig(filename='database_operations.log', level=logging.INFO)

class DatabaseAgent:
    def __init__(self, db_name: str, pool_size: int = 5, query_timeout: int = 5):
        self.db_name = db_name
        self.pool_size = pool_size
        self.query_timeout = query_timeout
        self.conn_pool = [self._create_connection() for _ in range(self.pool_size)]
        self.lock = RLock()

    def _create_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_name, timeout=self.query_timeout)
        return conn

    def __enter__(self) -> 'DatabaseAgent':
        self.conn = self._acquire_connection()
        logging.info(f"Connected to database {self.db_name}")
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self._release_connection(self.conn)
        logging.info("Connection released back to pool.")

    def __getitem__(self, query: str) -> List[Tuple[Any]]:
        return self.execute_read_query(query)

    def __setitem__(self, query: str, parameters: Union[Tuple[Any], List[Any]]) -> None:
        self.execute_query(query, parameters)

    def __delitem__(self, query: str) -> None:
        self.execute_query(query)

    def __contains__(self, query: str) -> bool:
        result = self.execute_read_query(query)
        return bool(result)

    def _acquire_connection(self) -> sqlite3.Connection:
        with self.lock:
            return self.conn_pool.pop()

    def _release_connection(self, conn: sqlite3.Connection) -> None:
        with self.lock:
            self.conn_pool.append(conn)

    def begin(self) -> None:
        self.execute_query("BEGIN TRANSACTION;")

    def commit(self) -> None:
        self.conn.commit()

    def rollback(self) -> None:
        self.conn.rollback()

    def execute_query(self, query: str, parameters: Union[Tuple[Any], List[Any]] = None) -> None:
        try:
            cursor = self.conn.cursor()
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            self.conn.commit()
            logging.info(f"Executed query: {query}")
        except sqlite3.Error as e:
            self.conn.rollback()
            logging.error(f"Failed to execute query {query}: {e}")
            raise

    def execute_read_query(self, query: str, parameters: Union[Tuple[Any], List[Any]] = None) -> List[Tuple[Any]]:
        try:
            cursor = self.conn.cursor()
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Failed to read data: {e}")
            raise

    def execute_multiple_queries(self, queries: str) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.executescript(queries)
            self.conn.commit()
            logging.info(f"Executed multiple queries.")
        except sqlite3.Error as e:
            self.conn.rollback()
            logging.error(f"Failed to execute multiple queries: {e}")
            raise

    def execute_prepared_statement(self, query: str, parameters: Union[Tuple[Any], List[Any]]) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, parameters)
            self.conn.commit()
            logging.info(f"Executed prepared statement: {query}")
        except sqlite3.Error as e:
            self.conn.rollback()
            logging.error(f"Failed to execute prepared statement {query}: {e}")
            raise

    def execute_batch_operations(self, query: str, parameters_list: List[Union[Tuple[Any], List[Any]]]) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.executemany(query, parameters_list)
            self.conn.commit()
            logging.info(f"Executed batch operations.")
        except sqlite3.Error as e:
            self.conn.rollback()
            logging.error(f"Failed to execute batch operations: {e}")
            raise

