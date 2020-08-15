import * as navbar_helpers from './navbar_helpers'
import * as data from './data'

export const selectors = {
    email: 'input[type=email]',
    password: 'input[type=password]',
    login_button: '.login-button'
}

export function assertOnLoginPage(){
    navbar_helpers.assertUnauthenticatedUserNavbar()
    cy.get(selectors.email).should('be.visible')
    cy.get(selectors.password).should('be.visible')
    cy.get(selectors.login_button).should('be.visible')
}

export const login_as = (email, password=data.PASSWORD) => {
    cy.log(selectors.login_button)
    cy.get(selectors.email).type(email)
    cy.get(selectors.password).type(password)
    cy.get(selectors.login_button).click()
}
