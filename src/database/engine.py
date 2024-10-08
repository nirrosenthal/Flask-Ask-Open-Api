from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from src.database.model import QuestionRequestModel

connection_url = os.getenv("DATABASE_URL")

class DatabaseEngineSingleton:
    __instance = None

    def __new__(cls):
        if DatabaseEngineSingleton.__instance is None:
            cls.__instance = \
                super(DatabaseEngineSingleton,cls).__new__(cls)
            cls.__instance._connection_url = connection_url
            cls.__instance._engine = create_engine(connection_url)   
            cls.__instance._session_maker = sessionmaker(bind=cls.__instance._engine)
        return cls.__instance
    
    @property
    def engine(cls):
        return cls.__instance._engine

    @property
    def connection_url(cls)->str:
        return cls.__instance._connection_url
  
    
    def add_question_request(cls,question:str, answer:str):
        record = QuestionRequestModel(question=question, answer=answer)
        
        with cls.__instance._session_maker() as session:
            session.add(record)
            session.commit()
        with cls.__instance._session_maker() as session:
            records =session.query(QuestionRequestModel).all()


    
if __name__ == "__main__":
    db = DatabaseEngineSingleton()
    print(connection_url)

    db.add_question_request("test: what is my name?", "test: nir the great")
        