---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalBalanceSubType1Code"]
code_set: "ExternalBalanceSubType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalBalanceSubType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalBalanceSubType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the balance sub-type, as published in an external balance sub-type code list.
External code sets can be downloaded from www.iso20022.org.
*`ADJT`-Balance to be held in the settlement account in order to comply with the average reserve due, in the event that the bank's balance is equal to the reserve due during the remaining days of the maintenance period.
*`BCUR`-Balance representing the amount in the domestic or base accounting currency.
*`BLCK`-Balance representing the regulatory reserve that a financial institution must have with the account servicing institution, eg, the minimum credit balance a financial institution is to keep with its Central Bank for mandatory reserve purposes. In some countries, a blocked balance is known as a 'reserve' balance.
*`BLKD`-Balance representing funds that cannot be touched by the account owner.
*`DLOD`-Balance representing the intra day overdraft granted by the Central Bank to financial institutions participating in a RTGS system. This balance may vary over time and shall be offset at the end of the day.
*`EAST`-Balance representing the potential loan a Central Bank would make in cash if the collateral is pledged, eg, securities available and eligible as collateral with the Central Bank.
*`FCOL`-Balance representing the forecast of the cash-equivalent resulting from evaluation of existing holdings at CSD that are qualified to serve as collateral.
*`FCOU`-Balance representing the cash equivalent resulting from evaluation of existing holdings at CSD that are qualified to serve as collateral and have been used as collateral.
*`FORC`-Balance representing the total of all balance types representing the forecast of transactions to settle, blocked items, custody transactions and corporate actions cash disbursements.
*`FUND`-Balance representing the net amount to be funded resulting from the difference between the total of all transactions with a cash impact and the existing cash coverage.
*`INTM`-Balance representing an intermediate amount such as the opening or closing balance incrementally carried forward from one page to the next in a multi-page statement or report.
*`LCUR`-Balance representing the amount in the local market currency for which the asset is held.
*`LRLD`-Balance of a specific limit value, eg, a bilateral balance is calculated in relation to a given bilateral limit.
*`NOTE`-Balance representing the amount that a financial institution has set aside for a specific reason and which is therefore not available. In the context of CSDs, reservation of liquidity made to meet settlement obligations.
*`PDNG`-Balance of securities pending delivery, such as orders to sell securities have been executed but settlement of the open transactions has not been confirmed.
*`PIPO`-Balance representing the fictive amount of automated direct debits or payment based on standing arrangements between the CSD and the user. Usage: Pay-Ins and Pay-Outs can be different based on individual payment instructions or available funds.
*`PRAV`-Average of the daily balances on the account used to fulfil the reserve requirements calculated from the beginning of the maintenance period.
*`RESV`-Balance representing the regulatory reserve that a financial institution must have with the account servicing institution, eg, the minimum credit balance a financial institution is to keep with its Central Bank for mandatory reserve purposes.
*`SCOL`-Balance representing the forecast of the cash-equivalent resulting from evaluation of the net incoming balance of securities qualified to serve as collateral for which settlement instructions are held at.
*`SCOU`-Balance representing the cash-equivalent resulting from evaluation of incoming securities, qualified to serve as collateral and actually used as collateral, which have been settled during the settlement process.
*`THRE`-Balance representing the amount that will be destined for investment. Difference between available balance and threshold for investment limit.
*`UNBL`-Balance representing funds that can be touched by the account owner.

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
| 1 | ADJT |
| 2 | BCUR |
| 3 | BLCK |
| 4 | BLKD |
| 5 | DLOD |
| 6 | EAST |
| 7 | FCOL |
| 8 | FCOU |
| 9 | FORC |
| 10 | FUND |
| 11 | INTM |
| 12 | LCUR |
| 13 | LRLD |
| 14 | NOTE |
| 15 | PDNG |
| 16 | PIPO |
| 17 | PRAV |
| 18 | RESV |
| 19 | SCOL |
| 20 | SCOU |
| 21 | THRE |
| 22 | UNBL |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
