---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPaymentTransactionStatus1Code"]
code_set: "ExternalPaymentTransactionStatus1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPaymentTransactionStatus1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPaymentTransactionStatus1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the status of an individual payment instructions, as published in an external payment transaction status code set.
External code sets can be downloaded from www.iso20022.org.
*`ACCC`-Settlement on the creditor's account has been completed.
*`ACCP`-Preceding check of technical validation was successful. Customer profile check was also successful.
*`ACFC`-Preceding check of technical validation and customer profile was successful and an automatic funds check was positive.
*`ACIS`-Payment instruction to issue a cheque has been accepted, and the cheque has been issued but not yet been deposited or cleared.
*`ACSC`-Settlement completed.
Usage : this can be used by a Market Infrastructure reporting to Infrastructure Participant or an Account Servicer to Account Owner to report that the transaction account entry has been completed.
Warning : this status is provided for transaction status reasons, not for financial information. It can only be used after bilateral agreement

*`ACSP`-All preceding checks such as technical validation and customer profile were successful and therefore the payment instruction has been accepted for execution.
*`ACTC`-Authentication and syntactical and semantical validation are successful
*`ACWC`-Instruction is accepted but a change will be made, such as date or remittance not sent.
*`ACWP`-Payment instruction included in the credit transfer is accepted without being posted to the creditor customer’s account.
*`BLCK`-Payment transaction previously reported with status 'ACWP' is blocked, for example, funds will neither be posted to the Creditor's account, nor be returned to the Debtor.
*`CANC`-Payment initiation has been successfully cancelled after having received a request for cancellation.
Usage: code to be used in the context of APIs only.
*`CPUC`-Cash has been picked up by the Creditor.
*`PATC`-Payment initiation needs multiple authentications, where some but not yet all have been performed. Syntactical and semantical validations are successful.
*`PDNG`-Payment instruction is pending. Further checks and status update will be performed.
*`PRES`-Request for Payment has been presented to the Debtor.
*`RCVD`-Payment instruction has been received.
*`RJCT`-Payment instruction has been rejected.
*`ACPD`-Status of transaction released from the Debtor Agent and accepted by the clearing.
*`RCVC`-Verification of Payee check has been applied to received transaction stating to be complete without mismatching data.
*`RVNA`-Verification of Payee check has been applied to received transaction stating to be complete with not applicable data.
*`RVNM`-Verification of Payee check has been applied to received transaction stating to be complete with mismatching data.
*`RVMC`-Verification of Payee check has been applied to received transaction stating to be complete with data matching closely.
*`ACFW`-Preceding check of technical validation and customer profile was successful, and an automatic funds check was positive, but an explicit confirmation by the initiating party is outstanding.
*`RVNC`-Verification of party check on the transaction is not yet completed.
*`RVCM`-Verification of Payee checks have been applied to received transaction stating to be completed containing mismatching data.

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
| 1 | ACCC |
| 2 | ACCP |
| 3 | ACFC |
| 4 | ACIS |
| 5 | ACSC |
| 6 | ACSP |
| 7 | ACTC |
| 8 | ACWC |
| 9 | ACWP |
| 10 | BLCK |
| 11 | CANC |
| 12 | CPUC |
| 13 | PATC |
| 14 | PDNG |
| 15 | PRES |
| 16 | RCVD |
| 17 | RJCT |
| 18 | ACPD |
| 19 | RCVC |
| 20 | RVNA |
| 21 | RVNM |
| 22 | RVMC |
| 23 | ACFW |
| 24 | RVNC |
| 25 | RVCM |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
