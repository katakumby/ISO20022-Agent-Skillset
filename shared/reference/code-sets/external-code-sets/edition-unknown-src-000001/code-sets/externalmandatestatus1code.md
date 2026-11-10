---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalMandateStatus1Code"]
code_set: "ExternalMandateStatus1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalMandateStatus1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalMandateStatus1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external mandate status code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`ACTV`-The mandate is active.
*`CANC`-The mandate is cancelled.
*`EXPI`-The mandate has passed the end date.
*`SUSP`-The mandate is put on hold.
*`RCVD`-The mandate data has been received by the related agent.
*`RJCT`-The mandate data has been rejected.
*`PATC`-The mandate initiation needs multiple authentications, where some but not yet all have been performed. Syntactical and semantical validations are successful.

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
| 1 | ACTV |
| 2 | CANC |
| 3 | EXPI |
| 4 | SUSP |
| 5 | RCVD |
| 6 | RJCT |
| 7 | PATC |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
