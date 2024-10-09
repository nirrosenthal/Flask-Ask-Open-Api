# Flask-Ask-Open-Api
Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database.

## Key Features
- Written in Python
- Flexible Configurations
- Postgres database to save request history
- Post request service
- Alembic for database migrations
- OpenAI API usage
- Docker
## Installation
- Install [Docker](https://docs.docker.com/engine/install/)
- Clone the project
## Configurations
- How to change the Flask server port?
- How to change the Posgres database port?
- How to change Postgres User/Password/database name?
## Running
1. Launch your command-line interface (e.g., CMD or Terminal) in the main project directory
2. Run docker container
```bash
docker-compose -f docker\docker-compose.yml up -d
```
3. Flask server is up and can send post requests (see Request format)
4. Close docker container
```bash
docker-compose -f docker\docker-compose.yml down
```
## Request Format

### Description
This endpoint allows you to submit a question and receive a response with an answer

### Endpoint
**URL:** `http://127.0.0.1:${FLASK_PORT}/ask`  

### Request Method
**POST**

### Request Headers
- **Content-Type:** `application/json`

### Request Body
The request body should be in JSON format and contain the following parameter:

| Parameter | Type   | Description                          |
|-----------|--------|--------------------------------------|
| question  | string | The question you want to ask.       |

Example Body:
```json
{
    "question": "tell me one thing you like about yourself"
}
```
### Response JSON Output
| Key | Type   | Description                          |
|-----------|--------|--------------------------------------|
| question  | string | The question that was asked.       |
| answer  | string | Answer Recieved from OpenAI api       |

Example Response Output:
```json
{
    "question": "tell me one thing you like about yourself",
    "answer": "I appreciate my ability to run post requests."
}
```
