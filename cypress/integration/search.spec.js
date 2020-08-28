/// <reference types="cypress" />

import * as navbar_helpers from "../support/navbar_helpers";
import * as common from "../support/common";

context('Search Tests', () => {

  beforeEach(() => {
    common.gotoLandingPage()
  })

  it('Search for a single match', () => {
    navbar_helpers.searchFor("Schindler's List", 1)
  })

  it('Search with multiple matches', () => {
    navbar_helpers.searchFor("The Lord of the Rings", 3)
  })

  it('Search with NO matches found', () => {
    navbar_helpers.searchFor("This movies does not exist", 0)
    cy.contains("No movies found")
  })

})
