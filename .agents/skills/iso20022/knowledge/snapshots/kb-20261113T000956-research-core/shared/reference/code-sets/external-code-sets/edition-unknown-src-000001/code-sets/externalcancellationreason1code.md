---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCancellationReason1Code"]
code_set: "ExternalCancellationReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCancellationReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCancellationReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the cancellation reason, as published in an external cancellation reason code set.
External code sets can be downloaded from www.iso20022.org.
*`AC02`-Debtor account number invalid or missing.
*`AC03`-Wrong account number in Credit Transfer.
*`AGNT`-Agent in the payment workflow is incorrect.
*`AM09`-Amount is not the amount agreed or expected.
*`BE16`-Debtor or Ultimate Debtor identification code missing or invalid.
*`COVR`-Cover payments has either been returned or cancelled.
*`CURR`-Currency of the payment is incorrect.

*`CUST`-Cancellation requested by the Debtor.
*`CUTA`-Cancellation requested because an investigation request has been received and no remediation is possible.
*`DS24`-Cancellation requested because the original payment order expired due to time-out.
*`DT01`-Invalid date (for example, wrong or missing settlement date).
*`DUPL`-Payment is a duplicate of another payment.
*`FRAD`-Cancellation requested following a transaction that was originated fraudulently. The use of the FraudulentOrigin code should be governed by jurisdictions.
*`FRNA`-To complement a rejection response, suggesting the request for cancelation should be forwarded to the next agent in the payment transaction chain.
*`FRTR`-Direct Debit Tracking recalled as Mandate Cancelled.
*`INDM`-To express the wish to establish a bilateral indemnity agreement.
*`MODT`-The underlying transaction in relation to an RTP was modified.
*`PAID`-The underlying transaction in relation to an RTP was already paid (via other means).
*`SVNR`-The payment is cancelled since a cash amount rendered was not correct or goods or a service was not rendered to the customer, e.g. in an e-commerce situation.
*`SYAD`-Cancellation requested by System Member to Settlement System Administrator to indicate that the cancellation request must not be forwarded further in the chain.
*`TECH`-Cancellation requested following technical problems resulting in an erroneous transaction.
*`UPAY`-Payment is not justified.
*`ENUE`-Cancellation or request for return requested by the Debtor specifically due to one or more errors by debtor in the original Credit Transfer. Usage: This code can be used for any error in the original Credit Transfer made by the Debtor. Can also be used if multiple errors were made in the original Credit Transfer.
*`UAPA`-The Debtor is requesting a return of the payment because the payment was not properly authorized.
Usage: This code can be used in the case where a Credit Transfer was made without proper authorization from the Debtor. This could be due to compromised end user credentials.
*`NARR`-Reason is provided as narrative information in the additional reason information.
*`INCR`-Process a cancellation request with incorrect reference to original batch.
*`BIAS`-Process a cancellation request but batch already settled.
*`DRTP`-Duplication of a request-to-pay message.
*`WNTB`-Breach of warranty provided in connection with a request for payment.
*`MD06`-Return of funds requested by end customer.
*`PPRC`-Request to Pay cancellation initiated because the Payee is not in good standing.
*`ECAG`-Payee (Creditor) cancels the Request To Pay (RTP) request due to error or adjustment agreement with Payer/Debtor.
*`NFNA`-To complement a cancellation request, instructing the market infrastructure that the request for cancelation should not be forwarded to the next agent in the payment transaction chain.

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
| 1 | AC02 |
| 2 | AC03 |
| 3 | AGNT |
| 4 | AM09 |
| 5 | BE16 |
| 6 | COVR |
| 7 | CURR |
| 8 | CUST |
| 9 | CUTA |
| 10 | DS24 |
| 11 | DT01 |
| 12 | DUPL |
| 13 | FRAD |
| 14 | FRNA |
| 15 | FRTR |
| 16 | INDM |
| 17 | MODT |
| 18 | PAID |
| 19 | SVNR |
| 20 | SYAD |
| 21 | TECH |
| 22 | UPAY |
| 23 | ENUE |
| 24 | UAPA |
| 25 | NARR |
| 26 | INCR |
| 27 | BIAS |
| 28 | DRTP |
| 29 | WNTB |
| 30 | MD06 |
| 31 | PPRC |
| 32 | ECAG |
| 33 | NFNA |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
