---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalEntryStatus1Code"]
code_set: "ExternalEntryStatus1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalEntryStatus1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalEntryStatus1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the status of an entry on the books of the account servicer, as published in an external code set.
External code sets can be downloaded from www.iso20022.org.
*`BOOK`-Booked means that the transfer of money has been completed between account servicer and account owner.
Usage: Status Booked does not necessarily imply finality of money as this depends on other factors such as the payment system used, the completion of the end-to-end transaction and the terms agreed between account servicer and owner.
Status Booked is the only status that can be reversed.
*`FUTR`-Entry is on the books of the account servicer and value will be applied to the account owner at a future date and time.
*`INFO`-Entry is only provided for information, and no booking on the account owner's account in the account servicer's ledger has been performed.
*`PDNG`-Booking on the account owner's account in the account servicer's ledger has not been completed.
Usage: this can be used for expected items, or for items for which some conditions still need to be fulfilled before they can be booked. If booking takes place, the entry will be included with status Booked in subsequent account report or statement. Status Pending cannot be reversed.

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
| 1 | BOOK |
| 2 | FUTR |
| 3 | INFO |
| 4 | PDNG |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
