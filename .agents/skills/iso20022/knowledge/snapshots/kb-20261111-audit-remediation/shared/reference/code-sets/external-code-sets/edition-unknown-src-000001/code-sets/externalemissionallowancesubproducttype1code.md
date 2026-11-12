---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalEmissionAllowanceSubProductType1Code"]
code_set: "ExternalEmissionAllowanceSubProductType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalEmissionAllowanceSubProductType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalEmissionAllowanceSubProductType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the detailed sub products types allowed for emission allowances and associated derivatives.
*`CERE`-Commodity attribute of type emissions allowance CER (Certified Emission Reduction).
*`EUAA`-Commodity attribute of type emissions allowance EUAA (European Union Aviation Allowance).
*`EUAE`-Commodity attribute of type emissions allowance EUA (European Union Allowance).
*`ERUE`-Commodity attribute of type emissions allowance ERU (European Reduction Unit).
*`OTHR`-Commodity attribute of other type.

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
| 1 | CERE |
| 2 | EUAA |
| 3 | EUAE |
| 4 | ERUE |
| 5 | OTHR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
