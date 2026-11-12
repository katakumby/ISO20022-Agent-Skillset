---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPaymentModificationRejection1Code"]
code_set: "ExternalPaymentModificationRejection1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPaymentModificationRejection1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPaymentModificationRejection1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for the rejection of a modification, as published in an external payment modification rejection code set.
External code sets can be downloaded from www.iso20022.org.
*`UM01`-Related transaction reference cannot be modified.
*`UM02`-Service level element of payment type cannot be modified(former UnableToModifyBankOperationCode).
*`UM03`-Category purpose element of payment type cannot be modified (former UnableToModifyInstructionCode).
*`UM04`-RequestedExecutionDate cannot be modified.
*`UM05`-InterbankSettlementDate cannot be modified (former UnableToModifyValueDate).
*`UM06`-SettlementAccount cannot be modified (former UnableToModifyInterbankSettlementAccount).
*`UM07`-Debtor cannot be modified.
*`UM08`-DebtorAccount cannot be modified.
*`UM09`-InstructedReimbursementAgent cannot be modified (former UnableToModifyReceiverCorrespondent).
*`UM10`-ThirdReimbursementAgent cannot be modified (former UnableToModifyThirdReimbursementInstitution).
*`UM11`-Clearing Channel element of payment type cannot be modified (former UnableToModifyPaymentScheme)
*`UM12`-Creditor agent account cannot be modified (former UnableToModifyAccountOfBeneficiaryInstitution)
*`UM13`-Creditor cannot be modified.
*`UM14`-Creditor account cannot be modified.
*`UM15`-Remittance information cannot be modified.
*`UM16`-PaymentPurpose cannot be modified.
*`UM17`-Charge bearer cannot be modified (former UnableToModifyDetailsOfCharges).
*`UM18`-Instruction for next agent cannot be modified (former UnableToModifySenderToReceiver).
*`UM19`-Instruction for creditor agent cannot be modified. (former UnableToModifyInstructionForFinalAgent).
*`UM20`-Used to inform of cancellation and request a new payment instruction. This should only be used if an agent does not want to modify a pending payment.
*`UM21`-Modification is not possible and the cancellation is requested.
*`UM22`-Debtor agent account cannot be modified (applicable for direct debits).
*`UM23`-Interbank settlement amount cannot be modified.
*`UM24`-Instruction for debtor agent cannot be modified (applicable for direct debits)
*`UM25`-Requested collection date cannot be modified (applicable for direct debits)
*`UM26`-Payment type cannot be modified.
*`UM27`-Instructed or equivalent amount cannot be modified.
*`UM28`-Priority of payment message cannot be modified.

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
| 1 | UM01 |
| 2 | UM02 |
| 3 | UM03 |
| 4 | UM04 |
| 5 | UM05 |
| 6 | UM06 |
| 7 | UM07 |
| 8 | UM08 |
| 9 | UM09 |
| 10 | UM10 |
| 11 | UM11 |
| 12 | UM12 |
| 13 | UM13 |
| 14 | UM14 |
| 15 | UM15 |
| 16 | UM16 |
| 17 | UM17 |
| 18 | UM18 |
| 19 | UM19 |
| 20 | UM20 |
| 21 | UM21 |
| 22 | UM22 |
| 23 | UM23 |
| 24 | UM24 |
| 25 | UM25 |
| 26 | UM26 |
| 27 | UM27 |
| 28 | UM28 |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
