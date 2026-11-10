---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalReversalReason1Code"]
code_set: "ExternalReversalReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalReversalReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalReversalReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reversal reason, as published in an external reversal reason code list.
External code sets can be downloaded from www.iso20022.org.
*`AC03`-Wrong IBAN in  SCT
*`AC04`-Account number specified has been closed on the Receiver's books
*`AG02`-Bank Operation code specified in the message is not valid for receiver
*`AM05`-Duplication
*`AM09`-Wrong amount in SCT
*`MD01`-No Mandate
*`MD05`-Creditor or creditor's agent should not have collected the direct debit
*`MS02`-Reason has not been specified by end customer
*`MS03`-Reason has not been specified by agent.
*`RC07`-Wrong BIC in SCT
*`TM01`-Associated message was received after agreed processing cut-off time.

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
| 1 | AC03 |
| 2 | AC04 |
| 3 | AG02 |
| 4 | AM05 |
| 5 | AM09 |
| 6 | MD01 |
| 7 | MD05 |
| 8 | MS02 |
| 9 | MS03 |
| 10 | RC07 |
| 11 | TM01 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
