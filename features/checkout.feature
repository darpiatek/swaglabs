Feature: Successful end-to-end purchase flow on Swag Labs

  This scenario validates that a standard user can complete
  a full purchase flow on the Swag Labs e-commerce application.

  Background:
    Given The user is on the Swag Labs login page

  Scenario: Standard user completes a purchase successfully
    When The standard_user logs in with valid credentials
    And The user adds the following products to the cart:
      | product name                |
      | Sauce Labs Backpack         |
      | Sauce Labs Bolt T-Shirt     |
    And The user navigates to the shopping cart
    And The user proceeds to the checkout step
    And The user enters the checkout information:
      | firstName | lastName | postalCode |
      | John      | Doe      | 12345      |
    And The user continues to the order overview page
    And The user validates the order total
    And The user finishes the checkout
    Then A confirmation message THANK YOU FOR YOUR ORDER is displayed
    And The user logs out successfully