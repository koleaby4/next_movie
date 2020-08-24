/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as movies_helpers from "../support/movies_helpers";
import * as login_helpers from "../support/login_helpers";
import * as common from "../support/common";
import * as data from "../support/data";

context('Movies Tests', () => {

  it('Godfather movie card is shown for unauthenticated users', () => {

    common.gotoMoviesPage()
    movies_helpers.assertMovieCard("The Shawshank Redemption")
    cy.get(".card img").should('be.visible')
  })

  it('The Dark Knight movie card is shown for authenticated users', () => {
    common.gotoLandingPage()

    navbar_helpers.clickLogin()
    login_helpers.loginAs(data.REGISTERED_EMAIL)

    common.gotoMoviesPage(true)
    movies_helpers.assertMovieCard("The Dark Knight")
  })
})
