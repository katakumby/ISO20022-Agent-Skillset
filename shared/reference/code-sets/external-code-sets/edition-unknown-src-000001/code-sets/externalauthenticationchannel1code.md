---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalAuthenticationChannel1Code"]
code_set: "ExternalAuthenticationChannel1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalAuthenticationChannel1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalAuthenticationChannel1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the transaction authentication channel, as published in an external authentication channel code set.
External code sets can be downloaded from www.iso20022.org.
*`ATMA`-Authentication provided through ATM
*`CARD`-Authentication provided through Card
*`INBA`-Authentication provided through Internet Banking
*`MOBI`-Authentication provided through Mobile

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
| 1 | ATMA |
| 2 | CARD |
| 3 | INBA |
| 4 | MOBI |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
