import * as navbar_helpers from './navbar_helpers'

export const gotoLandingPage = (authenticated = false) => {
  cy.visit("/")
  if (authenticated) {
    navbar_helpers.assertAuthenticatedUserNavbar()
  } else {
    navbar_helpers.assertUnauthenticatedUserNavbar()
  }
}



export const random_email = () => Date.now().toString() + "@test.co.uk"
export const PASSWORD = "Str0ngP@ssw0rd!"
