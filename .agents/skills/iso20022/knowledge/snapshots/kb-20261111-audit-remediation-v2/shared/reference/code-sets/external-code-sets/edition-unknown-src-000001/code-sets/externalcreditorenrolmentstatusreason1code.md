---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCreditorEnrolmentStatusReason1Code"]
code_set: "ExternalCreditorEnrolmentStatusReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCreditorEnrolmentStatusReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCreditorEnrolmentStatusReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the  creditor enrolment status reason code, as published in an external  creditor enrolment status reason code set.
External code sets can be downloaded from www.iso20022.org.
*`ACRD`-Already existing creditor.
*`AM05`-Duplication.
*`FF01`-Invalid file format.
*`RF01`-Reference is not unique.
*`RR04`-Regulatory Reason.
*`RR10`-Invalid character set.
*`TRJT`-Technical rejection.

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
| 1 | ACRD |
| 2 | AM05 |
| 3 | FF01 |
| 4 | RF01 |
| 5 | RR04 |
| 6 | RR10 |
| 7 | TRJT |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
