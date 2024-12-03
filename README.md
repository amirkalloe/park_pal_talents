# Park Pal Talents

This repository contains the code for the Park Pal Talents project.

## Prerequisites

- Python 3.12
- Poetry
- SQLite
- Docker
- Linux

## Installation
0. First cd backend
``cd backend``
### Set up dev envirnment
1. First install python 3.12:
``sudo apt-get install python3.12``
2. Then install poetry:
``sudo apt install python3-poetry``
3. Make sure to use pyhon 3.12:
``poetry env use 3.12``
4. Then install the dependencies using poetry:
``poetry install``
5. Set up the database and run the migrations:
``sudo apt install sqlite``
``make migration_upgrade_base``
6. Set up fastapi serer:
``make api``
7. Set up frontend streamlit:
``make streamlit``

### Run docker containers
1. Build containers for both frontend and backend:
``make docker_compose_up"``
2. Stop the containers:
``make docker_compose_down``
