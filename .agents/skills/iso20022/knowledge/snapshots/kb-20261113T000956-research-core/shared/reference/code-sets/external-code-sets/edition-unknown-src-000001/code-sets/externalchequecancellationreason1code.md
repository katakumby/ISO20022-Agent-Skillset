---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalChequeCancellationReason1Code"]
code_set: "ExternalChequeCancellationReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalChequeCancellationReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalChequeCancellationReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external cheque cancellation reason code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code set published separately.
External code sets can be downloaded from www.iso20022.org.
*`CUST`-Customer requested to stop/cancel the cheque.
*`LOST`-Cheque has been stolen/lost.
*`FRAD`-Cheque has been issued fraudulently.
*`DUPL`-Cheque has been issued in duplication of another cheque.
*`NARR`-Reason is provided as narrative information in the additional reason information.

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
| 1 | CUST |
| 2 | LOST |
| 3 | FRAD |
| 4 | DUPL |
| 5 | NARR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
