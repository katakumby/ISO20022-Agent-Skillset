---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDebtorActivationAmendmentReason1Code"]
code_set: "ExternalDebtorActivationAmendmentReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDebtorActivationAmendmentReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDebtorActivationAmendmentReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the debtor activation amendment reason code, as published in an external debtor activation amendment reason code set.
External code sets can be downloaded from www.iso20022.org.
*`AM05`-Duplication.
*`RF01`-Reference is not unique.
*`RR04`-Regulatory Reason.
*`TRJT`-Technical rejection.
*`UCRD`-Unknown creditor.
*`CUST`-Amendment requested by the customer.

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
| 1 | AM05 |
| 2 | RF01 |
| 3 | RR04 |
| 4 | TRJT |
| 5 | UCRD |
| 6 | CUST |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
