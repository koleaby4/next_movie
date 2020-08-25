export const selectors = {
    title: '.title',
    plot: '.plot',
    imdb_rating: '.imdb_rating',
    reviews_header: '.reviews-header',
    imdb_rating: '.imdb_rating',
    reviews_list: '.reviews-list',
    no_reviews: '.no-reviews',
}

export const assertMovieDetail = (title, imdb_rating) => {
    assertTitle(title)

    cy.get(selectors.plot).should('be.visible')
    cy.get(selectors.reviews_header).should('be.visible')

    assertImdbRating(imdb_rating)
}

export const assertTitle = title =>
    cy.get(selectors.title).contains(title)

export const assertPlot = plot =>
    cy.get(selectors.plot).contains(plot)

export const assertImdbRating = imdb_rating =>
    cy.get(selectors.imdb_rating).contains(imdb_rating)

export const assertNoReviews = () =>
    cy.get(selectors.no_reviews).contains('Be the first to review this movie')

export const assertHasReview = (reviewText) =>
    cy.get(selectors.reviews_list).contains(reviewText)
