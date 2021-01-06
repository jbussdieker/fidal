test:
	python3 -m unittest discover

coverage:
	coverage run --source fin -m unittest discover; coverage report -m
