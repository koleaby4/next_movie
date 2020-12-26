# Overview

Welcome to `Next_movie` - a movie information portal developed by [Nicolai Negru](linkedin.com/in/nicolai-negru) as the 4th (and final) milestone project at Code Institute's [Full-stack web developer course](https://codeinstitute.net/full-stack-software-development-diploma-uk).

The application can be accessed on https://koleaby4-next-movie.herokuapp.com/

The target group of this website consists of users who:
* wish to quickly identify which next movie is worth watching next
* look for movie details and ratings
* are interesting in getting insights into their watching patterns / statistics.

# Contents:

- [Overview](#overview)
- [Contents:](#contents)
- [Goals](#goals)
  - [Project Goals](#project-goals)
  - [Users' Goals](#users-goals)
- [Features](#features)
  - [Implemented functionality](#implemented-functionality)
  - [Features to be added in the future](#features-to-be-added-in-the-future)
- [User experience and design decisions](#user-experience-and-design-decisions)
  - [Font and colour choices](#font-and-colour-choices)
  - [Non-Functional considerations](#non-functional-considerations)
- [Project Management](#project-management)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Database](#database)
  - [Application resilience to invalid / missing data](#application-resilience-to-invalid--missing-data)
  - [Bird's-eye view on tables relationships](#birds-eye-view-on-tables-relationships)
    - [`Movie` model](#movie-model)
    - [`Review` model](#review-model)
    - [`CustomUser` model](#customuser-model)
    - [`Profile` model](#profile-model)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites)
  - [Deploying and running locally](#deploying-and-running-locally)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Testing](#testing)
  - [Unit tests](#unit-tests)
  - [System tests](#system-tests)
    - [How to use Cypress](#how-to-use-cypress)
  - [Compatibility tests](#compatibility-tests)
  - [Defect Management](#defect-management)
- [Payments](#payments)
- [Performance and cost-efficiency](#performance-and-cost-efficiency)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Libraries:](#libraries)
  - [Tools](#tools)
  - [3rd party services](#3rd-party-services)
  - [Databases](#databases)
- [Other Resources](#other-resources)


# Goals

## Project Goals

The initial project goal is to attract audience by providing information about movies.

It starts with two main categories:
* `Best Ever` - movies, which historically have been recognised as the most successful movie
* `Now Playing` - movies which currently can be seen in the cinemas across the world

<p>Both lists are available to all users - registered and unregistered.</p>

The project is looking to build a deeper relationship with the users by inviting them to register an account.<br>
By signing up users will be able to:
* access public content of movie details page
* receive push notifications for highly rated (imdb rating 7+) movies added to the database
* mark movies as `Watched` to hide them on `Best Ever` page
* see a part of user's profile statistics

<p>In the future this will open opportunities for data analysis, advertising and referral fees.</p>

Finally, the website is aiming to start generating an income stream.<br>
For one-off fee of £9.99 registered users can become `Prime Members`, getting access to:
* movie reviews
* further profile statistics
* [in the future - discounts to movie-related merchandise and cinema tickets]

## Users' Goals

* users who rely on ratings, get instant access the list of `Best Ever` movies
* people who consider going to cinema, can see what's `Now Playing`
* using search to quickly see ratings and review of a movie
* receive notifications of new highly rated movies
* ability to navigate website on mobile / tablet / desktop devices

# Features

## Implemented functionality

Available to everyone:
* view list of `Best Ever` movies (dynamically exclude movies marked as `watched` by the current user)
* view list of `Now Playing` movies
* account registration, confirmation email, login and log out
* search movies by name

Available to registered users only:
* view movie details
* mark movies as `watched` / `not watched` from movie detail page
* view list of all `watched` movies on (yes, you guessed it!) `/watched` page
* push notifications when new good movies are persisted to the database
* access some statistics about watched movies on profile page

Available to Prime Members only:
* access movie reviews on `movie detail` page
* additional statistics about watched movies on profile page

## Features to be added in the future

* connect to Google Analytics and identify most visited pages and potential stumbling blocks in the users' journey
* redirect to the cinemas showing respective movies in order to collect referral fees
* scheduled updates of the reviews for persisted movies
* reset password functionality
* performance optimisations for searches returning a large number of movies

A full list of `future` tickets can be found [here](https://github.com/koleaby4/next_movie/issues?q=is%3Aissue+is%3Aopen+label%3Afuture).

# User experience and design decisions

## Font and colour choices

We assume that the user visiting our website comes in a special "movie-mood".<br>
In order to preserve it, our designs had to be neutral and non-distracting.

As a result, the following conventional colours were chosen:
* white background
* dark grey header and footer
* [calming blue](https://www.verywellmind.com/the-color-psychology-of-blue-2795815) for Call-To-Action buttons
* reassuring [green](https://www.verywellmind.com/color-psychology-green-2795817) for icons indicating already unlocked features

It was decided to use [Open Sans Google font](https://fonts.google.com/specimen/Open+Sans?selection.family=Open+Sans)<br>
because of its contemporary memorable style and friendly curves resulting in clear and functional visuals.

## Non-Functional considerations

* the website will have a flat easy to navigate structure
* the content on the website will dynamically adjust for devices with various screen sizes
* to maintain sufficient load speed, movies information retrieved from 3rd party services will be stored in the application's database
* payment information will be processed using Stripe and will not be stored in the application's database
* all security keys and sensitive configuration will be managed using environment variables and [secrets.json](https://github.com/koleaby4/next_movie/blob/master/secrets.json) config file
* the web site should continue operate even if data coming from 3rd party services is incomplete or inconsistent

# Project Management

## User Stories

All user stories have been tracked using GitHub's [issues section](https://github.com/koleaby4/next_movie/issues?utf8=%E2%9C%93&q=is%3Aissue).
GitHub Issues is a lightweight equivalent of [Jira](https://www.atlassian.com/software/jira), which is widely used for planning and tracking software development activities.

Tickets grouping and filtering approach:
1. by default all tickets represent functional user stories. Example of a user story: [#28 - Navbar on the top](https://github.com/koleaby4/next_movie/issues/28)
2. tickets with ['bug' label](https://github.com/koleaby4/next_movie/issues?q=label%3Abug), represent defects in code, which have been found during development and testing.
3. Additional ['NFR' labels](https://github.com/koleaby4/next_movie/issues?q=label%3ANFR) have been introduced to help marking and filtering Non-Functional Requirements.
4. [`Compatibility` labels](https://github.com/koleaby4/next_movie/labels/compatibility) were used to mark tickets related to browser / platform / screen size compatibility
5. ['Future' labels](https://github.com/koleaby4/next_movie/issues?q=label%3Afuture) were used for stories planned for future releases.


## Wireframes

[Balsamiq](https://balsamiq.com) was used to develop wireframes for this project during the requirements collection phase.<br>
The tool allows to quickly create sketches of pages, amend them if need be and export.

To simplify and speed up development, the wireframes were embedded into user stories - see  [issue#49](https://github.com/koleaby4/next_movie/issues/49) and [issue#50](https://github.com/koleaby4/next_movie/issues/50) as an example.


A full collection of the wireframes can also be seen in the [wireframes folder](https://github.com/koleaby4/next_movie/tree/master/wireframes)


# Database

`Next_movie` website is using PostgreSQL for storing the data.<br>

The structure of the database was emerging organically during the implementation.<br>
That approach focuses on real business needs and prevents over-engineering by keeping [You aren't gonna need it](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) principle in mind.


## Application resilience to invalid / missing data

Very often in the software development world, we have control over the data our application deals with.<br>
`Next_movie` is a little bit different in that it relies primarily on the data fetched from a number of 3rd party APIs.

As the development of this project progressed, we've learned that there is a lot of inconsistent and missing data<br>
in the responses we were receiving. A few examples to consider:
* `1975-` as a movie's release year
* missing poster urls and review ratings
* movies present in `imdb8.p.rapidapi.com` APIs, but missing from `api.themoviedb.org`

To allow our website cope with these data anomalies:
* safety checks were added where possible
* many data model fields were marked as null-able
* extensive logging was put in place
* exception handling logic was instructed to skip persisting unrepairable 3rd party data

## Bird's-eye view on tables relationships

Structure of the custom tables and relationships among them is represented on this chart:

<img src="https://github.com/koleaby4/next_movie/blob/master/documentation/images/db_relationships.jpg?raw=true"
     alt="Database tables relationships"
     style="float: left; margin-right: 10px;" />


### `Movie` model

The `Movie` model within the `movies` app, is used to store information about individual movies.

Most of this data comes from `https://imdb8.p.rapidapi.com/title/get-details` end-point,<br>
except of `images` field, which is populated with the data returned by a separate call to `/get-images` API.

Keeping in mind that network calls are expensive, it was decided to store full response payloads returned by `get-details` API in `full_json_details` field.

That approach allows us to retro-fit more fields to the `Movie` model<br>
and populate them with real values from `full_json_details` field.


### `Review` model

The `Review` model within the `movies` app, was introduced to store information about movie reviews.<br>
Each review record contains one single review. Reviews are are linked to respective movie via `movie` foreign key.

During the development we came across movies with a very large number of reviews.<br>
Persisting them all would've been time- and space-consuming.<br>
To address unnecessary pressure on these resources it was decided to persist top n (by default n=5)  latest reviews.<br>
If need be, that configuration can be changed in `movies_collector > get_movie_reviews()` function.

### `CustomUser` model

The `CustomUser` model within the `users` application was introduced to eliminate `username` field<br>
from teh default user registration and authentication process.

`CustomUser` objects are referenced by `Profile` model in the `profile` app via foreign keys.

We also introduced `paid_for_membership` permission.<br>
That permission is granted to the users who purchased `Prime Membership`<br>
and indicates that these users should have access to premium features such as:
  * movie reviews
  * push notifications when new good movies are persisted
  * personalised profile charts reflecting users' watching preferences

### `Profile` model

The `Profile` model within the `profile` app is used as a storage of information about the movies user marked as `watched`.

On the one side, reference to the `users.CustomUser` model is maintained via `OneToOneField` Django models field.<br>
On the other side, we utilise `ManyToManyField` to connect to `movies.Movie` model.

`Profile` model also contains computationally-heavy `watched_movies_years`, `watched_movies_genres` and `watched_movies_average_rating` fields. Their values are dynamically recalculated by specialised `profile.signals` functions every time a movie is marked as `watched` / `unwatched`.

This approach ensures that:
1. correct values are available instantly when users navigate to the `profile` page
2. respective values have to be calculated only when collection of watched movies has changed.


# Deployment

## Prerequisites

Install:
  * [Python3.9+](https://www.python.org/downloads/)
  * [git](https://git-scm.com)

Register and obtain keys for the following services:
  * [Stripe](https://stripe.com)
  * [OMDB](http://www.omdbapi.com/)
  * [RapidApi IMDB](https://rapidapi.com/apidojo/api/imdb8)
  * [TMDB](https://www.themoviedb.org/documentation/api)


## Deploying and running locally

1. Install [postgresql](https://www.postgresql.org/download/)
2. Clone `Next_movie` repository by executing `git clone https://github.com/koleaby4/next_movie.git` in console
3. Change directory to the project folder `cd PATH_TO_THE_PROJECT_FOLDER`
4. Install dependencies `pip install -r requirements.txt`
5. Update `secrets.json` file with your database configuration and API keys
6. Create database structure by running `python3 manage.py migrate`
7. Create superuser `python3 manage.py createsuperuser` and follow instruction in terminal
8. Start the server `python3 manage.py runserver`

The application should now be running on http://127.0.0.1:8000

## Deployment to Heroku

* Create app on Heroku Dashboard
* Configure Postgresql
  * add postgresql to Heroku app using [these steps](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres)
  * fetch configuration from Heroku > App > heroku-postgresql > settings
* Connect the application to github and enable automated deployments
* Execute the following commands in terminal:
    ```
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    ```
* Both `Procfile` (declaring application type and desired http server) and `runtime.txt` (declaring desired Python version) have already been created for you - please review them
* Using Heroku Dashboard, declare and initialise all environment variables found in `secrets.json` file
* `git add . & git commit -m "Configure Heroku" & git push` to persist your changes in Git and trigger deployment
* Wait for deployment to complete and then click `Open App` button to open the website

The application should now be up and running on https://koleaby4-next-movie.herokuapp.com

# Testing

Testing was carried out in several iterations both manually and via automated tests.

## Unit tests

At the lowest level (closest to the code) [unit tests](https://en.wikipedia.org/wiki/Unit_testing) were implemented to verify:
 * models
 * views
 * usage of the correct templates
 * individual functions

I started testing using the testing frameworks provided by [django.test](https://docs.djangoproject.com/en/3.1/topics/testing/overview/).

Unit tests were placed into `tests.py` files of the respective application folders (for example `users/tests.py`)<br>
and  executed against a local instance of Postgresql.

Soon after promoting our project from a local database to the Heroku-hosted instance,<br>
developing and running unit-tests became more challenging because [Heroku does not allow](https://stackoverflow.com/questions/13705328/how-to-run-django-tests-on-heroku) dynamic creation / deletion of test databases.

To work around that security restriction, I continued developing and running tests against a local instance of Postgresql.<br>
That worked for a while, but as the project was becoming more and more complex (calls to 3rd-party APIs, usage of signals to trigger post_save actions, etc)<br>
unit tests had to either cover communication between components or to start employing [python mocks](https://docs.python.org/3/library/unittest.mock.html) to simulate parts of functionality.

On the one hand, unit tests are not supposed to be used for verifying integration among components.<br>
On the other hand, I was reluctant using mocks because their usage in our project would lead to unnecessarily complicated tests and could hide bugs as the codebase continued evolving.

At that point I decided that the project was ready for introducing system tests.

## System tests

[System tests](https://en.wikipedia.org/wiki/System_testing) were introduced to verify end-to-end functionality of the whole website.<br>
I decided to use [cypress](https://www.cypress.io/) for system tests. Cypress is a very popular JavaScript-based testing framework which allows user-like interactions with websites and verifications of page content.

Cypress tests can be found in `cypress\integration` folder, while a number of helper functions are stored in `cypress\support` folder.

Tests are grouped by functionality in the following categories:
* `landing.spec` - cover content of the landing page, which changes depending on whether the user is unauthenticated, logged in or registered as a Prime Member
* `movies.spec` - verifies content of `Best Ever` and `Now PLaying` movie lists
* `profile.spec` - checks content of profile page for both authenticated and Prime Member
* `search.spec` - tests for various search scenarios
* `users.spec` - users creation as well as login/logout functionality

When system tests were implemented, it was decided to remove unit tests for the following reasons:
* I did not have to maintain two databases (local and Heroku-hosted) just to keep the tests working
* to save time for fixing broken unit-tests after changing implementation details of the functions which did not affect visible-to-users functionality of the website (system tests are more robust when it comes to refactoring)
* website's functionality proved to be working and any substantial regression would be captured by system tests. Duplicating test coverage would not provide a higher level of confidence in our code.

The only area not covered by the tests at that point was Stripe payment.<br>
Automated verification of payment scenarios with 3rd party service in this case is complex for the following reasons:
1. [cypress has difficulties working with iframes](https://www.cypress.io/blog/2020/02/12/working-with-iframes-in-cypress/) and for [with Selenium the situation is not much better](https://www.guru99.com/handling-iframes-selenium.html)
2. implementing API-level integration tests proved to be impossible because communication with Stripe back-end is encrypted and the whole process is opaque
3. we do not control that service, so if its implementation details were to change in the future, our tests could cause [false positive](https://en.wikipedia.org/wiki/False_positives_and_false_negatives) failures.

To manage that risk, it was decided to continue verifying payments scenario manually on regular basis.

### How to use Cypress

1. Install cypress by following [these steps](https://docs.cypress.io/guides/getting-started/installing-cypress.html#System-requirements) from cypress' official documentation
2. Open `cypress.json` and set `baseUrl` to the root of the website
3. Open cypress UI by:
   1. opening command line
   2. navigating to the project directory
   3. running the following command `npm run cypress:open`
4. Click "Run all specs"  button to run the tests

## Compatibility tests

To make sure that users of various browsers / platforms / screen sizes could successfully use our website,<br>
a number of [compatibility user stories](https://github.com/koleaby4/next_movie/labels/compatibility) were added to the requirements.

Screen sizes:
* mobile
* tablet
* desktop

Browsers (based on statistics of [browser usage in 2020](https://gs.statcounter.com/browser-market-share/all/europe)):
* Google Chrome
* FireFox
* Microsoft Edge
* Safari

Platforms:
* Windows 10
* Android 11
* iOS 14

Testing all permutations of above parameters would've been impractical,<br>
so the following combinations were chosen to cover most common scenarios:

| Platform | Browser | Screen size |
| -------- | ------- | ----------- |
| Windows 10 | FireFox | Desktop |
| Windows 10 | Edge | Desktop |
| iOS 14 | Safari | Tablet |
| iOS 14 | Safari | Mobile |
| Android 11 | Chrome | Tablet |
| Android 11 | Chrome | Mobile |


## Defect Management

All defects identified during development and testing phase were noted.<br>
When defect could be resolved faster than the overheads of formally documenting it, it was resolved in-place.<br>
In situations when it was not possible to resolve defect on the spot, it was documented using the following format:
* Steps to reproduce
* Expected Results
* Actual Results

See [issue 38](https://github.com/koleaby4/next_movie/issues/38) as an example.

All defects were marked by a ['bug' label](https://github.com/koleaby4/next_movie/issues?q=label%3Abug)

# Payments

Keeping in mind that this website was developed for educational purposes, Stripe payments have been connected to test end-points.<br>
As a result of this, only specific test card details will be accepted when paying for `Prime Membership` on our website

<img src="https://github.com/koleaby4/next_movie/blob/master/documentation/images/test_payment_details.png?raw=true"
     alt="Test Payment Details"
     style="max-width:250px; margin-right: 10px;" />


# Performance and cost-efficiency

Having done an initial research of available free movies data sources, I came to conclusion<br>
that none of them offered a full set of features required for our website.

As a result I decided to combine information from several data sources:
* [OMDb API](http://www.omdbapi.com/) - free but very limited in terms of data available
* [RapidAPI IMDB end-points](https://rapidapi.com/apidojo/api/imdb8) - paid for and restricted on the number of calls we can make
* [The Movie Database (TMDb) API](https://developers.themoviedb.org/3) - free but relies on own movie IDs and thus requires intermediary calls to fetch imdb IDs

To compile together information about every movie, we have to make 3 calls to external APIs to fetch:
  1. core movie information
  2. movie images
  3. movie reviews

Keeping in mind that:
* we are charged for requests to RapidAPI end-points and requests are throttled to max 5 requests / second
* network calls are in general time-consuming
it was important to minimise the number of 3rd API calls.

To address these considerations, movies information once retrieved, is persisted in our internal database. When searching for movie details, we would first check whether this information was previously retrieved. If so - we would use persisted data, otherwise we would fetch and store it.

<img src="https://github.com/koleaby4/next_movie/blob/master/documentation/images/data_flow.png?raw=true"
     alt="Data flow diagram"
     style="max-width:800px; margin-right: 10px;" />

In several parts of our codebase we used multithreading for fetching information in parallel, in order to keep our website's response time to minimum. However even with these performance optimisations the longest chain of calls to get all movie details is fairly complex and time-consuming.

Finally, to increase performance of the website on `Best Ever` and `Now Playing` pages, we introduced caching mechanisms. The first time data is retrieved from 3rd party APIs, the results are stored in `top_rated_cache.json` and `now_playing_cache.json` respectively. Every time users request these lists, the results will be fetched from the cache files. The the application then checks whether the cache files are older than 24h and if so - will spawn a separate thread to fetch the latest data and update the cache. In the meantime cached results will be returned. In this manner the system is not waiting for the latest data to be fetched, but makes sure that cache is updated and the next request will contain most up-to-date results.

# Technologies Used

## Languages

* [Python](https://www.python.org)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.w3schools.com/js/)

## Libraries:

* [Django](https://www.djangoproject.com)
* [allauth](https://django-allauth.readthedocs.io)
* [Bootstrap](https://getbootstrap.com)
* [ion-icons](https://ionicons.com)
* [normalize.css](https://github.com/necolas/normalize.css)
* [Google Fonts](https://fonts.google.com)
* [Plotly Graphing Library](https://plotly.com/nodejs)
* [Gunicorn](https://pypi.org/project/gunicorn)

## Tools

* [Git](https://git-scm.com) and [GitHub](https://github.com/) for source control
* [Visual Studio Code](https://code.visualstudio.com) as development IDE
* [cypress](https://www.cypress.io/) for test automation
* [Database Relationship Visualiser](https://www.dbvis.com) for exactly that - visualising database relationships :)

## 3rd party services

* [OMDb API](http://www.omdbapi.com/)
* [RapidAPI IMDB end-points](https://rapidapi.com/apidojo/api/imdb8)
* [The Movie Database (TMDb) API](https://developers.themoviedb.org/3)
* [Stripe Payments](https://stripe.com)
* [SendGrid Email Delivery Service](https://sendgrid.com)

## Databases

* [PostgreSQL](https://www.postgresql.org)

# Other Resources

* Front-end style inspirations from [Bootstrap Templates](https://startbootstrap.com/templates)
* [Responsive photo grid](https://css-tricks.com/seamless-responsive-photo-grid) for dynamically arranging images
* [coolors.co](https://coolors.co)
