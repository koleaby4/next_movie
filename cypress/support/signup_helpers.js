import * as common_helpers from './common'

export const selectors = {
    email: "input[name=email]",
    password: "input[type=password]",
    signup_button : "form button[type=submit]"
}

export const clickSignUpButton = () =>
    cy.get(selectors.signup_button).contains("Sign up").click()

export function assertOnSignUpPage(){
    cy.get(selectors.email).should('be.visible')
    cy.get(selectors.password).should('be.visible')
    cy.get(selectors.signup_button).should('be.visible')
}

export const createNewUser = () => {
    const email = common_helpers.random_email()
    cy.get(selectors.email).type(email)
    cy.get(selectors.password).type(common_helpers.PASSWORD)
    clickSignUpButton()
    return email
}
