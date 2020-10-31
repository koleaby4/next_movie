# next_movie

Welcome to `next_movie` - a movie information portal developed by Nicolai Negru<br>
as the 4th (and final) milestone project at Code Institute's [Full-stack web developer course](https://codeinstitute.net/full-stack-software-development-diploma-uk)

The target group of this website consists of users who:
* wish to quickly identify which next movie is worth watching
* look for movie details and ratings
* are interesting in getting insights into their watching patterns / statistics.

# Contents:

<To Be added>

# Goals

## Project Goals

The initial project goal is to attract audience by providing information about movies.

It starts with two main categories:
* Best Ever - movies, which historically have been recognised as the most successful movie
* Now Playing - movies which currently can be seen in the cinemas across the world

<p>Both lists are available to all users - registered and unregistered.</p>

The project is looking to build deeper relationship with the users by inviting them to register account.<br>
By signing up users will be able to:
* access public content of movie details page
* receive push notifications for highly rated (imdb rating 7+) movies added to the database
* mark movies as `Watched` to hide them on `Best Ever` page
* see a part of user's profile statistics

<p>In the future this will open opportunities for data analysis, advertising and referral fees</p>

Finally, the website is aiming to start generating an income stream.<br>
For one-off fee of £9.99 registered users can become `Prime Members`, getting access to:
* movie reviews
* further profile statistics
* [in the future - discounts to movie-related merchandise]

## Users' Goals

* Users who rely on ratings, get instant access the list of `Best Ever` movies
* People who consider going to cinema, can see what's `Now Playing`
* Using search to quickly see ratings and review of a movie
* Receive notifications of new highly rated movies
* Ability to navigate website on mobile / tablet / desktop devices

# User experience and design decisions

## Font and colour choices

We assume that the user visiting our website comes in a special "movie-mood".<br>
In order to preserve it, our designs had to be neutral and non-distracting.

As a result, the following conventional colours were chosen:
* white background
* dark grey header and footer
* [calming blue](https://www.verywellmind.com/the-color-psychology-of-blue-2795815) for Call-To-Action buttons
* reassuring [green](https://www.verywellmind.com/color-psychology-green-2795817) for icons indicating already unlocked features

It was decided to use [Lora Google font](https://fonts.google.com/specimen/Lora#about)<br>
because of its contemporary memorable style and friendly curves resulting in clear and functional visuals.

# Project Management

## User Stories

All user stories have been tracked using GitHub's [issues section](https://github.com/koleaby4/next_movie/issues?utf8=%E2%9C%93&q=is%3Aissue).
GitHub Issues is a lightweight equivalent of [Jira](https://www.atlassian.com/software/jira), <br>
which is widely used for planning and tracking software development activities.

By default all tickets represent functional user stories. <br>
Example of a user story: [Navbar on the top](https://github.com/koleaby4/next_movie/issues/28)

Tickets with ['bug' label](https://github.com/koleaby4/next_movie/issues?q=label%3Abug),
represent defects in code, which have been found during development and testing.

Additional ['NFR' labels](https://github.com/koleaby4/next_movie/issues?q=label%3ANFR)
have been introduced to help marking and filtering Non-Functional Requirements.

Finally, ['Future' labels](https://github.com/koleaby4/next_movie/issues?q=label%3Afuture)
were used for stories planned for future releases.


## Wireframes

[Balsamiq](https://balsamiq.com) was used to develop wireframes for this project during the requirements collection phase.<br>
The tool allows to quickly create sketches of pages, amend them if need be and export.

To simplify and speed up development, the wireframes were embedded into user stories - see [issue#20](https://github.com/koleaby4/next_movie/issues/20) as an example.


A full collection of the wireframes can also be seen in the [wireframes folder](https://github.com/koleaby4/next_movie/tree/master/wireframes)

ToDo: /!\


## Non-Functional considerations

* The Website will have a flat easy to navigate structure
* The Content on the website will dynamically adjust for devices with various screen sizes
* To maintain sufficient load speed, movies information retrieved from 3rd party services will be stored in the application's database
* Payment information will be processed using Stripe and will not be stored in the the application's database
* All security keys and sensitive configuration will be managed using environment variables ans [secrets.json](https://github.com/koleaby4/next_movie/blob/master/secrets.json) config file
* Our website consumes data from several external sources - we should continue operate even if data coming through is incomplete or inconsistent

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

# Resources

1. Front-end style inspirations https://startbootstrap.com/templates/
2. Responsive photo grid https://css-tricks.com/seamless-responsive-photo-grid
3. normalize.css https://github.com/necolas/normalize.css/
4. omdb api
5. rapid api
6. other movies resourse - TBC
7. plotly charting library
8. google fonts
9. ion-icons

# Architecture / design decisions

to be added
