---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalAcceptedReason1Code"]
code_set: "ExternalAcceptedReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalAcceptedReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalAcceptedReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for an accepted status.

The list of valid codes is an external code list published separately. 
External code sets can be downloaded from www.iso20022.org.
*`ADEA`-Received after the servicer's deadline. Processed on best effort basis
*`NSTP`-Instruction was not straight through processing and had to be processed manually
*`SMPG`-Instruction is accepted but does not comply with the market practice rule published for the concerned market or process

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
| 1 | ADEA |
| 2 | NSTP |
| 3 | SMPG |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
