init:
	pip install -r requirements.txt

test:
	nosetests tests

clean:
	find . -name '*.pyc' -exec rm {} +
	find . -name '*.pyo' -exec rm {} +
	find . -name '*~' -exec rm  {} +
	rm -r *.egg-info
