import * as signup_helpers from './signup_helpers'
import * as login_helpers from './login_helpers'

export const navbar_selectors = {
    logo: '.logo',
    search_input: '.search-input',
    search_button: '.search-button',
    signup_link: '.sign-up',
    login_link: '.login',
    logout_link: '.logout',
    profile: '.profile'
}


export function clickSingUp() {
    cy.get(navbar_selectors.signup_link).click()
    signup_helpers.assertOnSignUpPage()
}

export function clickLogin() {
    cy.get(navbar_selectors.login_link).click()
    login_helpers.assertOnLoginPage()
}

export function clickLogOut() {
    cy.get(navbar_selectors.logout_link).click()
}

export function assertAlwaysPresentNavbarElements() {
    cy.get(navbar_selectors.logo).should('be.visible')
    cy.get(navbar_selectors.search_input).should('be.visible')
    cy.get(navbar_selectors.search_button).should('be.visible')
}

export function assertUnauthenticatedUserNavbar() {
    assertAlwaysPresentNavbarElements()
    cy.get(navbar_selectors.signup_link).should('be.visible')
    cy.get(navbar_selectors.login_link).should('be.visible')
}

export function assertAuthenticatedUserNavbar() {
    assertAlwaysPresentNavbarElements()
    cy.get(navbar_selectors.profile).should('be.visible')
    cy.get(navbar_selectors.logout_link).should('be.visible')
}


export function assertOnLoginPage(){
    assertUnauthenticatedUserNavbar()

}
