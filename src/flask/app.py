from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    ask_data = request.get_json()
    question = ask_data.get("question")
    answer = "defualt answer until openAI feature"
    response = {
        "question": question,
        "answer": answer
    }
    print(response)
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)