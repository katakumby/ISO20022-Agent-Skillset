---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalReservationType1Code"]
code_set: "ExternalReservationType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalReservationType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalReservationType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type of reservation, as published in an external reservation type code set.
External code sets can be downloaded from www.iso20022.org.
*`BLKD`-Amount blocked or frozen due to external circumstances such as a court order, death of beneficiary or account owner, or bankruptcy.
*`CARE`-Amount set aside by a participant to reserve liquidity from its own account, exclusively or executing cash withdrawals.
*`HPAR`-Amount set aside by a participant to reserve liquidity from its own account, exclusively for executing highly urgent payments.
*`NSSR`-Amount set aside by a participant to reserve liquidity from its own account, exclusively for the settlement of the multilateral cash balance stemming from the Net Security Settlement System.
*`THRE`-Amount above which funds will be destined for investment.
*`UPAR`-Amount set aside by a participant to reserve liquidity from its own account, exclusively for executing critical payments called urgent payments.

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
| 1 | BLKD |
| 2 | CARE |
| 3 | HPAR |
| 4 | NSSR |
| 5 | THRE |
| 6 | UPAR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
