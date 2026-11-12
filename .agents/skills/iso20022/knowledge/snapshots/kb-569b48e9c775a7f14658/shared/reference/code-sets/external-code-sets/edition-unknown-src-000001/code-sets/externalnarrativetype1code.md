---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalNarrativeType1Code"]
code_set: "ExternalNarrativeType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalNarrativeType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalNarrativeType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external narrative type code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`ADDI`-Narrative text describing the additional terms and conditions.
*`CHAR`-Narrative text describing the charge details.
*`DRAW`-Narrative text describing the drawing details.
*`PRAS`-Narrative text describing the assignment of proceeds terms and conditions.
*`TEFF`-Narrative text describing the terms of effectiveness.
*`TRNF`-Narrative text describing the transfer terms and conditions.
*`TVAR`-Narrative text describing the terms of variation.

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
| 1 | ADDI |
| 2 | CHAR |
| 3 | DRAW |
| 4 | PRAS |
| 5 | TEFF |
| 6 | TRNF |
| 7 | TVAR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
