.PHONY: install

install:
	@echo "Installing for deve environment"
	@.venv/bin/python -m pip install -e '.[dev]'
