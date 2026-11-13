---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalTransactorType1Code"]
code_set: "ExternalTransactorType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalTransactorType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalTransactorType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies a code to identify the transactor type. 

External code sets can be downloaded from www.iso20022.org.
*`DWTP`-Entity that offers a digital wallet solution enabling users to store payment instruments and initiate transactions electronically.
*`GATW`-Service provider that acts as an intermediary between merchants and payment networks, securely transmitting transaction data.
*`IDSO`-Third-party entity that partners with acquiring banks to provide merchant services, recruit merchants, and manage relationships.
*`MKTP`-Platform that connects buyers and sellers, facilitating transactions and often handling payment processing and settlement.
*`PMFT`-Entity that enables sub-merchants to accept electronic payments without requiring each sub-merchant to have a direct merchant account.
*`RMPP`-Service that enables conversion between fiat currency and digital assets, facilitating on-ramps and off-ramps.
*`SDWP`-Provider of a wallet solution where the funding source and transaction execution are separated into stages.
*`UPTA`-Entity that consolidates bill payments for utilities and provides a single interface for consumers or businesses to pay multiple service providers.

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
| 1 | DWTP |
| 2 | GATW |
| 3 | IDSO |
| 4 | MKTP |
| 5 | PMFT |
| 6 | RMPP |
| 7 | SDWP |
| 8 | UPTA |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
