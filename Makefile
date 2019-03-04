# For more information on the following see http://clarkgrubb.com/makefile-style-guide
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:

RUN_PIPENV = pipenv run

# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)
TARGET_MAX_CHAR_NUM := 23

.PHONY: help
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-$(TARGET_MAX_CHAR_NUM)s$(RESET)$(GREEN)%s$(RESET)\n", $$1, $$2}'
	@echo ''

.PHONY: clean
clean: remove_py_cache remove_coverage_data ## Remove build files, python cache files and test coverage data

.PHONY: test
test: ## Run pytest
	$(RUN_PIPENV) pytest -s

.PHONY: coverage
coverage: ## Generate and open html coverage report
	(RUN_PIPENV) coverage html && open htmlcov/index.html

.PHONY: format_imports
format_imports: ## Format Python imports with isort
	$(RUN_PIPENV) isort --recursive .

.PHONY: format_py
format_py: ## Format Python code format with black
	$(RUN_PIPENV) black .

.PHONY: format
format: format_imports format_py ## Format Python imports and code

.PHONY: lint
lint: ## Lint Python code with flake8
	$(RUN_PIPENV) flake8

.PHONY: remove_coverage_data
remove_coverage_data: ## Remove test coverage data
	rm -f .coverage
	rm -rf htmlcov

.PHONY: remove_py_cache
remove_py_cache: ## Remove cached Python bytecode
	find . -name "*.pyc" | xargs rm -rf
	find . -name "*.pyo" | xargs rm -rf
	find . -name "__pycache__" -type d | xargs rm -rf

.PHONY: run
run: ## Run dev server
	$(RUN_PIPENV) flask run
