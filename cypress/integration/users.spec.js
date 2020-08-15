/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as signup_helpers from "../support/signup_helpers";
import * as common from "../support/common";

context('User Registration', () => {
  beforeEach(() => {
    common.gotoLandingPage()
    navbar_helpers.clickSingUp()

    const email = signup_helpers.createNewUser()
    navbar_helpers.assertAuthenticatedUserNavbar()
    // cy.get('.navbar-nav').contains('Commands').click()
    // cy.get('.dropdown-menu').contains('Navigation').click()
  })

  it('New user can be registered', () => {


    // const email = Date.now().toString() + "@test.co.uk"
    // const password = uuidv4()

    // cy.contains('Login')

    // cy.get('.assertion-table')
    // .find('tbody tr:last')
    // .should('have.class', 'success')
    // .find('td')
    // .first()
    // // checking the text of the <td> element in various ways
    // .should('have.text', 'Column content')


    // cy.location('pathname').should('include', 'navigation')

    // cy.go('back')
    // cy.location('pathname').should('not.include', 'navigation')

    // cy.go('forward')
    // cy.location('pathname').should('include', 'navigation')

    // // clicking back
    // cy.go(-1)
    // cy.location('pathname').should('not.include', 'navigation')

    // // clicking forward
    // cy.go(1)
    // cy.location('pathname').should('include', 'navigation')
  })

  // it('cy.visit() - visit a remote url', () => {
  //   // https://on.cypress.io/visit

  //   // Visit any sub-domain of your current domain

  //   // Pass options to the visit
  //   cy.visit('https://example.cypress.io/commands/navigation', {
  //     timeout: 50000, // increase total time for the visit to resolve
  //     onBeforeLoad (contentWindow) {
  //       // contentWindow is the remote page's window object
  //       expect(typeof contentWindow === 'object').to.be.true
  //     },
  //     onLoad (contentWindow) {
  //       // contentWindow is the remote page's window object
  //       expect(typeof contentWindow === 'object').to.be.true
  //     },
  //   })
  //   })
})
