backend_dev:
	$(MAKE) -C backend dev
migration_upgrade_base:
	$(MAKE) -C backend migration_upgrade_base
streamlit_dev:
	$(MAKE) -C backend streamlit_dev
docker_api:
	sudo docker build -t park-pal-talents/api . -f "backend/api.Dockerfile" && sudo docker run -p 8000:8000 park-pal-talents/api
docker_frontend:
	sudo docker build -t park-pal-talents/frontend . -f "backend/frontend.Dockerfile" && sudo docker run -p 8501:8501 park-pal-talents/frontend