Feature: HTTP GET
  Scenario: When the http endpoint is called it returns a 200
    Given an http request is sent to the URL
    Then it should return a 200 response code
