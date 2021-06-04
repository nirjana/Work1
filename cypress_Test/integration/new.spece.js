/// <reference types="Cypress" />

Cypress.on('uncaught:exception', (err, runnable) => {
    return false;
  });

describe('My First Test', function() {
    it('Visits the Url', function() {
      cy.visit('https://www.techlistic.com/p/selenium-practice-form.html')
    cy.contains('Selenium Practice Form').should('have.text','Selenium Practice Form')
    
    })
}) 