api:
	poetry run uvicorn app.main:app --host 0.0.0.0 --reload --port 8000
.PHONY: streamlit
streamlit:
	streamlit run streamlit/Homepage.py
migration_upgrade_base:
	poetry run alembic -c alembic/alembic.ini upgrade head
docker_compose_up:
	sudo docker-compose up -d
docker_compose_down:
	sudo docker-compose down