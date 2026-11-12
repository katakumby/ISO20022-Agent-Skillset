---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCreditorAgentInstruction1Code"]
code_set: "ExternalCreditorAgentInstruction1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCreditorAgentInstruction1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCreditorAgentInstruction1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies further instructions concerning the processing of a payment instruction, as provided to the creditor agent.
*`CHQB`-(Ultimate) creditor must be paid by cheque.
*`HOLD`-Amount of money must be held for the (ultimate) creditor, who will call. Pay on identification.
*`PHOB`-Please advise/contact (ultimate) creditor/claimant by phone.
*`PRTK`-Indicates that a payer token is requested/used.
*`RECI`-Further information regarding the intended recipient.
*`TELB`-Please advise/contact (ultimate) creditor/claimant by the most efficient means of telecommunication.
*`TKCM`-Token found with counterparty mismatch.
*`TKSG`-Single Use Token already used.
*`TKSP`-Token found with suspended status.
*`TKVE`-Token found with value limit rule violation.
*`TKXP`-Token expired.
*`TOKN`-Token information.
*`VLTK`-Additional validation information to be used in conjunction with the token.
*`SEID`-Use of Secondary Identification of Creditor Account (which may relate to Head Office Collection Account, Building Society Roll Number or Credit Card Primary Account Number).

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
| 1 | CHQB |
| 2 | HOLD |
| 3 | PHOB |
| 4 | PRTK |
| 5 | RECI |
| 6 | TELB |
| 7 | TKCM |
| 8 | TKSG |
| 9 | TKSP |
| 10 | TKVE |
| 11 | TKXP |
| 12 | TOKN |
| 13 | VLTK |
| 14 | SEID |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
