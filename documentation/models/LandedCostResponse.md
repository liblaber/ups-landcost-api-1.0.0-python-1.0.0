# LandedCostResponse

**Properties**

| Name     | Type     | Required | Description                                             |
| :------- | :------- | :------- | :------------------------------------------------------ |
| shipment | Shipment | ✅       | Every Landed Cost response must be based on a shipment. |

# Shipment

Every Landed Cost response must be based on a shipment.

**Properties**

| Name                                 | Type                        | Required | Description                                                                                                                                              |
| :----------------------------------- | :-------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| currency_code                        | str                         | ✅       | Specifies the Currency Code set at the commodity level. This currency is applicable for all duty, tax, VAT, and fee at the shipment and commodity level. |
| import_country_code                  | str                         | ✅       | Specifies the Import/Ship-To/Destination/Final country of the shipment. Please check country list in the Appendices section.                             |
| id\_                                 | str                         | ✅       | Specifies the Shipment ID in the Landed Cost quote.                                                                                                      |
| brokerage_fee_items                  | List[BrokerageFeeItems]     | ✅       | An array of Brokerage fees.                                                                                                                              |
| total_brokerage_fees                 | float                       | ✅       | Grand total of all applicable Brokerage fees.                                                                                                            |
| total_duties                         | float                       | ✅       | Total duty amount of this shipment.                                                                                                                      |
| total_commodity_level_taxes_and_fees | float                       | ✅       | Total tax and other fees at commodity level.                                                                                                             |
| total_shipment_level_taxes_and_fees  | float                       | ✅       | Total tax and other fees at shipment level.                                                                                                              |
| total_vat                            | float                       | ✅       | Total VAT of the shipment.                                                                                                                               |
| total_duty_and_tax                   | float                       | ✅       | Grand total of the combined duty, VAT, tax, and other fees of all commodities in this shipment including shipment level taxes and fees.                  |
| grand_total                          | float                       | ✅       | Sum of totalDutyAndTax + totalBrokerageFees                                                                                                              |
| shipment_items                       | List[ResponseShipmentItems] | ✅       | An array of Landed Cost for all valid commodities.                                                                                                       |
| trans_id                             | str                         | ❌       | An identifier unique to the request.                                                                                                                     |
| perf_stats                           | PerfStats                   | ❌       | See ALPerfStats                                                                                                                                          |
| al_version                           | int                         | ❌       | Version number of the instance that processed this request. Default is 1.                                                                                |
| errors                               | Errors                      | ❌       | Error code and description                                                                                                                               |

# PerfStats

See ALPerfStats

**Properties**

| Name           | Type | Required | Description                                               |
| :------------- | :--- | :------- | :-------------------------------------------------------- |
| abs_layer_time | str  | ✅       | Time taken through the abstraction layer in milliseconds. |
| fulfill_time   | str  | ✅       | Time taken to complete the request.                       |
| receipt_time   | str  | ✅       | Time taken to receive the request.                        |

<!-- This file was generated by liblab | https://liblab.com/ -->
