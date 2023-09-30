# database_agent.py
from session_manager import Session, init_db
from models import Conversation, ObjectDetection
from crud_enum import CRUD

class DatabaseAgent:

    def __init__(self):
        self.session = Session()
        
    def db_handler(self, operation, model, **kwargs):
        try:
            if operation not in CRUD.__members__:
                raise ValueError(f"Invalid operation: {operation}. Must be one of {list(CRUD.__members__.keys())}.")
            operation_type = CRUD(operation).value

            if operation_type == CRUD.CREATE.value:
                new_entry = model(**kwargs)
                self.session.add(new_entry)
                self.session.commit()
                
            elif operation_type == CRUD.READ.value:
                query_result = self.session.query(model).filter_by(**kwargs).all()
                return query_result

            elif operation_type == CRUD.UPDATE.value:
                entries = self.session.query(model).filter_by(**kwargs.get('filter_by')).all()
                for entry in entries:
                    for key, value in kwargs.get('update_values').items():
                        setattr(entry, key, value)
                self.session.commit()

            elif operation_type == CRUD.DELETE.value:
                entries = self.session.query(model).filter_by(**kwargs).all()
                for entry in entries:
                    self.session.delete(entry)
                self.session.commit()

            return "Operation completed successfully."
        
        except Exception as e:
            return f"An error occurred: {e}"
