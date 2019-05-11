all:
	@echo "Seting up the system"
	@./scripts/setup.sh
	@echo "Done!"

run:
	@echo "Running up the System"
	@docker-compose up -d flood-server
	@echo "Done!"

run-grafana:
	@echo "Running up Grafana"
	@ID=$(id -u) docker-compose up -d grafana
	@echo "Done!"

run-all:
	@echo "Running up Grafana"
	@ID=$(id -u) docker-compose up -d
	@echo "Done!"

stop:
	@echo "Running down the System"
	@docker-compose down
	@echo "Done!"
