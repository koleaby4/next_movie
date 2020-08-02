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
