# Simple Makefile for Django project routines
# Based on https://github.com/dgladkov/django-project-template/blob/master/Makefile

project=$(shell pwd)
scripts=$(project)/scripts
processes=4
user=www-data # owner of the socket, normally should be nginx user
instance=production # application instance

clean:
	-rm -rf build
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;
	-rm -rf hotel.egg-info

test: clean
	python $(scripts)/manage.py test

fresh_syncdb:
	-rm -f $(project).sqlite
	python $(scripts)/manage.py syncdb --noinput

syncdb:
	python $(scripts)/manage.py syncdb --noinput

collectstatic:
	python $(scripts)/manage.py collectstatic

run:
	python $(scripts)/manage.py runserver 0.0.0.0:8000
