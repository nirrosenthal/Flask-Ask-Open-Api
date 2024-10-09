import src.openai_api.openai_ask_question
from mockito import when, verify, mock
import pytest
import src.openai_api.client


@pytest.fixture
def completions_mock(request):
    question, answer = request.param
    openAI_response_mock = mock({'choices':[mock({'message':mock({'content': answer})})]})
    model = "gpt-4o-mini"
    messages = [
            {"role":"system", "content": "You are an assistant who answers questions"},
            {"role": "user", "content": question}
    ]
    completions_mock = mock()
    when(completions_mock).create(model=model,messages=messages).thenReturn(openAI_response_mock)
    return completions_mock


@pytest.mark.parametrize('completions_mock', [("what do i get from this post request?","the question and answer to it")], indirect=True)
def test_ask__sanity__expected_question_answer_property(completions_mock):
    question, answer = ("what do i get from this post request?","the question and answer to it")
    openAI_mock = mock({'chat':mock({'completions': completions_mock})})
    when(src.openai_api.client).OpenAI().thenReturn(openAI_mock)
    openAIAskQuestion = src.openai_api.openai_ask_question.OpenAIAskQuestion(question)
    openAIAskQuestion.ask()
    assert(openAIAskQuestion.answer==answer)




