---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPendingProcessingReason1Code"]
code_set: "ExternalPendingProcessingReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPendingProcessingReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPendingProcessingReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for pending status.
The list of valid codes is an external code list published separately. External code sets can be downloaded from www.iso20022.org.
*`ADEA`-Received after the servicer's deadline. Processed on best effort basis
*`DISA`-Exceptional closing of all financial institutions due to natural disaster, for example, earthquake
*`ESCA`-Special follow-up is taking place
*`IAAD`-Pending reason being investigated
*`LPRO`-Longer processing timeframe for this type of SSI
*`MINF`-Information, for example, currency is missing
*`NEWI`-Financial instrument is a new issue and not yet available/tradable
*`NEXT`-Next process is launched. No processing pending problems to be reported
*`NSTP`-Instruction was not straight through processing and had to be processed manually
*`PRSY`-Transaction was put on hold/frozen by the system

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
| 1 | ADEA |
| 2 | DISA |
| 3 | ESCA |
| 4 | IAAD |
| 5 | LPRO |
| 6 | MINF |
| 7 | NEWI |
| 8 | NEXT |
| 9 | NSTP |
| 10 | PRSY |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
