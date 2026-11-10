---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalGarnishmentType1Code"]
code_set: "ExternalGarnishmentType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalGarnishmentType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalGarnishmentType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the garnishment type as published in an external document type code list.
*`GNCS`-Garnishment from a third party payer for Child Support
*`GNDP`-Garnishment from a direct payer for Child Support
*`GTPP`-Garnishment from a third party payer to taxing agency

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
| 1 | GNCS |
| 2 | GNDP |
| 3 | GTPP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
