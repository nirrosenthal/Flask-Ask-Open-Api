
from flask import Flask, request, jsonify
from src.openai_api.openai_ask_question import OpenAIAskQuestion
from src.database.engine import DatabaseEngine
import os

app = Flask(__name__)

PORT = os.environ.get("FLASK_PORT")

@app.route("/ask", methods=["POST"])
def ask():
    print("Ask post request received")
    open_ai = OpenAIAskQuestion(request.get_json().get("question"))
    open_ai.ask()
    print("Open API request successful") #log
    DatabaseEngine().add_question_request(open_ai.question, open_ai.answer)
    print("Database addition successful") #log
    response = {
        "question": open_ai.question,
        "answer": open_ai.answer
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=PORT)