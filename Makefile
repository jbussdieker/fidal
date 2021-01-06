test:
	python3 -m unittest discover

coverage:
	coverage run --source fidal -m unittest discover; coverage report -m
