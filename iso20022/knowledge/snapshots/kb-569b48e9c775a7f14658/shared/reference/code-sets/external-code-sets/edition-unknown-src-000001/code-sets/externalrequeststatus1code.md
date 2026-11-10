---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalRequestStatus1Code"]
code_set: "ExternalRequestStatus1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalRequestStatus1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalRequestStatus1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the request status, as published in an external request status code set.
External code sets can be downloaded from www.iso20022.org.
*`RCVD`-Message has been received.
*`RJCT`-Message has been rejected.
*`ACPT`-Message has been accepted.
*`PDNG`-Message is pending further analysis and investigation.
*`PART`-Message has been partially accepted.

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
| 1 | RCVD |
| 2 | RJCT |
| 3 | ACPT |
| 4 | PDNG |
| 5 | PART |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
