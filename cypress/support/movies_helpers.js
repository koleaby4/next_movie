export const selectors = {
    movie_card: '.card',
    movie_title: '.card .card-body',
    card_image: '.card img'
}

export const assertMovieCard = title =>
    cy.get(selectors.movie_card).contains(title)
    .parents(selectors.movie_card)
    .then($card => cy.wrap($card).find('img').should('be.visible'))
