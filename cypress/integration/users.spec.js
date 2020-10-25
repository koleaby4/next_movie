/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as signup_helpers from "../support/signup_helpers";
import * as login_helpers from "../support/login_helpers";
import * as logout_helpers from "../support/logout_helpers";
import * as common from "../support/common";
import * as data from "../support/data";

context('User Tests', () => {

  beforeEach(() => {
    common.gotoLandingPage()
  })

  it('New user can be registered', () => {
    navbar_helpers.clickSingUp()
    signup_helpers.createNewUser()
  })

  it('Existing user can login and log out', () => {

    login_helpers.loginAs(data.REGISTERED_EMAIL)

    navbar_helpers.clickLogOut()

    navbar_helpers.clickMyAccount()
    cy.get(navbar_helpers.selectors.logoutLink).should("not.exist")
  })


  it('Validation error when trying to sign up with known email', () => {
    navbar_helpers.clickSingUp()
    signup_helpers.createNewUser(data.REGISTERED_EMAIL)
    cy.contains("A user is already registered with this e-mail address.")
  })

})
