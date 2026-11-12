---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCreditorReferenceType1Code"]
code_set: "ExternalCreditorReferenceType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCreditorReferenceType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCreditorReferenceType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of creditor reference as published in an external creditor reference type code set.
External code sets can be downloaded from www.iso20022.org.
*`DISP`-Document is a dispatch advice.
*`FXDR`-Document is a pre-agreed or pre-arranged foreign exchange transaction to which the payment transaction refers.
*`PUOR`-Document is a purchase order.
*`RPIN`-Document is a linked payment instruction to which the current payment instruction is related, for example, in a cover scenario.
*`RADM`-Document is a remittance advice sent separately from the current transaction.
*`SCOR`-Document is a structured communication reference provided by the creditor to identify the referred transaction.
*`PRNB`-Document is a payment reference number used to identify, match, or reconcile the referred contribution payment or related remittance information.

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
| 1 | DISP |
| 2 | FXDR |
| 3 | PUOR |
| 4 | RPIN |
| 5 | RADM |
| 6 | SCOR |
| 7 | PRNB |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
