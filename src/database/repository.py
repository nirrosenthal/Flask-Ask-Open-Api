from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from src.database.model import QuestionRequestModel
from src.database.repository_interface import QuestionAnswerRepositoryInterface


# implementation using Postgres
postgres_engine = create_engine(os.getenv("DATABASE_URL"))   
postgres_session_maker = sessionmaker(bind=postgres_engine)

class QuestionAnswerPostgresRepository(QuestionAnswerRepositoryInterface):

    def add_question_request(self, question, answer):
        record = QuestionRequestModel(question=question, answer=answer)
        with postgres_session_maker() as session:
            session.add(record)
            session.commit() 

    def get_question_request_history(self, **filters):
        with postgres_session_maker() as session:
            return session.query(QuestionRequestModel).all()