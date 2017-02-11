install-dev:
	@pip install -r requirements/development.txt

run:
	@python manage.py runserver

shell:
	@python manage.py shell

deploy-stage:
	@git push stage master
	@heroku run python manage.py migrate --remote stage

deploy-prod:
	@git push prod master
	@heroku run python manage.py migrate --remote prod

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

startdev:
	@git remote add stage https://git.heroku.com/lexci-stage.git
	@git remote add prod https://git.heroku.com/lexci.git
	@pip install -r requirements/development.txt
	@python manage.py loaddata fixtures/convenio.json
	@make migrate