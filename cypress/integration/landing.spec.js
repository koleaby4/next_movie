/// <reference types="cypress" />

import * as login_helpers from "../support/login_helpers";
import * as common from "../support/common";
import * as data from "../support/data";
import * as landing_helpers from "../support/landing_helpers";


context('Profile Tests', () => {

  beforeEach(() => {
    common.gotoLandingPage()
  })


  it('Content shown to unauthorised users', () => {
    landing_helpers.assertPublicContent()

    cy.get(landing_helpers.selectors.signupButton).should("be.visible")
    cy.get(landing_helpers.selectors.registeredUserIcon).should("not.exist")

    cy.get(landing_helpers.selectors.only4registeredUsersMessage).should("be.visible")
    cy.get(landing_helpers.selectors.paymentButton).should("not.exist")
    cy.get(landing_helpers.selectors.primeMemberIcon).should("not.exist")
  })

  it('Content shown to logged in users', () => {
    login_helpers.loginAs(data.REGISTERED_EMAIL)
    common.gotoLandingPage()

    landing_helpers.assertLoggedInContent()

    cy.get(landing_helpers.selectors.only4registeredUsersMessage).should("not.exist")
    cy.get(landing_helpers.selectors.paymentButton).should("be.visible")
    cy.get(landing_helpers.selectors.primeMemberIcon).should("not.exist")
  })

  it('Content shown to prime members', () => {
    login_helpers.loginAs(data.REGISTERED_PAID_EMAIL)
    common.gotoLandingPage()

    landing_helpers.assertPrimeMemberContent()
  })

})
