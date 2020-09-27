export const selectors = {
    emailAddress: '.email',
    watchedMoviesAverageRating: '.watched-movies-average-rating',
}

export const assertProfileContent = email => {
    cy.get(selectors.emailAddress).contains(email)
    cy.get(selectors.watchedMoviesAverageRating).should('be.visible')
}
