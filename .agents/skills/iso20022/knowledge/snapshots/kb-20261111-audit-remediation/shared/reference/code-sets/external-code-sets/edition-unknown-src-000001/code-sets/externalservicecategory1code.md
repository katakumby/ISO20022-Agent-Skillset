---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalServiceCategory1Code"]
code_set: "ExternalServiceCategory1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalServiceCategory1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalServiceCategory1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the service category, as published in an external status reason code list.
External code sets can be downloaded from www.iso20022.org.
*`ACMS`-Agreement under which or rules under which the transaction should be processed expressed as a code.
This category encompasses the reporting of fees related to account management services including, inter alia, membership fees and minimum fees (i.e. fees added to small invoices in order to reach the minimum fees agreed for each participant).

*`BICM`-This category encompasses the reporting of all fees related to the management of collateral subject to bilateral agreements (covering central bank financing for marketable and non-marketable assets, non-cleared OTC derivatives and securities financing).
*`CALM`-This category encompasses the reporting of all fees related to cash and liquidity management services.
*`CLEA`-This category encompasses the reporting of fees related to the provision of clearing services.
*`CUST`-This category encompasses the reporting of all fees that are charged per operation such as election instructions. The category is also used to report fees on tax services related to assets under custody together with the processing of corporate actions and meetings events.
*`INSV`-This category encompasses the reporting of all fees related to the provision of information through any kind of means and to the provision of connectivity tools. This includes ISO messaging (inbound or outbound), graphical user interface (GUI) access, connectivity, recharge of security tokens, report subscriptions and the provision of data by any other means (e.g. paper based formats).
*`INVS`-This category encompasses the reporting of all related to specific services provided for investment funds, such as order routing or holder reporting.  The safekeeping and settlement of investment funds and exchange-traded funds should be reported under the Safekeeping Services and Settlement Services categories respectively.
*`ISSU`-This category encompasses the reporting of fees related to the provision of issuer services by a CSD. This includes fees such as issuance and redemptions of securities and management of corporate actions.
*`OTHR`-This category encompasses the reporting of fees related to other services provided which might not be set in a general tariff applicable to all clients, but bilaterally agreed with clients individually. This includes the provision of customised service requests and other support provided to clients such as training and testing access as well as out-of-pocket expenses.
*`PENM`-This category encompasses the reporting of fees related to the recovery of costs associated with the development and maintenance of the penalty mechanism. Note: this category should not be used for the reporting of the penalty itself.
*`REGI`-This category encompasses the reporting of all fees related to the registration of securities.
*`SAFE`-This category encompasses the reporting of all fees that are calculated as basis points applied to the assets under custody. This includes notary, central maintenance and asset servicing fees.
*`SECL`-This category encompasses the reporting of all fees related to securities lending services.
*`PENA`-This category encompasses the reporting of all fees related to the cost recovery of settlement penalties applied by non-EU settlement systems (outside the scope of CSDR settlement discipline).
*`SETT`-This category encompasses the reporting of all fees related to the settlement of securities and/or cash. This includes fees related to the settlement of market claims and transformations. Taxes applied on settled transactions (such as financial transaction taxes) and ancillary settlement services are also reported under this category.
*`SHDT`-This category encompasses the reporting of fees related to the provision of services allowing intermediaries to send shareholders' data to issuers. This includes costs related to the provision of service for the calculation and settlement of fees applied by intermediaries to issuers for the notification of shareholders' data.
*`STEX`-This category encompasses the reporting of fees related to the provision of stock exchange services. This includes transaction fees.
*`TPCM`-This category encompasses the reporting of all fees related to the provision of services to collateral giver and/or collateral takers involved in a triparty collateral management transaction.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | ACMS |
| 2 | BICM |
| 3 | CALM |
| 4 | CLEA |
| 5 | CUST |
| 6 | INSV |
| 7 | INVS |
| 8 | ISSU |
| 9 | OTHR |
| 10 | PENM |
| 11 | REGI |
| 12 | SAFE |
| 13 | SECL |
| 14 | PENA |
| 15 | SETT |
| 16 | SHDT |
| 17 | STEX |
| 18 | TPCM |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
