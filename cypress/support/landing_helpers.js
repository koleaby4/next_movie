export const selectors = {
    carouselItems: '.carousel-item',

    freeContentHeartOutline: 'ion-icon[name=heart-outline]',
    registeredUserHalfHeart: 'ion-icon[name=heart-half]',
    primeMemberFullHeart: 'ion-icon[name=heart]',

    signupButton: '.sign-up-button',
    only4registeredUsersMessage: '.only-4-registered-users-message',

    paymentButton: '[test-data=payment-form] button[type=submit]',
}

export const assertPublicContent = () => {
    cy.get(selectors.carouselItems).its("length").should("be.eq", 4)
    cy.get(selectors.freeContentHeartOutline).scrollIntoView().should('be.visible')
}

export const assertLoggedInContent = () => {
    assertPublicContent()

    cy.get(selectors.registeredUserHalfHeart).should("be.visible")
    cy.get(selectors.signupButton).should("not.exist")
}
export const assertPrimeMemberContent = () => {
    assertLoggedInContent()

    cy.get(selectors.primeMemberFullHeart).should("be.visible")
    cy.get(selectors.paymentButton).should("not.exist")
}
