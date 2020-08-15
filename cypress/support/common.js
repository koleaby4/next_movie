import * as navbar_helpers from './navbar_helpers'

export const gotoLandingPage = (authenticated = false) => {
  cy.visit("/")
  if (authenticated) {
    navbar_helpers.assertAuthenticatedUserNavbar()
  } else {
    navbar_helpers.assertUnauthenticatedUserNavbar()
  }
}
