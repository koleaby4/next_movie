import * as data from './data'

export const selectors = {
    email: "input[type=email]",
    password: "input[type=password]",
    signupButton : "form button[type=submit]"
}

export const clickSignUpButton = () =>
    cy.get(selectors.signupButton).contains("Sign up").click()

export function assertOnSignUpPage(){
    cy.get(selectors.email).should('be.visible')
    cy.get(selectors.password).should('be.visible')
    cy.get(selectors.signupButton).should('be.visible')
}

export const createNewUser = (email=data.getRandomEmail()) => {
    cy.get(selectors.email).type(email)
    cy.get(selectors.password).type(data.PASSWORD)
    clickSignUpButton()
    return email
}
