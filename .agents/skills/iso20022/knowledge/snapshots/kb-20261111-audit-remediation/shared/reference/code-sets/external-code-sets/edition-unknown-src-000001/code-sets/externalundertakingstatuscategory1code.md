---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalUndertakingStatusCategory1Code"]
code_set: "ExternalUndertakingStatusCategory1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalUndertakingStatusCategory1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalUndertakingStatusCategory1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external status stage code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`AMND`-Status is related to an undertaking amendment.
*`AMTC`-Status is related to a counter-undertaking amount.
*`AMTU`-Status is related to an undertaking amount.
*`APPL`-Status is related to an undertaking application.
*`BAMD`-Status is related to an undertaking amendment requested by the beneficiary.
*`CONF`-Status is related to an undertaking confirmation.
*`DEMD`-Status is related to an undertaking demand.
*`NEXT`-Status is related to an undertaking non-extension request.
*`TERM`-Status is related to an undertaking termination.

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
| 1 | AMND |
| 2 | AMTC |
| 3 | AMTU |
| 4 | APPL |
| 5 | BAMD |
| 6 | CONF |
| 7 | DEMD |
| 8 | NEXT |
| 9 | TERM |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
