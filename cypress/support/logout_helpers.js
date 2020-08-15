import * as navbar_helpers from './navbar_helpers'

export const selectors = {
    logoutButton: '.logout-button'
}

export function assertOnLoginPage(){
    navbar_helpers.assertUnauthenticatedUserNavbar()
    cy.get(selectors.email).should('be.visible')
    cy.get(selectors.password).should('be.visible')
    cy.get(selectors.login_button).should('be.visible')
}

export const logOut = () => {
    cy.get(selectors.logoutButton).click()
    navbar_helpers.assertUnauthenticatedUserNavbar()
}
