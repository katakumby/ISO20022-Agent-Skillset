---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalBalanceType1Code"]
code_set: "ExternalBalanceType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalBalanceType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalBalanceType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the balance type, as published in an external balance type code set.
External code sets can be downloaded from www.iso20022.org.
*`CLAV`-Closing balance of amount of money that is at the disposal of the account owner on the date specified.
*`CLBD`-Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening booked balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting period.
*`FWAV`-Forward available balance of money that is at the disposal of the account owner on the date specified.
*`INFO`-Balance for informational purposes.
*`ITAV`-Available balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified.
*`ITBD`-Balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified.
*`OPAV`-Opening balance of amount of money that is at the disposal of the account owner on the date specified.
*`OPBD`-Book balance of the account at the beginning of the account reporting period. It always equals the closing book balance from the previous report.
*`PRCD`-Balance of the account at the previously closed account reporting period. The opening booked balance for the new period has to be equal to this balance.
Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the date it references and equal the actual booked opening balance of the current date.
*`XPCD`-Balance, composed of booked entries and pending items known at the time of calculation, which projects the end of day balance if everything is booked on the account and no other entry is posted.

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
| 1 | CLAV |
| 2 | CLBD |
| 3 | FWAV |
| 4 | INFO |
| 5 | ITAV |
| 6 | ITBD |
| 7 | OPAV |
| 8 | OPBD |
| 9 | PRCD |
| 10 | XPCD |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
