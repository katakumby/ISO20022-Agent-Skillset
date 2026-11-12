---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalProductType1Code"]
code_set: "ExternalProductType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalProductType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalProductType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of asset class a non-equity financial instrument can be classified as.
*`COMM`-Identifies categories of instruments that are commodities.
*`CURR`-Identifies categories of currency instruments.
*`EQUI`-Identifies categories of instruments related to an equity.
*`INTR`-Identifies categories of instruments that are interest rates based.
*`CRDT`-Identifies categories of instruments that are credits.
*`EMAL`-Identifies categories of instruments related to emission allowance.
*`OCTN`-Identifies categories of instruments classified as other C10.

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
| 1 | COMM |
| 2 | CURR |
| 3 | EQUI |
| 4 | INTR |
| 5 | CRDT |
| 6 | EMAL |
| 7 | OCTN |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
