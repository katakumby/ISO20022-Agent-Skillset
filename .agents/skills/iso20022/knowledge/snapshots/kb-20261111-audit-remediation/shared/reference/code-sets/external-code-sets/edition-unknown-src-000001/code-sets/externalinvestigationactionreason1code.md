---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationActionReason1Code"]
code_set: "ExternalInvestigationActionReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationActionReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationActionReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the requested action, as published in an external investigation action code set.
External code sets can be downloaded from www.iso20022.org.
*`IRSI`-Closure is requested as the investigation request was sent in error.
*`IRRR`-Closure is requested as the investigation request has been resolved by requestor.
*`IRCD`-Objection is raised as the compensation amount quoted on the investigation response appears incorrect.
*`IRIC`-Objection is raised as the data provided on the investigation response is insufficent to address the original request.
*`NARR`-See AdditionalInformation element for action reason.

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
| 1 | IRSI |
| 2 | IRRR |
| 3 | IRCD |
| 4 | IRIC |
| 5 | NARR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
