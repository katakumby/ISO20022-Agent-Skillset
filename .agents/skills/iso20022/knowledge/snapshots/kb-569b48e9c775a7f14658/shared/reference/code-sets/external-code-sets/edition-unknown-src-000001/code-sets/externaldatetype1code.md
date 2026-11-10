---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDateType1Code"]
code_set: "ExternalDateType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDateType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDateType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Defines the type of date, as published in an external date type code list.
External code sets can be downloaded from www.iso20022.org.
*`INDA`-Relates to the invoice date.
*`PADD`-Relates to the payment due date.
*`NXBD`-Relates to the next billing date.
*`NTAV`-Date type is not available.
*`PYDT`-Relates to the payroll date.

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
| 1 | INDA |
| 2 | PADD |
| 3 | NXBD |
| 4 | NTAV |
| 5 | PYDT |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
