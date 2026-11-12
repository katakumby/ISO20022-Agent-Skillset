---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalModelFormIdentification1Code"]
code_set: "ExternalModelFormIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalModelFormIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalModelFormIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external model form identification code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.

*`ISP1`-ISP98 model form for standby incorporating annexed form of payment demand with statement.
*`ISP2`-ISP98 model form or standby providing for extension and incorporating annexed form of payment demand with alternative non-extension statement.
*`ISP3`-ISP98 model form or standby providing for reduction and incorporating annexed form of reduction demand.
*`ISP4`-ISP98 model form for standby providing for transfer and incorporating annexed form of transfer demand.
*`ISP5`-ISP98 model form for simplified demand only standby.
*`ISP6`-ISP98 model form for counter standby with annexed form of local bank undertaking.
*`ISP7`-ISP98 model form for standby requiring confirmation.
*`ISP8`-ISP98 model form for confirmation of standby.
*`UDG1`-Model form for demand guarantee defined in the latest version of the ICC Uniform Rules For Demand Guarantees (URDG).
*`UDG2`-Model form for counter-guarantee defined in the latest version of the ICC Uniform Rules For Demand Guarantees (URDG).

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
| 1 | ISP1 |
| 2 | ISP2 |
| 3 | ISP3 |
| 4 | ISP4 |
| 5 | ISP5 |
| 6 | ISP6 |
| 7 | ISP7 |
| 8 | ISP8 |
| 9 | UDG1 |
| 10 | UDG2 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
