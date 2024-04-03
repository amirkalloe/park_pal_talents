backend_dev:
	$(MAKE) -C backend dev
migration_upgrade_base:
	$(MAKE) -C backend migration_upgrade_base
streamlit_dev:
	$(MAKE) -C backend streamlit_dev
docker:
	sudo docker build -t amirkalloe/container . -f "backend/Dockerfile" && sudo docker run -p 8000:8000 amirkalloe/container