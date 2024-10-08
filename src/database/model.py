from datetime import datetime
from sqlalchemy import Integer, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base


QuestionRequestBase = declarative_base()

class QuestionRequestModel(QuestionRequestBase):
    __tablename__ = 'question_request'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #index=true?
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
 
    def __repr__(self) -> str:
        return f"""QuestionRequestModel(
        created_at:{self.created_at}\n
        question:{self.question}\n
        answer:{self.answer}\n
        )"""
