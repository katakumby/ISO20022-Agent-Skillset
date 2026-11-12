---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalClaimNonReceiptRejection1Code"]
code_set: "ExternalClaimNonReceiptRejection1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalClaimNonReceiptRejection1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalClaimNonReceiptRejection1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for the rejection of a claim non receipt, as published in an external claim non receipt rejection code set.
External code sets can be downloaded from www.iso20022.org.
*`NOOR`-Original credit transfer never received.
*`RNPR`-Original credit transfer was received but is not processable.
*`ARJT`-Already rejected original SCT (SEPA Credit Transfer).
*`ARDT`-Already returned original SCT (SEPA Credit Transfer).
*`RR04`-Regulatory reason.

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
| 1 | NOOR |
| 2 | RNPR |
| 3 | ARJT |
| 4 | ARDT |
| 5 | RR04 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
