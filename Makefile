all:
	@echo "Seting up the system"
	@./scripts/setup.sh
	@echo "Done!"

run:
	@echo "Kickin off the System"
	@./scripts/run.sh
	@echo "Done!"
