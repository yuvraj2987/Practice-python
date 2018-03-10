.PHONY: test

test:
	bash cli/test.sh

setup27:
	bash cli/setup27.sh

setup35:
	bash cli/setup35.sh

clean:
	rm */*.pyc
