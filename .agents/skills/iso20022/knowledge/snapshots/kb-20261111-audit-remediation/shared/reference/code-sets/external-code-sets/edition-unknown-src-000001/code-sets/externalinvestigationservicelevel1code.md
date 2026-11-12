---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationServiceLevel1Code"]
code_set: "ExternalInvestigationServiceLevel1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationServiceLevel1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationServiceLevel1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the investigation service level, as published in an external investigation service level code set.
External code sets can be downloaded from www.iso20022.org.
*`R01D`-Response expected within one business day.
*`R03D`-Response expected within three business days.
*`R05D`-Response expected within five business days.
*`R10D`-Response expected within ten business days.
*`R15D`-Response expected within fifteen business days.

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
| 1 | R01D |
| 2 | R03D |
| 3 | R05D |
| 4 | R10D |
| 5 | R15D |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
