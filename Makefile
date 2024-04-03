backend_api:
	$(MAKE) -C backend api
frontend_streamlit:
	$(MAKE) -C backend streamlit
migration_upgrade_base:
	$(MAKE) -C backend migration_upgrade_base

docker_compose_up:
	cd backend && sudo docker-compose up -d
docker_compose_down:
	cd backend && sudo docker-compose down