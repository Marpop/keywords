
# keywords

## Development

Required:

- python >= 3.7
- pipenv

Use `pipenv` to make virtualenv and install all dependencies:

    pipenv install --dev

Type `make` to see available commands from `Makefile`. All are executed inside created virtual environment.

Running dev server (you need to create `.env` file based on `.env.example`):

    make run
