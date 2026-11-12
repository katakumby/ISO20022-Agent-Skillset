---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalEnquiryRequestType1Code"]
code_set: "ExternalEnquiryRequestType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalEnquiryRequestType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalEnquiryRequestType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external request type code for the enquiry on a position in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code set published separately.
External code sets can be downloaded from www.iso20022.org.
*`RT11`-Type is an enquiry on the bank's position.
*`RT12`-Type is an enquiry on a specific transaction.
*`RT13`-Type is an enquiry on a queued transaction.
*`RT14`-Type is an enquiry on a suspicious transaction.
*`RT16`-Type is an enquiry on the system date and/or time.
*`RT15`-Type is an enquiry on pending inward credits.

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
| 1 | RT11 |
| 2 | RT12 |
| 3 | RT13 |
| 4 | RT14 |
| 5 | RT16 |
| 6 | RT15 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
