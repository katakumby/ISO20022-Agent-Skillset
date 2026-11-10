---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPaymentGroupStatus1Code"]
code_set: "ExternalPaymentGroupStatus1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPaymentGroupStatus1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPaymentGroupStatus1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the status of a group of payment instructions, as published in an external payment group status code set.
External code sets can be downloaded from www.iso20022.org.
*`ACCP`-Preceding check of technical validation was successful. Customer profile check was also successful.
*`ACCC`-Settlement on the creditor's account has been completed.
*`ACSC`-Settlement on the debtor's account has been completed.
Usage : this can be used by the first agent to report to the debtor that the transaction has been completed. 
Warning : this status is provided for transaction status reasons, not for financial information. It can only be used after bilateral agreement

*`ACSP`-All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution.
*`ACTC`-Authentication and syntactical and semantical validation are successful
*`ACWC`-Instruction is accepted but a change will be made, such as date or remittance not sent.
*`PART`-A number of transactions have been accepted, whereas another number of transactions have not yet achieved
'accepted' status.
*`PDNG`-Payment initiation or individual transaction included in the payment initiation is pending. Further checks and status update will be performed.
*`RCVD`-Payment initiation has been received by the receiving agent
*`RJCT`-Payment initiation or individual transaction included in the payment initiation has been rejected.
*`RCVC`-Verification of Payee check have been applied to received transactions stating to be complete without mismatching data.
*`RVCM`-Verification of Payee checks have been applied to received transactions stating to be complete containing mismatching data.
*`RVNC`-Verification of party check on transactions received is not yet completed.

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
| 1 | ACCP |
| 2 | ACCC |
| 3 | ACSC |
| 4 | ACSP |
| 5 | ACTC |
| 6 | ACWC |
| 7 | PART |
| 8 | PDNG |
| 9 | RCVD |
| 10 | RJCT |
| 11 | RCVC |
| 12 | RVCM |
| 13 | RVNC |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
