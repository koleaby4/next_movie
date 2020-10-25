import * as signup_helpers from './signup_helpers'
import * as login_helpers from './login_helpers'

export const selectors = {
    brand_link: '.navbar-brand',
    searchInput: '.search-input',
    searchButton: '.search-button',
    signupLink: '.sign-up',
    loginLink: '.login',
    logoutLink: '.logout',
    bestEverLink: '.best-ever',
    nowPlayingLink: '.now-playing',
    myAccountDropdown: '#navbarDropdownAccount',
    profileLink: '.profile-link',
    primeMembershipLink: '.prime-membership-link',
}


export const clickSingUp = () => {
    clickMyAccount()
    cy.get(selectors.signupLink).click()
    signup_helpers.assertOnSignUpPage()
}

export const clickMyAccount = () => {
    cy.get(selectors.myAccountDropdown).click()
}

export const clickLogin = () => {
    clickMyAccount()
    cy.get(selectors.loginLink).click()
    login_helpers.assertOnLoginPage()
}

export const clickLogOut = () => {
    clickMyAccount()
    cy.get(selectors.logoutLink).click()
}

export const clickProfile = () => {
    clickMyAccount()
    cy.get(selectors.profileLink).click()

}

export const assertAlwaysPresentNavbarElements = () => {
    cy.get(selectors.brand_link).should('be.visible')
    cy.get(selectors.searchInput).should('be.visible')
    cy.get(selectors.searchButton).should('be.visible')
    cy.get(selectors.bestEverLink).should('be.visible')
    cy.get(selectors.nowPlayingLink).should('be.visible')
    cy.get(selectors.myAccountDropdown).should('be.visible')
}

export const assertUnauthenticatedUserNavbar = () => {
    assertAlwaysPresentNavbarElements()
}

export const assertAuthenticatedUserNavbar = () => {
    assertAlwaysPresentNavbarElements()
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
