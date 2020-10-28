/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as login_helpers from "../support/login_helpers";
import * as common from "../support/common";
import * as profile_helpers from "../support/profile_helpers";
import * as data from "../support/data";


context('Profile Tests', () => {

  beforeEach(() => {
    common.gotoLandingPage()
  })


  it('No Profile link in MyAccount menu for unauthorised users', () => {
    navbar_helpers.clickMyAccount()
    cy.get(navbar_helpers.selectors.profileLink).should("not.exist")
  })

  it('Partial Profile content for registered users', () => {
    login_helpers.loginAs(data.REGISTERED_EMAIL)
    navbar_helpers.clickProfile()

    profile_helpers.assertFreeProfileContentIsVisible(data.REGISTERED_EMAIL)
    profile_helpers.assertPremiumContentIsHidden()
  })

  it('Full Profile content for prime members', () => {
    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)
    navbar_helpers.clickProfile()

    profile_helpers.assertPremiumProfileContentIsVisible(data.REGISTERED_PAID_EMAIL)
  })

})
