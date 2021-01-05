test:
	python3 -m unittest discover

coverage:
	coverage run --source iex -m unittest discover; coverage report -m
