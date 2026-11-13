---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalValidationRuleIdentification1Code"]
code_set: "ExternalValidationRuleIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalValidationRuleIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalValidationRuleIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external validation rule identification scheme name code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`CCTR`-Identifies the validation rules related to the Russian Cross-border Transactions Currency Control Reporting.
*`ITRP`-Identifies the validation rules related to the invoice tax reporting.
*`MMSR`-Identifies the validation rule scheme related to the ECB Euro Money Market Statistical Reporting.
*`SMMD`-Identifies the validation rules related to the Bank Of England Sterling Money Market Daily Reporting.

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
| 1 | CCTR |
| 2 | ITRP |
| 3 | MMSR |
| 4 | SMMD |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
