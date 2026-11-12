---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalContractBalanceType1Code"]
code_set: "ExternalContractBalanceType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalContractBalanceType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalContractBalanceType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies a contract balance type code, as published in the external ISO 20022 external code set.
External code sets can be downloaded from www.iso20022.org.
*`EXPC`-Revolver loan current utilisation (applicable on loan contracts types)
*`EXPT`-Total loan utilisation for loans with total loan limit  (applicable on loan contracts types)

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
| 1 | EXPC |
| 2 | EXPT |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
