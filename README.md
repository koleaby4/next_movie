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

Unit tests will be executed against a local instance of Postgresql.<br>
This is because our unit testing frameworks have to dynamically create and delete test database.

## System tests

We also use [system tests](https://en.wikipedia.org/wiki/System_testing) to verify end-to-end functionality of the whole website.<br>
[Cypress](https://www.cypress.io/) is a very popular testing framework which allows user-like interactions with websites and verifications of page's content.


### How to use Cypress

1. Install cypress by following [these steps](https://docs.cypress.io/guides/getting-started/installing-cypress.html#System-requirements) from cypress' official documentation
2. Open `cypress.json` and set `baseUrl` to the root of the website
3. Open cypress UI by:
   1. opening command line
   2. navigating to the project directory
   3. running the following command `npm run cypress:open`
4. Click "Run all specs"  button to run the tests
