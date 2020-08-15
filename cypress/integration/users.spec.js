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
    const email = signup_helpers.createNewUser()
    navbar_helpers.assertAuthenticatedUserNavbar()

  })

  it('Existing user can login and log out', () => {

    navbar_helpers.clickLogin()
    navbar_helpers.assertUnauthenticatedUserNavbar()

    login_helpers.loginAs(data.REGISTERED_EMAIL)
    navbar_helpers.assertAuthenticatedUserNavbar()

    navbar_helpers.clickLogOut()
    logout_helpers.logOut()
  })

})
