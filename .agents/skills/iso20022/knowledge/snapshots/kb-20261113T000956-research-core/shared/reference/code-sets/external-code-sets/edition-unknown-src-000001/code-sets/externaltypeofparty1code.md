---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalTypeOfParty1Code"]
code_set: "ExternalTypeOfParty1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalTypeOfParty1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalTypeOfParty1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external type of party code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`ADVP`-Party advising the undertaking.
*`ANYB`-Any bank.
*`APPL`-Party named in the undertaking as the “applicant”.
*`BENE`-Party in whose favour the undertaking (or counter-undertaking) is issued.
*`CONF`-Party that adds its undertaking to honour the undertaking.
*`CUB2`-Beneficiary of the second counter-undertaking.
*`CUB3`-Beneficiary of the third counter-undertaking.
*`ISSU`-Party that issues the undertaking (or counter-undertaking).
*`OBLG`-Party obligated to reimburse the issuer.
*`ORDR`-Party requested to issue an undertaking on behalf of the applicant. Also known as the ordering institution or applicant's bank.
*`PRES`-Party nominated to receive presentation.
*`SADV`-Second advising party.
*`SPEC`-Party located at specified address.

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
| 1 | ADVP |
| 2 | ANYB |
| 3 | APPL |
| 4 | BENE |
| 5 | CONF |
| 6 | CUB2 |
| 7 | CUB3 |
| 8 | ISSU |
| 9 | OBLG |
| 10 | ORDR |
| 11 | PRES |
| 12 | SADV |
| 13 | SPEC |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
