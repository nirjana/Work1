
/// <reference types="cypress"/>

Cypress.on('uncaught:exception', (err, runnable) => {
    return false;
  });

describe('My First Test', function() {
    it('Visits the Url', function() {
      cy.visit('https://www.techlistic.com/p/selenium-practice-form.html')
    })

    it('[formS]UploadFile', function() {
      cy.get('#photo').click()
      const filepath = 'img.jpg'
      cy.get('input[type="file"]').attachFile(filepath)
      //cy.contains('Selenium Practice Form').should('have.text','Selenium Practice Form')
      })  
      
    
    it('[form]EnterFirstName', function() {
    cy.get(':nth-child(12) > input').type('Sujata')


  })
  it('[form]EnterLastName', function() {
    cy.get(':nth-child(15) > input').type('gaihre')

})

it('[form]ChooseGender', function() {
    cy.get('#sex-0').click()

})

it('[form]YearOfExperience', function() {
    cy.get('#exp-1').click()
    cy.get('#exp-2').click()
    
})
it('[form]EnteringDate', function() {
cy.get('#datepicker').click()  
cy.get('#datepicker').type('6/1/2121')
})
it('[form]ChooseProfession', function() {
cy.get('#profession-0').click()
cy.get('#profession-1').click()

})
it('[form]ChooseAutomationTool', function() {
cy.get('#tool-0').click()
cy.get('#tool-1').click()
cy.get('#tool-2').click()

})
it('[form]SelectContinents', function() {
cy.get('#continents').select('Antartica')
})
it('[formS]ContentText', function() {
cy.contains('Selenium Practice Form').should('have.text','Selenium Practice Form')
})  

it('[form]Button', function() {
cy.get('#submit').click()

})

})
