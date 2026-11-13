---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPostTradeEventType1Code"]
code_set: "ExternalPostTradeEventType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPostTradeEventType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPostTradeEventType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of post trade event, as published in an external post trade event type code set.
External code sets can be downloaded from www.iso20022.org.
*`EAMT`-Trade will be settled early.
*`PEAM`-Trade will be partially settled early.
*`PRUR`-Part of the trade will be settled on its original date and the remainder will rollover.
*`PRUW`-Part of the trade will not be settled.
*`ROLL`-Rollover of a previous trade.
*`UNWD`-Trade will not be settled.
*`UNWR`-Original trade will not settle on its original date, but will be rolled over.

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
| 1 | EAMT |
| 2 | PEAM |
| 3 | PRUR |
| 4 | PRUW |
| 5 | ROLL |
| 6 | UNWD |
| 7 | UNWR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
