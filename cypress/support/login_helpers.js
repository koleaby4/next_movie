import * as navbar_helpers from './navbar_helpers'
import * as data from './data'

export const selectors = {
    email: 'input[type=email]',
    password: 'input[type=password]',
    loginButton: '.login-button'
}

export const assertOnLoginPage = () => {
    navbar_helpers.assertNavbarElements()
    cy.get(selectors.email).should('be.visible')
    cy.get(selectors.password).should('be.visible')
    cy.get(selectors.loginButton).should('be.visible')
}

export const loginAs = (email, password=data.PASSWORD) => {
    navbar_helpers.clickLogin()
    navbar_helpers.assertNavbarElements()

    cy.log(selectors.loginButton)
    cy.get(selectors.email).type(email)
    cy.get(selectors.password).type(password)
    cy.get(selectors.loginButton).click()
}
