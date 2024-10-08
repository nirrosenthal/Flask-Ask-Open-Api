from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from src.database.model import QuestionRequestModel

class DatabaseEngine:
    __instance = None

    def __new__(cls):
        if DatabaseEngine.__instance is None:
            cls.__instance = \
                super(DatabaseEngine,cls).__new__(cls)
            cls.__instance._engine = create_engine(os.getenv("DATABASE_URL"))   
            cls.__instance._session_maker = sessionmaker(bind=cls.__instance._engine)
        return cls.__instance
    
    
    def add_question_request(cls,question:str, answer:str):
        record = QuestionRequestModel(question=question, answer=answer)
        
        with cls.__instance._session_maker() as session:
            session.add(record)
            session.commit()
        with cls.__instance._session_maker() as session:
            records =session.query(QuestionRequestModel).all()


    
if __name__ == "__main__":
    db = DatabaseEngine()
    print(os.getenv("DATABASE_URL"))
    db.add_question_request("test: what is my name?", "test: nir the great")
        