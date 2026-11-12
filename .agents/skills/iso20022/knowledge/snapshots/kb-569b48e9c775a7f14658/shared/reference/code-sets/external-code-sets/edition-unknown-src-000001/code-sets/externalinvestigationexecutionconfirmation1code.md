---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationExecutionConfirmation1Code"]
code_set: "ExternalInvestigationExecutionConfirmation1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationExecutionConfirmation1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationExecutionConfirmation1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the result of an investigation, as published in an external investigation execution confirmation code set.
External code sets can be downloaded from www.iso20022.org.
*`ACDA`-Used when a creditor accepts the debit authorisation.
*`ACNR`-The claim for non-receipt of a payment instruction is accepted.
*`ACVA`-The claim for value date correction is accepted.
*`CHRG`-Further charges details are provided to resolve the case.
*`CNCL`-Used when a requested cancellation is successful.
*`CONF`-Used when a payment has been checked and was correctly executed without any intervention.
*`CVAA`-The original value date was correct.
*`CWFW`-Used when a payment will be cancelled to solve an investigation case.
*`FTNA`-The cancellation request has been forwarded to the next agent for execution.
Usage: This code should only be utilised where a Case Id is not present.
*`ICOV`-Used when a transfer of funds has been initiated (a cover payment) to resolve a case.
*`IDUP`-Used when the requested check for a possible duplicate instruction is confirmed.
*`IPAY`-Used when the result of an investigation is, or will be, the initiation of a payment instruction.
*`IPYI`-Used when a payment instruction (eg. MT103) has been initiated to resolve a case.
*`MCOV`-Used when a transfer of funds has been modified (a cover payment) to resolve a case.
*`MODI`-Used when a requested modification is successful.
*`MWFW`-Used when the payment will be modified to solve an investigation case.
*`PDCR`-Used when a requested cancellation is pending.
*`PECR`-Used when a requested cancellation has been partially executed.
*`PURP`-Further purpose details are provided to resolve the case.
*`RJCR`-Used when a requested cancellation has been rejected.
*`RJNR`-The claim for non-receipt of a payment instruction is rejected.
*`RJVA`-The claim for value date correction is rejected.
*`SMTC`-Used when the entry in the statement is correct.
*`SMTI`-Used when the entry in the statement is incorrect and further information is provided with the resolution.
*`UWFW`-Used when sender wants to respond to an assignment with an Unable To Apply workflow.
*`BIAS`-Process a cancellation request but batch already settled.
*`IDNE`-Process a  Batch Cancellation "using an incorrect batch sequence number”.
*`IVCR`-Process a cancellation request with incorrect reference to original batch.
*`INFO`-Used when additional information has been sent to the beneficiary of a payment.
*`NINF`-Used when no additional information is available.
*`PDNG`-Used to inform that a response to an investigation is pending.

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
| 1 | ACDA |
| 2 | ACNR |
| 3 | ACVA |
| 4 | CHRG |
| 5 | CNCL |
| 6 | CONF |
| 7 | CVAA |
| 8 | CWFW |
| 9 | FTNA |
| 10 | ICOV |
| 11 | IDUP |
| 12 | IPAY |
| 13 | IPYI |
| 14 | MCOV |
| 15 | MODI |
| 16 | MWFW |
| 17 | PDCR |
| 18 | PECR |
| 19 | PURP |
| 20 | RJCR |
| 21 | RJNR |
| 22 | RJVA |
| 23 | SMTC |
| 24 | SMTI |
| 25 | UWFW |
| 26 | BIAS |
| 27 | IDNE |
| 28 | IVCR |
| 29 | INFO |
| 30 | NINF |
| 31 | PDNG |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
