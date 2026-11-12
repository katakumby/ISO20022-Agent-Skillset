---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPaymentCancellationRejection1Code"]
code_set: "ExternalPaymentCancellationRejection1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPaymentCancellationRejection1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPaymentCancellationRejection1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for the rejection of a cancellation, as published in an external payment cancellation rejection code set.
External code sets can be downloaded from www.iso20022.org.
*`AC04`-Account number specified has been closed on the receiver’s books.
*`ADAC`-Reported when the cancellation request cannot be processed because customer has not yet provided the debit authority on its account.
*`AGNT`-Reported when the cancellation cannot be accepted because of an agent refuses to cancel.
*`AM04`-Amount of funds available to cover specified message amount is insufficient.
*`ARDT`-Cancellation not accepted as the transaction has already been returned.
*`ARPL`-Reported when the cancellation request cannot be processed because no reply has been  received yet from the receiver of the request message.
*`CUST`-Reported when the cancellation cannot be accepted because of a customer decision (Creditor).
*`LEGL`-Reported when the cancellation cannot be accepted because of regulatory rules.
*`NARR`-Reason is provided as narrative information in the additional reason information.
*`NOAS`-No response from beneficiary (to the cancellation request).
*`NOOR`-Original transaction (subject to cancellation) never received.
*`PTNA`-Reported when the cancellation request cannot be accepted because the payment instruction has been passed to the next agent.
*`RQDA`-Reported when authority is required by the Creditor to return the payment.
*`WSEQ`-Reported when the cancellation request cannot be processed because the sequence referred to in the request is not valid.
*`INDM`-Complementing a Pending or Reject Status. Payment cancellation request cannot be accepted until an indemnity agreement is established.
*`ACLR`-Request-to-pay has already been cancelled.
*`AEXR`-Request-to-pay Expiry Date and Time has already passed.
*`ARFR`-Request-to-pay has already been refused by the Debtor.
*`ARJR`-Request-to-pay has already been rejected.
*`PATE`-Payment related to the request-to-pay has already been transmitted for execution.
*`RR04`-Regulatory Reason.
*`RCAR`-Request for cancellation of the request-to-pay has already been rejected.
*`RCNR`-Request for cancellation of the request-to-pay has never been received.
*`RCPR`-Request for cancellation of the request-to-pay has already been received and processed.
*`URTP`-Request-to-pay is unknown.
*`AACR`-Request-to-pay (RTP) has already been accepted.
*`ARJT`-Underlying transaction already rejected.

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
| 1 | AC04 |
| 2 | ADAC |
| 3 | AGNT |
| 4 | AM04 |
| 5 | ARDT |
| 6 | ARPL |
| 7 | CUST |
| 8 | LEGL |
| 9 | NARR |
| 10 | NOAS |
| 11 | NOOR |
| 12 | PTNA |
| 13 | RQDA |
| 14 | WSEQ |
| 15 | INDM |
| 16 | ACLR |
| 17 | AEXR |
| 18 | ARFR |
| 19 | ARJR |
| 20 | PATE |
| 21 | RR04 |
| 22 | RCAR |
| 23 | RCNR |
| 24 | RCPR |
| 25 | URTP |
| 26 | AACR |
| 27 | ARJT |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
