---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalReportingSource1Code"]
code_set: "ExternalReportingSource1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalReportingSource1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalReportingSource1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reporting source, as published in an external reporting source code list.
External code sets can be downloaded from www.iso20022.org.
*`ACCT`-Statement or Report is based on accounting data.
*`ARPF`-An account reconciliation system that provides full reconciliation that usually addresses checks
*`ARPP`-An account reconciliation system that provides partial reconciliation that usually addresses checks
*`CTDB`-A sub-application that reports presentment totals
*`CUST`-Statement or Report is based on custody data.
*`DEPT`-Cash or deposit accounting system
*`DPCS`-Deposit system that reports what has been collected from various financial institutions
*`LKBX`-Processing system that captures and reports check data in a lockbox environment.
*`RCPT`-A system that reports consolidated remittance information obtained from various , i.e., ACH, wires, lockbox, etc.
*`MIBO`-Transaction submitted directly from PMI (Payment Market Infrastructure back-office system).
*`PFRE`-Transactions submitted directly from participant / PSO (Payment System Operator) applications.

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
| 1 | ACCT |
| 2 | ARPF |
| 3 | ARPP |
| 4 | CTDB |
| 5 | CUST |
| 6 | DEPT |
| 7 | DPCS |
| 8 | LKBX |
| 9 | RCPT |
| 10 | MIBO |
| 11 | PFRE |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
