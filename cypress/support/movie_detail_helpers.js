export const selectors = {
    title: '.title',
    plot: '.plot',
    imdb_rating: '.imdb_rating',
    reviews_header: '.reviews-header',
    imdb_rating: '.imdb_rating',
    reviews_list: '.reviews-list',
    no_reviews: '.no-reviews',
    reviews_hidden: '.reviews-container .prime-invitation',
    prime_invitation: '.prime-invitation',
    watched_movie_block: '.watched-movie-block',
    watched_movie_block_icon: '.watched-movie-block ion-icon',
    not_watched_movie_icon: ".not-watched-icon",
    watched_movie_icon: ".watched-icon",
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

export const assertReviewsHidden = () =>
    cy.get(selectors.reviews_hidden).should("be.visible")

export const assertHasReview = (reviewText) =>
    cy.get(selectors.reviews_list).contains(reviewText)

export const assertPrimeInvitationShown = () =>
    cy.get(selectors.prime_invitation).should('be.visible')

export const assertWatchedMovieBlockShown = () =>
    cy.get(selectors.watched_movie_block).should('be.visible')

export const assertMovieMarkedWatched = () =>
    cy.get(selectors.watched_movie_icon).should('be.visible')

export const assertMovieMarkedNotWatched = () =>
    cy.get(selectors.not_watched_movie_icon).should('be.visible')

export const toggleWatchedStatus = () =>
    cy.get(selectors.watched_movie_block_icon).click()

export const assureMovieMarkedNotWatched = () => {
    cy.get(selectors.watched_movie_block).then(watched_block => {
        if (watched_block.find(selectors.watched_movie_icon).length > 0) {
            toggleWatchedStatus()
        }
    });

    assertMovieMarkedNotWatched()
}
