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
    movies_helpers.assertMovieCard("The Shawshank Redemption").click()
    login_helpers.assertOnLoginPage()
  })

  it('Movie details shown for authenticated non-prime users', () => {
    common.gotoLandingPage()

    navbar_helpers.clickMyAccount()
    navbar_helpers.assertPrimeMembershipLinkVisibility(false)
    navbar_helpers.clickMyAccount()

    login_helpers.loginAs(data.REGISTERED_EMAIL)
    navbar_helpers.clickMyAccount()
    navbar_helpers.assertPrimeMembershipLinkVisibility(true)

    common.gotoMoviesPage()
    navbar_helpers.searchFor("Throne of Blood", 1)
    movies_helpers.assertMovieCard("Throne of Blood")
      .click()

    movie_detail_helpers.assertMovieDetail("Throne of Blood", "8.1")

    const plot = "A war-hardened general, egged on by his ambitious wife, works to fulfill a prophecy that he would become lord of Spider's Web Castle."
    movie_detail_helpers.assertPlot(plot)

    movie_detail_helpers.assertReviewsHidden()
    movie_detail_helpers.assertPrimeInvitationShown()
  })

  it('Reviews are shown on movie details for prime members', () => {
    common.gotoLandingPage()

    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)

    navbar_helpers.searchFor("Portrait of a Lady on Fire", 1)
    movies_helpers.assertMovieCard("Portrait of a Lady on Fire")
      .click()

    movie_detail_helpers.assertHasReview("Every frame a painting")
    movie_detail_helpers.assertWatchedMovieBlockShown()

  })

  it('Watched / Not Watched toggle for prime members', () => {
    common.gotoLandingPage()

    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)

    navbar_helpers.searchFor("Portrait of a Lady on Fire", 1)
    movies_helpers.assertMovieCard("Portrait of a Lady on Fire")
      .click()

    movie_detail_helpers.assertWatchedMovieBlockShown()

    movie_detail_helpers.assureMovieMarkedNotWatched()

    movie_detail_helpers.toggleWatchedStatus()
    movie_detail_helpers.assertMovieMarkedWatched()

    movie_detail_helpers.toggleWatchedStatus()
    movie_detail_helpers.assureMovieMarkedNotWatched()
  })

  it('Now playing page is populated', () => {
    common.gotoMoviesPage()
    navbar_helpers.clickNowPlaying()
  })
})
