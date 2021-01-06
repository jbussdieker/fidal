test:
	python -m unittest discover

coverage:
	coverage run --source fidal -m unittest discover; coverage report -m
