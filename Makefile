.PHONY: develop-install develop-uninstall test pep8

test: pep8
	green -vv --run-coverage

develop-install:
	python setup.py develop

develop-uninstall:
	python setup.py develop --uninstall

pep8:
	flake8
