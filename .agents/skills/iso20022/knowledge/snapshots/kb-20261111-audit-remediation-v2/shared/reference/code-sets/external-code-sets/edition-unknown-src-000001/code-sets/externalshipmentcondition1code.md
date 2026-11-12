---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalShipmentCondition1Code"]
code_set: "ExternalShipmentCondition1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalShipmentCondition1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalShipmentCondition1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies a shipment conditions code, as published in the external ISO 20022 external code set.
External code sets can be downloaded from www.iso20022.org.
*`ADVN`-Goods/service delivered after payment
*`PMNT`-Goods/service delivered at the same time as payment.
*`TRLN`-Goods/service delivered before payment

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
| 1 | ADVN |
| 2 | PMNT |
| 3 | TRLN |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
