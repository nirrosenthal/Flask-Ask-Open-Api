import pytest
from flask import json
from src.flask.app import app
import src.flask.app
from mockito import when, verify, mock


@pytest.fixture
def flaskClient():
    app.testing = True
    with app.test_client() as flaskClient:
        yield flaskClient

@pytest.fixture
def openAIAskQuestion(request):
    question, answer = request.param    
    mock_openAI = mock({"question": question, "answer": answer})
    when(src.flask.app).OpenAIAskQuestion(question).thenReturn(mock_openAI)
    return mock_openAI


@pytest.mark.parametrize('openAIAskQuestion', [("what do i get from this post request?","the question and answer to it")], indirect=True)
def test_ask__sanity_respose__expected_answer_question_response_code_200(flaskClient, openAIAskQuestion):
    response = flaskClient.post('/ask', json={"question": openAIAskQuestion.question})
    assert response.status_code == 200
    json_data = response.get_json()
    when(openAIAskQuestion).ask().thenReturn(openAIAskQuestion.answer)
    assert json_data["question"] == openAIAskQuestion.question
    assert json_data["answer"] == openAIAskQuestion.answer
    verify(openAIAskQuestion).ask()
