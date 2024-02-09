Feature: Comprehensive User Email Interaction

  Scenario: User successfully manages email interactions including attachment
    Given the user logs in with correct credentials
    Then the user should see the inbox
    When the user creates an email from contacts and adds an attachment
    Then the email with the attachment should be successfully sent
    When the user logs out
    Then the user should see the login page
