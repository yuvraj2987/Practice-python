.PHONY: test

test: clean
	bash cli/test.sh

setup27:
	bash cli/setup27.sh

setup35:
	bash cli/setup35.sh

clean:
	find . -name "*.pyc" -delete & \
	    find . -name "__pycache__" -delete
