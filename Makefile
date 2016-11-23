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

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

migrate-heroku-stage:
	@heroku run python manage.py migrate --remote stage

migrate-heroku-prod:
	@heroku run python manage.py migrate --remote prod