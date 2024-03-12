dev:
	poetry run uvicorn app.main:app --host 0.0.0.0 --reload --port 8000
migration_upgrade_base:
	poetry run alembic -c alembic/alembic.ini upgrade head
streamlit_dev:
	poetry run streamlit run Homepage.py