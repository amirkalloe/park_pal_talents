backend_dev:
	$(MAKE) -C backend dev
migration_upgrade_base:
	$(MAKE) -C backend migration_upgrade_base
streamlit_dev:
	$(MAKE) -C backend streamlit_dev