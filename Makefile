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

pep8:
	pep8.py --filename=*.py --ignore=W --exclude="manage.py,settings.py" --statistics --repeat $(project)

pylint:
	pylint $(project)  --max-public-methods=50 --include-ids=y --ignored-classes=Item.Meta --method-rgx='[a-z_][a-z0-9_]{2,40}$$'

fresh_syncdb:
	-rm -f $(project).sqlite
	python $(scripts)/manage.py syncdb --noinput

syncdb:
	python $(scripts)/manage.py syncdb --noinput

shell:
	python $(scripts)/manage.py shell

run:
	python $(scripts)/manage.py runserver 0.0.0.0:8000

uwsgi:
	uwsgi -p $(processes) -s /tmp/$(project).sock -H ./env --uid $(user) -w $(project).wsgi.$(instance) --pythonpath ./$(project)
