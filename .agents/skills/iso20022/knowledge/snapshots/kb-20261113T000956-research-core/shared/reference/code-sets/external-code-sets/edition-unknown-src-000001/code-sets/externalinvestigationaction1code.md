---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationAction1Code"]
code_set: "ExternalInvestigationAction1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationAction1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationAction1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the requested action, as published in an external investigation action code set.
External code sets can be downloaded from www.iso20022.org.
*`RQCL`-Responder is requested to close the investigation. All investigation requests relating to the investigation may be disregarded.
*`RQST`-Responder is requested to provide the status of the investigation.
*`RQOB`-Responder is requested to review an earlier response as the requestor objects to it.
*`RQRO`-Responder is requested to reopen the investigation.

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
| 1 | RQCL |
| 2 | RQST |
| 3 | RQOB |
| 4 | RQRO |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
