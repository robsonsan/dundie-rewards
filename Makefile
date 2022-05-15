.PHONY: install virtualenv ipython test pflake8

install:
	@echo "Installing for dev environment"
	@../.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@../.venv/bin/python -m pip -m venv .venv


fmt:
	@../.venv/bin/black dundie tests integration


lint:
	@../.venv/bin/pflake8 

ipython:
	@../.venv/bin/ipython


test:
	@pytest -vv -s tests/

