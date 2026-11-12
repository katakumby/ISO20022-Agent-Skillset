---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDebtorAgentInstruction1Code"]
code_set: "ExternalDebtorAgentInstruction1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDebtorAgentInstruction1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDebtorAgentInstruction1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies further instructions concerning the processing of a payment instruction, as provided to the creditor agent.
*`HOLD`-Amount of money must be held for the (ultimate) creditor, who will call. Pay on identification.
*`CHQB`-(Ultimate) creditor must be paid by cheque.
*`PRTK`-Indicates that a payer token is requested/used.
*`PHOB`-Please advise/contact (ultimate) creditor/claimant by phone.
*`TELB`-Please advise/contact (ultimate) creditor/claimant by the most efficient means of telecommunication.
*`TOKN`-Token information.
*`VLTK`-Additional validation information to be used in conjunction with the token.

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
| 1 | HOLD |
| 2 | CHQB |
| 3 | PRTK |
| 4 | PHOB |
| 5 | TELB |
| 6 | TOKN |
| 7 | VLTK |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
