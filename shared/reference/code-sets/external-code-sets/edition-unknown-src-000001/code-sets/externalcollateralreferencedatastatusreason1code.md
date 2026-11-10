---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCollateralReferenceDataStatusReason1Code"]
code_set: "ExternalCollateralReferenceDataStatusReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCollateralReferenceDataStatusReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCollateralReferenceDataStatusReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the status reason, as published in an external collateral reference data status reason code list.
External code sets can be downloaded from www.iso20022.org.
*`MFNS`-All fields in message format are not supported.
*`ESPN`-Eligibility set profile not found.
*`EXTN`-Extension not allowed as there is no end date for original instruction.
*`INDX`-Index does not exist.
*`IPNS`-Input parameters not supported (when the instruction comes at  thet transaction level).
*`COMB`-Instructing party/counterparty combination is not configured for the instruction type.
*`NCFG`-Instructing party not configured for the instruction type.
*`LIST`-List identification does not exist for the instructing party.
*`NRGN`-Original instruction not found.
*`OIEX`-Original instruction already expired.
*`RMVL`-Does not support this removal type.
*`SIDN`-Security identification is not supported.
*`SITN`-Security identification type not supported.
*`SDNM`-Start date of original instruction does not match.
*`SYST`-System error.

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
| 1 | MFNS |
| 2 | ESPN |
| 3 | EXTN |
| 4 | INDX |
| 5 | IPNS |
| 6 | COMB |
| 7 | NCFG |
| 8 | LIST |
| 9 | NRGN |
| 10 | OIEX |
| 11 | RMVL |
| 12 | SIDN |
| 13 | SITN |
| 14 | SDNM |
| 15 | SYST |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
