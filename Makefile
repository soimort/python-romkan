SETUP = python3 setup.py
SETUP2 = python2 setup.py

.PHONY: default clean build sdist bdist bdist_egg install release

default: build sdist bdist bdist_egg

test:
	$(SETUP) test

clean:
	zenity --question
	rm -fr build/ dist/ src/*.egg-info/
	find . | grep __pycache__ | xargs rm -fr
	find . | grep .pyc | xargs rm -fr

build:
	$(SETUP) build

sdist:
	$(SETUP) sdist
	$(SETUP2) sdist

bdist:
	$(SETUP) bdist

bdist_egg:
	$(SETUP) bdist_egg
	$(SETUP2) bdist_egg

install: bdist_egg
	sudo $(SETUP) install
	sudo $(SETUP2) install

release:
	zenity --question
	$(SETUP) sdist bdist_egg upload
	$(SETUP2) bdist_egg upload
