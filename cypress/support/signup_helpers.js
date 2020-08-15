import * as data from './data'

export const selectors = {
    email: "input[type=email]",
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
    const email = data.get_random_email()
    cy.get(selectors.email).type(email)
    cy.get(selectors.password).type(data.PASSWORD)
    clickSignUpButton()
    return email
}
