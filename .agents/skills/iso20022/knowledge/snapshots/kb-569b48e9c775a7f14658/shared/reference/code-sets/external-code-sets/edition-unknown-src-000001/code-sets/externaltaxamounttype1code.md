---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalTaxAmountType1Code"]
code_set: "ExternalTaxAmountType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalTaxAmountType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalTaxAmountType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the nature, or use, of the amount in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`CITY`-Tax accessed by city jurisdications within a country.
*`CNTY`-Tax accessed by county jurisdications within a country.
*`LOCL`-Tax accessed by local jurisdications within a country.
*`PROV`-Tax accessed by province jurisdications within a country.
*`STAT`-Tax accessed by state jurisdications within a country.

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
| 1 | CITY |
| 2 | CNTY |
| 3 | LOCL |
| 4 | PROV |
| 5 | STAT |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
