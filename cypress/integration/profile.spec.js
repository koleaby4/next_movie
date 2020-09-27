/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as login_helpers from "../support/login_helpers";
import * as common from "../support/common";
import * as profile_helpers from "../support/profile_helpers";
import * as data from "../support/data";
import * as movie_detail_helpers from "../support/movie_detail_helpers";
import * as movies_helpers from "../support/movies_helpers";


context('User Tests', () => {

  beforeEach(() => {
    common.gotoLandingPage()
  })


  it('Existing user can login and log out', () => {

    navbar_helpers.clickLogin()
    navbar_helpers.assertUnauthenticatedUserNavbar()

    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)
    navbar_helpers.assertAuthenticatedUserNavbar()

    movies_helpers.assertMovieCard("Portrait of a Lady on Fire")
      .click()

    movie_detail_helpers.assureMovieMarkedWatched()

    navbar_helpers.clickProfile()

    profile_helpers.assertProfileContent(data.REGISTERED_PAID_EMAIL)

  })

})
