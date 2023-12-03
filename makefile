shell:
	pipenv shell

test:
	python3 -m unittest discover -s ./practice/python/001_unit_test
	python3 -m unittest discover -s ./practice/python/002_hello_world
	python3 -m unittest discover -s ./advent-of-code/d01.1-trebuchet