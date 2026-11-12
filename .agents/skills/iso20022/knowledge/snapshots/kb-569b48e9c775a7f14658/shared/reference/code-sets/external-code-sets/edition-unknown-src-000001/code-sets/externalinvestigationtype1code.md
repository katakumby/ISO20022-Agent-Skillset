---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationType1Code"]
code_set: "ExternalInvestigationType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the investigation type, as published in an external investigation type code set.
External code sets can be downloaded from www.iso20022.org.
*`UTAP`-A booked entry cannot be applied by the creditor.
*`CCNR`-Creditor claims non-receipt of payment.
*`CONR`-Creditor agent claims non-receipt of cover or settlement.
*`RQFI`-Further information is required on a payment, entry, message or instruction.
*`PINC`-Payment initiation has not been settled or confirmed.
*`RQVA`-Revaluation of an entry is requested.
*`RQUF`-Use of funds on an entry is requested.
*`RQDA`-Debit authorisation on an entry is requested.
*`ACCT`-Investigation relating to an account.
*`RQCH`-Investigation relating to charges that have been taken or are requested.
*`RIMF`-Request from International Monetary Fund.
*`OTHR`-Other request type.

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
| 1 | UTAP |
| 2 | CCNR |
| 3 | CONR |
| 4 | RQFI |
| 5 | PINC |
| 6 | RQVA |
| 7 | RQUF |
| 8 | RQDA |
| 9 | ACCT |
| 10 | RQCH |
| 11 | RIMF |
| 12 | OTHR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
