import * as signup_helpers from './signup_helpers'
import * as login_helpers from './login_helpers'

export const navbar_selectors = {
    logo: '.logo',
    searchInput: '.search-input',
    searchButton: '.search-button',
    signupLink: '.sign-up',
    loginLink: '.login',
    logoutLink: '.logout',
    profile: '.profile'
}


export const clickSingUp = () => {
    cy.get(navbar_selectors.signupLink).click()
    signup_helpers.assertOnSignUpPage()
}

export const clickLogin = () => {
    cy.get(navbar_selectors.loginLink).click()
    login_helpers.assertOnLoginPage()
}

export const clickLogOut = () =>
    cy.get(navbar_selectors.logoutLink).click()

export const assertAlwaysPresentNavbarElements = () => {
    cy.get(navbar_selectors.logo).should('be.visible')
    cy.get(navbar_selectors.searchInput).should('be.visible')
    cy.get(navbar_selectors.searchButton).should('be.visible')
}

export const assertUnauthenticatedUserNavbar = () => {
    assertAlwaysPresentNavbarElements()
    cy.get(navbar_selectors.signupLink).should('be.visible')
    cy.get(navbar_selectors.loginLink).should('be.visible')
}

export const assertAuthenticatedUserNavbar = () => {
    assertAlwaysPresentNavbarElements()
    cy.get(navbar_selectors.profile).should('be.visible')
    cy.get(navbar_selectors.logoutLink).should('be.visible')
}

export const assertOnLoginPage = () =>
    assertUnauthenticatedUserNavbar()
