---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalUnableToApplyIncorrectData1Code"]
code_set: "ExternalUnableToApplyIncorrectData1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalUnableToApplyIncorrectData1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalUnableToApplyIncorrectData1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason of an unable to apply due to incorrect data, as published in an external unable to apply incorrect data code set.
External code sets can be downloaded from www.iso20022.org.
*`IN01`-Related transaction reference is incorrect.
*`IN02`-Payment type service level is incorrect (former IncorrectBankOperationCode).
*`IN03`-Payment type category purpose is incorrect (former IncorrectInstructionCode).
*`IN04`-RequestedExecutionDate is incorrect.
*`IN05`-Interbank settlement date is incorrect (former IncorrectValueDate).
*`IN06`-Interbank settlement amount is incorrect (former IncorrectSettledAmount).
*`IN07`-Debtor is incorrect.
*`IN08`-DebtorAccount is incorrect.
*`IN09`-InstructedReimbursementAgent is incorrect (former IncorrectReceiverCorrespondent).
*`IN10`-ThirdReimbursementAgent is incorrect (former IncorrectThirdReimbursementInstitution).
*`IN11`-Payment type clearing channel is incorrect (former PaymentScheme).
*`IN12`-CreditorAgentAccount is incorrect (former IncorrectAccountOfBeneficiaryInstitution).
*`IN13`-Creditor is incorrect.
*`IN14`-Creditor account is incorrect.
*`IN15`-RemittanceInformation is incorrect.
*`IN16`-Transaction payment purpose is incorrect.
*`IN17`-ChargeBearer is incorrect (former IncorrectDetailsOfCharges).
*`IN18`-Instruction for next agent is incorrect (former IncorrectSenderToReceiverInformation).
*`IN19`-Instruction for creditor agent is incorrect (former IncorrectInstructionForFinalAgent).
*`IN33`-Amount in statement entry is incorrect.
*`IN36`-SettlementAccount is incorrect.
*`IN37`-Instructing reimbursement agent is incorrect.
*`IN38`-Debtor's address is incorrect.
*`IN39`-Creditor's address is incorrect.
*`IN40`-RelatedRemittanceInformation is incorrect.
*`MM20`-Name and account of creditor are not matching.
*`MM21`-Name and account of debtor are not matching.
*`MM22`-Name and account of creditor agent (former FinalAgent) are not matching.
*`MM23`-Insufficient or incoherent details about the debtor with respect to regulatory requirements.
*`MM24`-Insufficient or incoherent details about the creditor with respect to regulatory requirements.
*`MM25`-Payment is pending execution. For reasons of regulatory requirements we request further information on the account number or unique identification of the debtor.
*`MM26`-Payment is pending execution. For reasons of regulatory requirements we request further information on the name and/or address of the debtor.
*`MM27`-Payment has been executed. For reasons of regulatory requirements we request further information on the account number or unique identification of the debtor.
*`MM28`-Payment has been executed. For reasons of regulatory requirements we request further information on the name and/or address of the debtor.
*`MM29`-Payment is pending execution. For reasons of regulatory requirements we request further information on the account number or unique identification of the creditor.
*`MM30`-Payment is pending execution. For reasons of regulatory requirements we request further information on the name and/or address of the creditor.
*`MM31`-Payment has been executed. For reasons of regulatory requirements we request further information on the account number or unique identification of the creditor.
*`MM32`-Payment has been executed. For reasons of regulatory requirements we request further information on the name and/or address of the creditor.
*`MM34`-Insufficient charges details provided.
*`MM35`-Payment purpose needs to be further specified.
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
| 1 | IN01 |
| 2 | IN02 |
| 3 | IN03 |
| 4 | IN04 |
| 5 | IN05 |
| 6 | IN06 |
| 7 | IN07 |
| 8 | IN08 |
| 9 | IN09 |
| 10 | IN10 |
| 11 | IN11 |
| 12 | IN12 |
| 13 | IN13 |
| 14 | IN14 |
| 15 | IN15 |
| 16 | IN16 |
| 17 | IN17 |
| 18 | IN18 |
| 19 | IN19 |
| 20 | IN33 |
| 21 | IN36 |
| 22 | IN37 |
| 23 | IN38 |
| 24 | IN39 |
| 25 | IN40 |
| 26 | MM20 |
| 27 | MM21 |
| 28 | MM22 |
| 29 | MM23 |
| 30 | MM24 |
| 31 | MM25 |
| 32 | MM26 |
| 33 | MM27 |
| 34 | MM28 |
| 35 | MM29 |
| 36 | MM30 |
| 37 | MM31 |
| 38 | MM32 |
| 39 | MM34 |
| 40 | MM35 |
| 41 | NARR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
