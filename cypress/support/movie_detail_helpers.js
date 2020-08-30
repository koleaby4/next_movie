export const selectors = {
    title: '.title',
    plot: '.plot',
    imdb_rating: '.imdb_rating',
    reviews_header: '.reviews-header',
    imdb_rating: '.imdb_rating',
    reviews_list: '.reviews-list',
    no_reviews: '.no-reviews',
    prime_invitation: '.prime-invitation',
    seen_movie_block: '.seen-movie-block',
    seen_movie_block_icon: '.seen-movie-block ion-icon',
    not_seen_movie_icon: ".not-seen-icon",
    seen_movie_icon: ".seen-icon",
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

export const assertPrimeInvitationShown = () =>
    cy.get(selectors.prime_invitation).should('be.visible')

export const assertSeenMovieBlockShown = () =>
    cy.get(selectors.seen_movie_block).should('be.visible')

export const assertMovieMarkedSeen = () =>
    cy.get(selectors.seen_movie_icon).should('be.visible')

export const assertMovieMarkedNotSeen = () =>
    cy.get(selectors.not_seen_movie_icon).should('be.visible')

export const toggleSeenMovieStatus = () =>
    cy.get(selectors.seen_movie_block_icon).click()

export const assureMovieMarkedNotSeen = () => {
    cy.get(selectors.seen_movie_block).then(seen_block => {
        if (seen_block.find(selectors.seen_movie_icon).length > 0) {
            toggleSeenMovieStatus()
        }
    });

    assertMovieMarkedNotSeen()
}
