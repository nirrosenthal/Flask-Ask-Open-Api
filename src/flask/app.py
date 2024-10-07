
from flask import Flask, request, jsonify
from src.openai_api.openai_ask_question import OpenAIAskQuestion

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    open_ai = OpenAIAskQuestion(request.get_json().get("question"))
    open_ai.ask()
    response = {
        "question": open_ai.question,
        "answer": open_ai.answer
    }
    print(response)
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)