install-dev:
	@pip install -r requirements/development.txt

run:
	@python manage.py runserver

shell:
	@python manage.py shell

deploy-stage:
	@git push stage master

deploy-prod:
	@git push prod master
