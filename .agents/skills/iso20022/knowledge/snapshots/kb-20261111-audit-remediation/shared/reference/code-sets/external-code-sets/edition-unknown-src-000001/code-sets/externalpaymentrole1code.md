---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPaymentRole1Code"]
code_set: "ExternalPaymentRole1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPaymentRole1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPaymentRole1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the role associated with a specific party in a payment instruction, as published in an external payment role code set.
External code sets can be downloaded from www.iso20022.org.
*`BKMG`-Party responsible for managing the recovery functions related to a system.
*`LMMG`-Party in a financial institution responsible for the management of the limits. This party is responsible for fixing, modifying, or suspending limits as relevant for the management of counterpart risk or systemic risk containment.
*`LQMG`-Party in a financial institution responsible for the management of liquidity for the financial institution. This party has access to some functions available on the system, such as the liquidity transfers or management of standing instructions for liquidity control.
*`PYMG`-Party in a financial institution responsible for the management of payment processing for the financial institution. This includes authorising, recycling, and modification of payment transactions.
*`REDR`-Party in a financial institution entitled to obtain information from the system, but not act upon/alter this information.
*`STMG`-Party in a financial institution responsible for the management of settlement processing.

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
| 1 | BKMG |
| 2 | LMMG |
| 3 | LQMG |
| 4 | PYMG |
| 5 | REDR |
| 6 | STMG |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
