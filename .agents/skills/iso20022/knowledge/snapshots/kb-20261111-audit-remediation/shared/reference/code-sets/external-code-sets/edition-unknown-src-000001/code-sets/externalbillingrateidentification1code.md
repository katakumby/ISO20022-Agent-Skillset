---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalBillingRateIdentification1Code"]
code_set: "ExternalBillingRateIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalBillingRateIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalBillingRateIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of billing rate or factor, as published in an external billing rate identification code list.
External code sets can be downloaded from www.iso20022.org.
*`AEAR`-Per annum earnings rate, adjusted for reserves, applied to the current analysis period’s investable balance for calculation of the earnings allowance credit.  The ECR, Net of Reserves, is calculated as:    ECR, Net of Reserves  =  ECR, Not Net (00 01 22) * (1 – Reserve Rate)
*`ANXE`-The anticpated earnings allowance rate, as adjusted, to be used next month in the calculation of the earnings allowance. See AEAR AdjustedEarningsAllowance Rate
*`CDRA`-The current CD (Certificate of Deposit) rate as published by the bank.
*`DINR`-The per annum rate used to calculate the Deficiency Interest amount to be paid to the bank.
*`DSCR`-The per annum rate used to calculate a surcharge based on the Deficiency Interest amount to be paid to the bank.
*`EALR`-Per annum earnings rate applied to the current statement period’s investable balance for calculation of the earnings allowance credit. The earnings allowance credit is used to offset the charges for balance compensable services. This rate has NOT been adjusted for reserves. The ECR, Not Net of Reserves, is calculated as:    ECR, Not Net  =  ECR, Net of Reserves (00 01 20)  /  (1 – Reserve Rate)
*`FDIC`-The current FDIC rate used in the US to calculate the Federal Deposit Insurance premium paid by the banks to the FDIC.
*`ICDR`-Per annum interest rate used to calculate the interest amount credited to a designated account. The amount of interest credited, if any, is reported in a Compensation Section with a Compensation Identifier of TtlInterestCredited
*`MULT`-The collected balance required to offset $1.00 of balance compensable service charges.  This factor can be used to calculate the balance equivalent of balance compensable service charges.  The multiplier is calculated in one of three different ways depending on whether the Earnings Allowance Rate (ECR) is adjusted for reserves or not (net of reserves or not)  and, in the case where the ECR is not adjusted for reserves, whether the multiplier is adjusted for reserves or not.
*`NCBO`-Per annum interest rate used to calculate overdraft compensation on an average net collected balance which is negative (AFP balance 00 00 10).  An average NET balance is negative when the sum of the daily ending POSITIVE and NEGATIVE balances is negative.
*`NGCO`-Per annum interest rate applied to NEGATIVE collected balances (AFP balance 00 00 13) for calculation of overdraft compensation.
*`NGLO`-Per annum interest rate applied to NEGATIVE ledger balances (AFP balance 00 00 03) for calculation of overdraft compensation.
*`NLBO`-Per annum interest rate used to calculate overdraft compensation on an average net ledger balance which is negative (AFP balance 00 00 00).  An average NET balance is negative when the sum of the daily ending POSITIVE and NEGATIVE balances is negative.
*`NXME`-The anticpated earnings allowance rate to be used next month in the calculation of the earnings allowance. See EALR EarningsAllowance Rate
*`NXMU`-The anticipated Multiplier to be used next month. See MULT Multiplier.
*`PRIR`-The current per annum Prime rate as published by the bank.
*`RRQR`-The per annum reserve rate as applied to non demand deposit accounts such as time deposit or CD accounts.
*`RSRV`-Per annum interest rate used to calculate that portion of the CollectedBal-AvgPositive that US banks must keep on deposit at the US Federal Reserve.
*`UFUR`-Per annum interest rate assessed on that portion of the account balance which is the difference between the average negative ledger and the average negative collected balance (AFP balance 00 00 15).  This rate is used to assess compensation on the portion of the negative collected balance that represents the use of uncollected funds.

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
| 1 | AEAR |
| 2 | ANXE |
| 3 | CDRA |
| 4 | DINR |
| 5 | DSCR |
| 6 | EALR |
| 7 | FDIC |
| 8 | ICDR |
| 9 | MULT |
| 10 | NCBO |
| 11 | NGCO |
| 12 | NGLO |
| 13 | NLBO |
| 14 | NXME |
| 15 | NXMU |
| 16 | PRIR |
| 17 | RRQR |
| 18 | RSRV |
| 19 | UFUR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
