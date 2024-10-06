import pytest
from flask import json
from src.flask.app import app
from mockito import when, verify

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_ask__sanity_respose__expected_answer_question_response_code_200(client):
    question = "what do i get from this post request?"
    data = {"question": question}
    response = client.post('/ask', json=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["question"] == question
    # need to mock openAI to get answer from openAI
    assert json_data["answer"] == "the question and answer to it"
