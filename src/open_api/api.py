from openai import OpenAI
import os
import requests
import json

OPENAI_API_KEY = "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"

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

client = OpenAI()

question = "why is the sky blue?"
openai_response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role":"system", "content": "You are an assistant who answers questions"},
        {"role": "user", "content": question}
    ]
)
print(openai_response.choices[0].message.content)