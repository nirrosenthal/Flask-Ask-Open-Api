from abc import ABC, abstractmethod

# interface for repository of any database
class QuestionAnswerRepositoryInterface(ABC):
    @abstractmethod
    def add_question_request(self, question, answer):
        pass

    def get_question_request_history(self):
        pass