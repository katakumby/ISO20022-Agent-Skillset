---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalUnderlyingTradeTransactionType1Code"]
code_set: "ExternalUnderlyingTradeTransactionType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalUnderlyingTradeTransactionType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalUnderlyingTradeTransactionType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external commercial reference type code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`CONT`-Underlying transaction is a contract.
*`DELV`-Underlying transaction is a delivery order.
*`PROF`-Underlying transaction is a proforma invoice.
*`PROJ`-Underlying transaction is a project.
*`PUOR`-Underlying transaction is a purchase order.
*`QUOT`-Underlying transaction is a quotation.
*`TEND`-Underlying transaction is a tender.

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
| 1 | CONT |
| 2 | DELV |
| 3 | PROF |
| 4 | PROJ |
| 5 | PUOR |
| 6 | QUOT |
| 7 | TEND |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
