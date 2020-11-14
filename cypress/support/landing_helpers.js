export const selectors = {
    carouselItems: '.carousel-item',

    freeContentIcon: 'ion-icon[name=bicycle-outline]',
    registeredUserIcon: 'ion-icon[name=car-sport-outline]',
    primeMemberIcon: 'ion-icon[name=rocket-outline]',

    signupButton: '.sign-up-button',
    only4registeredUsersMessage: '.only-4-registered-users-message',

    paymentButton: '[test-data=payment-form] button[type=submit]',
}

export const assertPublicContent = () => {
    cy.get(selectors.carouselItems).its("length").should("be.eq", 4)
    cy.get(selectors.freeContentIcon).scrollIntoView().should('be.visible')
}

export const assertLoggedInContent = () => {
    assertPublicContent()

    cy.get(selectors.registeredUserIcon).should("be.visible")
    cy.get(selectors.signupButton).should("not.exist")
}
export const assertPrimeMemberContent = () => {
    assertLoggedInContent()

    cy.get(selectors.primeMemberIcon).should("be.visible")
    cy.get(selectors.paymentButton).should("not.exist")
}
