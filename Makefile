help:
	@echo '                                                                                             '
	@echo 'Makefile for the External Grader                                                             '
	@echo '                                                                                             '
	@echo 'Usage:                                                                                       '
	@echo '    make requirements              install requirements                                      '
	@echo '    make requirements-test         install test requirements                                 '
	@echo '    make test                      run tests                                                 '
	@echo '    make test-cov                  run tests with coverage                                   '
	@echo '    make compose                   build and launch containers                               '
	@echo '    make update                    reset changes and pull the newest version from git        '
	@echo '                                                                                             '

requirements:
	pip install -qr requirements/requirements.txt

requirements-test: requirements
	pip install -qr requirements/requirements-test.txt

test:
	pytest -vvv

test-cov:
	pytest --cov-report term-missing --cov=./ -vvv

compose:
	docker-compose -f docker-compose.reqs.yml build
	docker-compose build
	docker-compose up -d

update:
	git reset --hard
	git pull https://github.com/Ragnaruk/external_grader.git

.PHONY: requirements requirements-test test test-cov compose update