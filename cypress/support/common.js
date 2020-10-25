import * as navbar_helpers from './navbar_helpers'

export const gotoLandingPage = (authenticated = false) => {
  cy.visit("/")
  navbar_helpers.assertNavbarElements()
}


export const gotoMoviesPage = () => {
  cy.visit("movies")
  navbar_helpers.assertNavbarElements()
}
