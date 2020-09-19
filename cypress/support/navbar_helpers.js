import * as signup_helpers from './signup_helpers'
import * as login_helpers from './login_helpers'

export const selectors = {
    logo: '.logo',
    searchInput: '.search-input',
    searchButton: '.search-button',
    signupLink: '.sign-up',
    loginLink: '.login',
    logoutLink: '.logout',
    nowPlayingLink: '.now-playing',
    primeMembershipLink: '.prime-membership-link',
}


export const clickSingUp = () => {
    cy.get(selectors.signupLink).click()
    signup_helpers.assertOnSignUpPage()
}

export const clickLogin = () => {
    cy.get(selectors.loginLink).click()
    login_helpers.assertOnLoginPage()
}

export const clickLogOut = () =>
    cy.get(selectors.logoutLink).click()

export const assertAlwaysPresentNavbarElements = () => {
    cy.get(selectors.logo).should('be.visible')
    cy.get(selectors.searchInput).should('be.visible')
    cy.get(selectors.searchButton).should('be.visible')
    cy.get(selectors.nowPlayingLink).should('be.visible')
}

export const assertUnauthenticatedUserNavbar = () => {
    assertAlwaysPresentNavbarElements()
    cy.get(selectors.signupLink).should('be.visible')
    cy.get(selectors.loginLink).should('be.visible')
}

export const assertAuthenticatedUserNavbar = () => {
    assertAlwaysPresentNavbarElements()
    cy.get(selectors.logoutLink).should('be.visible')
}

export const assertOnLoginPage = () =>
    assertUnauthenticatedUserNavbar()

export const assertPrimeMembershipLink = (expect_visible=true) =>
    cy.get(selectors.primeMembershipLink).should(expect_visible ? 'be.visible' : 'not.exist')

export const searchFor = (term, expected_matches_count) => {
    cy.get(selectors.searchInput).type(term)
    cy.get(selectors.searchButton).click()

    if (expected_matches_count){
        cy.get('.card-body p').each( el => cy.wrap(el).contains(term))
        cy.get('.card-body p').its('length').should('eq', expected_matches_count)
    }
}

export const clickNowPlaying = () => {
    cy.get(selectors.nowPlayingLink).click()
    cy.get('.card').its('length').should('be.gt', 6)
}
