# next_movie

# Deployment to heroku

* Create app in heroku website
* Connect it to github and enable automated deployments
* `pip install gunicorn`
* `pip freeze > requirements.txt`
* Create `Progfile`
* Set python version `runtime.txt`
* `git push` to trigger deployment

# Postgresql configuration

* Add postgresql to heroku app using [these steps](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres)
* Fetch configuration from HEroku > App > heroku-postgresql > settings
* Add respective configuration to django project > settings > DATABASES distionary
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* open app `<app_url>/admin` and login with the above user

# Testing

We use several layers of tests to verify our functionality

## Unit tests

[Unit tests](https://en.wikipedia.org/wiki/Unit_testing) are our lowest level of test, which we use to verify:
 * models
 * views
 * usage of the correct templates

We use unit testing framework provided by Django and respective 3rd party applications (for example [allauth](https://django-allauth.readthedocs.io/)).<br>
Unit tests can be found in `tests.py` files of the respective application folders (for example `users/tests.py`).

## System tests

We also use [system tests](https://en.wikipedia.org/wiki/System_testing) to verify end-to-end functionality of the whole website.<br>
[Cypress](https://www.cypress.io/) is a very popular testing framework which allows user-like interacting with websites and verifying page content.
