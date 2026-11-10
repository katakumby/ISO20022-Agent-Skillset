---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalMessageFunction1Code"]
code_set: "ExternalMessageFunction1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalMessageFunction1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalMessageFunction1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Code to identify the type of process related to the message, as published separately in a message function external code set.

External code sets can be downloaded from www.iso20022.org.
*`REQU`-Message function is request.
*`ADVC`-Advice indicates where the sender informs the receiver of an activity that has been taken that requires a response.
*`NOTI`-Message function is notification.
*`CAAD`-Advice about the capture of an activity already performed (response expected).
*`CANO`-Notification about the capture of an activity already performed (no response expected).
*`BNTF`-Notification to initiate the transfer of a batch (no response expected).
*`BTRQ`-Request to initiate the transfer of a batch (response expected).
*`CLNF`-Notification to initiate the transfer of a collection (no response expected).
*`CLRQ`-Request to initiate the transfer of a collection (response expected).
*`STAD`-Advice about the status of a transaction.
*`STNO`-Notification about the status of a transaction.
*`ERNO`-Notification of a message containing errors.
*`RENO`-Notification of a rejected message.
*`INSN`-Informs of an action to be taken.

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
| 1 | REQU |
| 2 | ADVC |
| 3 | NOTI |
| 4 | CAAD |
| 5 | CANO |
| 6 | BNTF |
| 7 | BTRQ |
| 8 | CLNF |
| 9 | CLRQ |
| 10 | STAD |
| 11 | STNO |
| 12 | ERNO |
| 13 | RENO |
| 14 | INSN |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
