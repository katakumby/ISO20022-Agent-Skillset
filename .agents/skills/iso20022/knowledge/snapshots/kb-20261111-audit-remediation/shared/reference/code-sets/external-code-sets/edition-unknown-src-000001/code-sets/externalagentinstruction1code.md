---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalAgentInstruction1Code"]
code_set: "ExternalAgentInstruction1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalAgentInstruction1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalAgentInstruction1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies further instructions for the agent concerning the processing of an instruction.
External code sets can be downloaded from www.iso20022.org.
*`CHQB`-(Ultimate) creditor must be paid by cheque.
*`HOLD`-Amount of money must be held for the (ultimate) creditor, who will call. Pay on identification.
*`INQR`-Additional Information to an inquiry reason must be provided.
*`PBEN`-(Ultimate) creditor to be paid only after verification of identity.
*`PHOA`-Please advise/contact next agent by phone.
*`PHOB`-Please advise/contact (ultimate) creditor/claimant by phone.
*`TELA`-Please advise/contact next agent by the most efficient means of telecommunication.
*`TELB`-Please advise/contact (ultimate) creditor/claimant by the most efficient means of telecommunication.
*`TFRO`-Payment instruction will be valid and eligible for execution from the date and time stipulated.
*`TTIL`-Payment instruction is valid and eligible for execution until the date and time stipulated. Otherwise, the payment instruction will be rejected.

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
| 3 | INQR |
| 4 | PBEN |
| 5 | PHOA |
| 6 | PHOB |
| 7 | TELA |
| 8 | TELB |
| 9 | TFRO |
| 10 | TTIL |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
