from src.openai_api.client import OpenAIClient

class OpenAIAskQuestion(OpenAIClient):

    def __init__(self, question: str):
        super().__init__()
        self._question = question

    @property
    def question(self)->str:
        return self._question

    @property
    def answer(self)->str:
        return self._answer
    
    def ask(self)->str:
        # add an empty question clause
        if self._question=="":
            return ""
        
        self._openai_response = self._client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"system", "content": "You are an assistant who answers questions"},
            {"role": "user", "content": self._question}
        ]
        )
        self._answer = self._openai_response.choices[0].message.content
        return self._answer
    
