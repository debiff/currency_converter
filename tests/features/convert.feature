Feature: Testing the convert API
  Users should be able to submit GET requests to a web service,
  in order to perform the currency conversion for a given date


  Scenario Outline: Get amount converted in a given date
    Given the convert API service is queried to convert "<amount>" "<src_currency>" in "<dst_currency>" in data "<reference_date>"
    Then the response status code is "200"
    And the response contains the amount converted "<result>"

    Examples: Conversions
      | src_currency | dst_currency | amount | reference_date | result |
      | USD          | GBP          | 50.3   | 2019-10-23     | 39.08  |
      | NOK          | CHF          | 540    | 2019-10-24     | 58.7   |
      | PHP          | AUD          | 0      | 2019-10-25     | 0.0    |