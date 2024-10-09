# Flask-Ask-Open-Api
Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database.

## Table Of Contents
- [Key Features](#key-features)
- [Installation](#installation)
- [Configurations](#configurations)
- [Running](#running)
- [Request Format](#request-format)

## Key Features
- Written in Python
- Flexible Configurations
- Postgres database to save request history
- Post request service
- Alembic for database migrations
- OpenAI API usage
- Docker
## Installation
1. Install [Docker](https://docs.docker.com/engine/install/)
2. Clone the project
3. Create a new [OpenAI Secret Key](https://platform.openai.com/api-keys) (or use your own)
4. Configure your project with the new OpenAI Secret Key (See [Configurations](#configurations))
## Configurations
### Change Project Startup settings
1. Go to the directory /docker
2. Open the .env File
.env Example:
```plaintext
OPENAI_API_KEY=open_api_secret_key_example
FLASK_APP=flask_app/app.py
POSTGRES_USER=flask_app
POSTGRES_PASSWORD=flask_app_insert
POSTGRES_HOST=database
POSTGRES_DB=question_answer_db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
FLASK_PORT=5000
```
Editing the .env file to change the following settings:
- OpenAI API credentials:
    - OpenAI API Secret Key: 
```plaintext
OPENAI_API_KEY={NEW OPENAPI SECRET KEY}
```
- Ports:
    - Flask Server Port
    ```plaintext
    FLASK_PORT={NEW PORT}
    ```
    - Postgres Database Port
    ```plaintext
    POSTGRES_PORT={NEW PORT}
    ```
- Database Settings:
    - Postgres user
    ```plaintext
    POSTGRES_PORT={NEW PORT}
    ```
    - Postgres password
    ```plaintext
    POSTGRES_PORT={NEW PORT}
    ```
    - Postgres Database name
    ```plaintext
    POSTGRES_PORT={NEW PORT}
    ```
## Running
1. Launch your command-line interface (e.g., CMD or Terminal) in the main project directory
2. Run docker container
```bash
docker-compose -f docker\docker-compose.yml up -d
```
3. Flask server is up and can send post requests (see [Request Format](#request-format))
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
