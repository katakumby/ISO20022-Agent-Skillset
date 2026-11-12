---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPaymentControlRequestType1Code"]
code_set: "ExternalPaymentControlRequestType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPaymentControlRequestType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPaymentControlRequestType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external request type code for a payment control command in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code set published separately.
External code sets can be downloaded from www.iso20022.org.
*`RT01`-Type is a request to release the pending transactions.
*`RT02`-Type is a request to hold normal transactions.
*`RT03`-Type is a request to cancel a transaction.
*`RT04`-Type is a request to change the sequence of the transactions.
*`RT05`-Type is a request to release the suspicious transactions.

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
| 1 | RT01 |
| 2 | RT02 |
| 3 | RT03 |
| 4 | RT04 |
| 5 | RT05 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
