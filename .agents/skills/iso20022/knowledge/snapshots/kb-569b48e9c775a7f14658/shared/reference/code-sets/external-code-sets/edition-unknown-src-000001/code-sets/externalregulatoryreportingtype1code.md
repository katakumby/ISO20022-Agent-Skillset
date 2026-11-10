---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalRegulatoryReportingType1Code"]
code_set: "ExternalRegulatoryReportingType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalRegulatoryReportingType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalRegulatoryReportingType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of regulatory reporting, as published in an external code set.
External code sets can be downloaded from www.iso20022.org.
*`DECL`-The transaction includes a declaration confirming compliance with applicable regulatory and sanctions requirements (e.g., FEFTA, OFAC, or other relevant frameworks). This type code refers to information in any element under the same occurrence of “RgltryRptg/Dtls”.
*`CIST`-Regulatory Authority requires the status of residency of an involved party, e.g. if it is a resident or non-resident. This type code may refer to information in any element under the same occurrence of “RgltryRptg/Dtls”.
*`CRST`-Regulatory Authority requires the status or type of Creditor, e.g. if it is a corporation, an individual or the government. This type code may refer to information in any element under the same occurrence of “RgltryRptg/Dtls”.
*`TAXS`-Regulatory Authority requires a tax information, e.g. an tax identification reference. This type code may refer to information in any element under the same occurrence of “RgltryRptg/Dtls”.
*`PURP`-Regulatory Authority requires or recommends a code or narrative text to identify the purpose of payment in line with the specific requirements of that authority. This type code may refer to information in any element under the same occurrence of “RgltryRptg/Dtls”.

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
| 1 | DECL |
| 2 | CIST |
| 3 | CRST |
| 4 | TAXS |
| 5 | PURP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
