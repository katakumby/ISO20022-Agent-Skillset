---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDocumentPurpose1Code"]
code_set: "ExternalDocumentPurpose1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDocumentPurpose1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDocumentPurpose1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the document purpose as published in an external document purpose code list.
External code sets can be downloaded from www.iso20022.org.
*`CONF`-The document represents a document that has been confirmed, for example an invoice that has been confirmed by the buyer for payment.

*`FINV`-The document represents an invoice submitted under a factoring arrangment.

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
| 1 | CONF |
| 2 | FINV |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
