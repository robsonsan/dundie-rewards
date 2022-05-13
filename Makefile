.PHONY: install virtualenv ipython test

install:
	@echo "Installing for deve environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython


test:
	@pytest -vv -s tests/

