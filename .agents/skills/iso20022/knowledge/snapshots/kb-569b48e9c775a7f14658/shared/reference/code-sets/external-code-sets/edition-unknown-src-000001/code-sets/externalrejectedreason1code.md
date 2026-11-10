---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalRejectedReason1Code"]
code_set: "ExternalRejectedReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalRejectedReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalRejectedReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for a rejected status
The list of valid codes is an external code list published separately. External code sets can be downloaded from www.iso20022.org.
*`ADEA`-Received after the servicer's deadline
*`BDAY`-Date is not a business day
*`CTRC`-Unrecognised or invalid client
*`DPRG`-Request has been rejected because the instruction process is in progress or has been processed
*`INDT`-Some message details specified in the instruction/request are inconsistent with those that expected
*`MISM`-The request cannot be executed. The message requested is not valid
*`NAUT`-Permission to be processed is not granted
*`NINS`-Referred instrument does not exist
*`NOAC`-Client has no access to the service
*`TERM`-Unrecognised or invalid effective date/time
*`ASBR`-Acknowledgement of settlement batch received from PSO for settlement.
*`AB15`-Settlement Instruction with invalid account number or specific settlement type.
*`AB26`-Invalid batch Settlement Instruction received.
*`AB12`-Process a Batch Removal Instruction with an incorrect Batch Concurrent Sequence.
*`DT07`-Process a Batch Removal Instruction with an incorrect "Original Creation Date and Time" for the batch.
*`AB13`-Invalid routing code send by participant to settlement operator.
*`AB21`-Processing interbank batch settlement instruction with invalid agreement number for settlement type.
*`ISWS`-Invalid settlement window for settlement instruction.
*`MISN`-Missing ISIN on settlement instruction.
*`NOFR`-Warning messages that is send to participants when settlement account must be funded.
*`RC14`-Participant is in BCP no settlement instruction for CLS.
*`RC16`-Originator of the instruction is not an active participant in SADC RTGS.
*`RC15`-Participant is not an active member of a specific settlement type.
*`RC13`-Originator of the instruction is not an active participant in RTGS.
*`SBRN`-Settlement batch removal notification due to batch not funded at window closure by participants.

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
| 1 | ADEA |
| 2 | BDAY |
| 3 | CTRC |
| 4 | DPRG |
| 5 | INDT |
| 6 | MISM |
| 7 | NAUT |
| 8 | NINS |
| 9 | NOAC |
| 10 | TERM |
| 11 | ASBR |
| 12 | AB15 |
| 13 | AB26 |
| 14 | AB12 |
| 15 | DT07 |
| 16 | AB13 |
| 17 | AB21 |
| 18 | ISWS |
| 19 | MISN |
| 20 | NOFR |
| 21 | RC14 |
| 22 | RC16 |
| 23 | RC15 |
| 24 | RC13 |
| 25 | SBRN |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
