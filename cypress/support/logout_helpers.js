import * as navbar_helpers from './navbar_helpers'

export const selectors = {
    logoutButton: '.logout-button'
}


export const logOut = () => {
    cy.get(selectors.logoutButton).click()
}
