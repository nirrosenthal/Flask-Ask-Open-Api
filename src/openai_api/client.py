from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:

    def __init__(self):
        self._client = OpenAI()

    