# Flask-Ask-Open-Api
Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database.

## Key Features
- Written in Python
- Flexible Setup
- Post request service
- Docker
## Installation
- Install [Docker](https://docs.docker.com/engine/install/))
- clone the project
## Configurations
- How to change the Flask server port?
- How to change the Posgres database port?
- How to change Postgres User/Password/database name?
## Running
- Open powershell/cmd in main Project directory
- Run docker container:
  docker-compose -f docker\docker-compose.yml down
- Closing Flask server and database
