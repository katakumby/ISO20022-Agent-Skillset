---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalChargeType1Code"]
code_set: "ExternalChargeType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalChargeType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalChargeType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the nature, or use, of the charges in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`BRKF`-Fee paid to a broker for services provided.
*`BTCH`-Fee paid for processing a batch of transactions.
*`COMM`-Fee paid for services provided.
*`SUMM`-Summation of individual fees.
*`AMND`-Payment order was changed based on request to do so from the (original) sending bank or as a result of receiving amended information from the (original) sending bank.
*`CFEE`-Used when fees are assessed for cancellation of a payment.
*`CLEF`-Used when fees are assessed for standard processing of financial institution type transfers.
*`INVS`-Charges related to the processing of an investigation case/inquiry.
*`INTE`-Interest related charges.
*`NSTP`-Charge for a payment that required an intervention during processing.
*`DEBT`-Claim is being submitted in response to receiving a customer credit transfer with DEBT in Charge Bearer code.
*`TELE`-Charges relating to the most appropriate and efficient means of telecommunications available, for example, SWIFT, telex, telephone, facsimile, as determined by the party executing the payment instruction.
*`ACCM`-Account maintenance fee.
*`RECH`-Charge for a reporting message (camt.05X).

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
| 1 | BRKF |
| 2 | BTCH |
| 3 | COMM |
| 4 | SUMM |
| 5 | AMND |
| 6 | CFEE |
| 7 | CLEF |
| 8 | INVS |
| 9 | INTE |
| 10 | NSTP |
| 11 | DEBT |
| 12 | TELE |
| 13 | ACCM |
| 14 | RECH |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
