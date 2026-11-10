---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalRePresentmentReason1Code"]
code_set: "ExternalRePresentmentReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalRePresentmentReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalRePresentmentReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external representment reason code in the format of character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
*`AMCR`-Amount corrected due to proof of transaction
*`CLSD`-Liability Shift to acquirer due to missing card authentication method denied
*`CRPI`-Credit previously issued
*`OTVA`-Original transaction was valid
*`VLSD`-Liability Shift to acquirer due to missing cardholder verification method denied

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
| 1 | AMCR |
| 2 | CLSD |
| 3 | CRPI |
| 4 | OTVA |
| 5 | VLSD |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
