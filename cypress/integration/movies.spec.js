/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as movies_helpers from "../support/movies_helpers";
import * as movie_detail_helpers from "../support/movie_detail_helpers";
import * as login_helpers from "../support/login_helpers";
import * as common from "../support/common";
import * as data from "../support/data";

context('Movies Tests', () => {

  it('Unauthenticated user redirected to login page when navigating to movie details', () => {

    common.gotoMoviesPage()
    movies_helpers.assertMovieCard("The Shawshank Redemption")
      .click()
    login_helpers.assertOnLoginPage()
  })

  it('Movie details shown for authenticated non-prime users', () => {
    common.gotoLandingPage()

    navbar_helpers.clickLogin()
    login_helpers.loginAs(data.REGISTERED_EMAIL)
    navbar_helpers.assertPrimeMembershipLink(true)

    common.gotoMoviesPage(true)
    movies_helpers.assertMovieCard("The Dark Knight")
      .click()

    movie_detail_helpers.assertMovieDetail("The Dark Knight", "9.0")

    const plot = "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
    movie_detail_helpers.assertPlot(plot)

    movie_detail_helpers.assertNoReviews()
    movie_detail_helpers.assertPrimeInvitationShown()
  })

  it('Reviews are shown on movie details', () => {
    common.gotoLandingPage()

    navbar_helpers.clickLogin()
    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)
    navbar_helpers.assertPrimeMembershipLink(false)

    common.gotoMoviesPage(true)
    movies_helpers.assertMovieCard("Portrait of a Lady on Fire")
      .click()

    movie_detail_helpers.assertHasReview("Wonderful movie (by registered_paid_user)")
    movie_detail_helpers.assertWatchedMovieBlockShown()

  })

  it('Watched / Not Watched toggle for prime members', () => {
    common.gotoLandingPage()

    navbar_helpers.clickLogin()
    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)

    common.gotoMoviesPage(true)
    movies_helpers.assertMovieCard("Portrait of a Lady on Fire")
      .click()

    movie_detail_helpers.assertWatchedMovieBlockShown()

    movie_detail_helpers.assureMovieMarkedNotWatched()

    movie_detail_helpers.toggleWatchedStatus()
    movie_detail_helpers.assertMovieMarkedWatched()

  })

})
