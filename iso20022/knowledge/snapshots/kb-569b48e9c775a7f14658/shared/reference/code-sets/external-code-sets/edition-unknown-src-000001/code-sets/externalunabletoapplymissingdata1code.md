---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalUnableToApplyMissingData1Code"]
code_set: "ExternalUnableToApplyMissingData1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalUnableToApplyMissingData1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalUnableToApplyMissingData1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason of an unable to apply due to missing data, as published in an external unable to apply missing data code set.
External code sets can be downloaded from www.iso20022.org.
*`MS01`-RemittanceInformation is missing.
*`MS02`-Instruction for next agent is missing (former MissingSenderToReceiverInformation split into debtor, credit and next agent information).
*`MS03`-Debtor is missing.
*`MS04`-DebtorAccount is missing.
*`MS05`-DebtorAgent is missing (former MissingFirstAgent for credit transfers).
*`MS06`-Amount is missing.
*`MS07`-SettlementAccount is missing. (former MissingNostroVostroAccount).
*`MS08`-Intermediary is missing.
*`MS09`-InstructingReimbursementAgent is missing (former MissingReimbursementAgent1).
*`MS10`-InstructedReimbursementAgent is missing (former MissingReimbursementAgent2).
*`MS11`-Third reimbursement agent is missing (former MissingReimbursementAgent).
*`MS12`-Creditor is missing.
*`MS13`-CreditorAccount is missing.
*`MS14`-Payment instruction is missing.
*`MS15`-Creditor agent is missing (former MissingFirstAgent for direct debits).
*`MS16`-Instruction for creditor agent is missing (former MissingSenderToReceiverInformation split into debtor, credit and next agent information).
*`MS17`-Instruction for debtor agent is missing (former MissingSenderToReceiverInformation split into debtor, credit and next agent information).
*`MS18`-RelatedRemittanceInformation is missing.
*`NARR`-See narrative field for additional information.

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
| 1 | MS01 |
| 2 | MS02 |
| 3 | MS03 |
| 4 | MS04 |
| 5 | MS05 |
| 6 | MS06 |
| 7 | MS07 |
| 8 | MS08 |
| 9 | MS09 |
| 10 | MS10 |
| 11 | MS11 |
| 12 | MS12 |
| 13 | MS13 |
| 14 | MS14 |
| 15 | MS15 |
| 16 | MS16 |
| 17 | MS17 |
| 18 | MS18 |
| 19 | NARR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
