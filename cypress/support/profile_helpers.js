export const selectors = {
    summaryCard: '.summary-card',
    descriptionCard: '.description-card',
    genresChartCard: '.genres-chart-card',
    yearsChartCard: '.years-chart-card',

    emailAddress: '.email',
    watchedMoviesAverageRating: '.watched-movies-average-rating',
    watchedMoviesCount: '.watched-movies-count',

    primeInvitation: '.prime-invitation',
}

export const assertFreeProfileContentIsVisible = email => {
    cy.get("h1").contains("Profile")

    cy.get(selectors.summaryCard).should('be.visible')

    cy.get(selectors.emailAddress).contains(email)
    cy.get(selectors.watchedMoviesCount).should('be.visible')
    cy.get(selectors.watchedMoviesAverageRating).should('be.visible')

    cy.get(selectors.descriptionCard).should('be.visible')
}

export const assertPremiumProfileContentIsVisible = email => {
    assertFreeProfileContentIsVisible(email)
    cy.get(selectors.genresChartCard).should('be.visible')
    cy.get(selectors.yearsChartCard).should('be.visible')
}


export const assertPremiumContentIsHidden = () => {
    cy.get(selectors.genresChartCard).should('not.exist')
    cy.get(selectors.yearsChartCard).should('not.exist')
    cy.get(selectors.primeInvitation).should('be.visible')

}
