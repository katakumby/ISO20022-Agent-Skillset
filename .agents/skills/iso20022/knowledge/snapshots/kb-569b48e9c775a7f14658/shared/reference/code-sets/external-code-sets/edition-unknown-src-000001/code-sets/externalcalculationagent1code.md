---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCalculationAgent1Code"]
code_set: "ExternalCalculationAgent1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCalculationAgent1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCalculationAgent1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the calculation agent, as published in an external calculation agent code list.
External code sets can be downloaded from www.iso20022.org.
*`ISDA`-As defined in the ISDA Master Agreement.
*`JOIN`-Trading side and counterparty side will jointly act.
*`TRAD`-Trading side will act.
*`CNTP`-Counterparty side will act.

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
| 1 | ISDA |
| 2 | JOIN |
| 3 | TRAD |
| 4 | CNTP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
