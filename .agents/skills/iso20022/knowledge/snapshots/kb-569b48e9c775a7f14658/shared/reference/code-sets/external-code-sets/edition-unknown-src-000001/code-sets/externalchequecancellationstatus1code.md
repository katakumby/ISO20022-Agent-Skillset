---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalChequeCancellationStatus1Code"]
code_set: "ExternalChequeCancellationStatus1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalChequeCancellationStatus1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalChequeCancellationStatus1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external cheque cancellation status code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code set published separately.
External code sets can be downloaded from www.iso20022.org.
*`RJCR`-Cheque cancellation request or request to stop the cheque is rejected.
*`ACCR`-Cheque cancellation request or request to stop the cheque is accepted.

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
| 1 | RJCR |
| 2 | ACCR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
