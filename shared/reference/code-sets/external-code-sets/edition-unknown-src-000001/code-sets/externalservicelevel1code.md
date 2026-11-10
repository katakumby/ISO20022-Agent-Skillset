---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalServiceLevel1Code"]
code_set: "ExternalServiceLevel1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalServiceLevel1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalServiceLevel1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external service level code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`BKTR`-Payment through internal book transfer.
*`G001`-Tracked Customer Credit Transfer.
*`G002`-Tracked Stop and Recall.
*`G003`-Tracked Outbound Corporate Transfer.
*`G004`-Tracked Financial Institution Transfer.
*`NPCA`-Payments must be executed following the NPC Area Payment scheme.
*`NUGP`-Payment must be executed as a non-urgent transaction with priority settlement.
*`NURG`-Payment must be executed as a non-urgent transaction, which is typically identified as an ACH or low value transaction.
*`PRPT`-Transaction must be processed according to the EBA Priority Service.
*`SDVA`-Payment must be executed with same day value to the creditor.
*`SEPA`-Payment must be executed following the Single Euro Payments Area scheme.
*`SVDE`-Payment execution following the cheque agreement and traveller cheque agreement of the German Banking Industry Committee (Die Deutsche Kreditwirtschaft - DK) and Deutsche Bundesbank – Scheck Verrechnung Deutschland
*`URGP`-Payment must be executed as an urgent transaction cleared through a real-time gross settlement system, which is typically identified as a wire or high value transaction.
*`URNS`-Payment must be executed as an urgent transaction cleared through a real-time net settlement system, which is typically identified as a wire or high value transaction.
*`INST`-Used for payment initiation to identify that a Payment or Direct Debit initiation must be executed as an instant or real-time payment instrument.
*`SRTP`-Request to Pay (RTP) transaction refers to an RTP scheme (such as for example the SEPA Request to Pay (SRTP) scheme).
*`SVAT`-Scheck Verarbeitung Austria (Cheque Processing).
*`G006`-Specifies the service conditions applicable to a tracked exceptions and investigations case.
*`G007`-Specifies the service level for a tracked inbound customer credit transfer.
*`G005`-Tracked Instant Customer Credit Transfer.


*`G009`-Specifies the service level for a tracked low-value cross-border customer credit transfer.
*`WFSM`-Transaction is to be treated as an advice and only applied to the account of the creditor or next agent after settlement of the cover has been confirmed.
*`EOLO`-Payment is executed following a Euro One-Leg Out Scheme.
*`SPLI`-A split payment is a payment that is split into several payments of lower value, namely with the purpose to comply with maximum amount thresholds applicable to some domestic Payment Market Infrastructures or to reduce counterparty liquidity risk.
*`IRCA`-Payment must be executed following the Icelandic Rulebook Council Area (IRCA) scheme.
*`EAPS`-Identifies payments executed under the East African Payment System (EAPS), the regional cross-border settlement scheme operated by EAC central banks.
*`SPSC`-Transaction must be processed according to the Swift Scheme rulebook.
*`SD01`-Digital asset transactions must be processed according to the Swift Ledger rules.
*`NOLO`-Payment is executed following the NPC One-Leg Out Scheme.

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
| 1 | BKTR |
| 2 | G001 |
| 3 | G002 |
| 4 | G003 |
| 5 | G004 |
| 6 | NPCA |
| 7 | NUGP |
| 8 | NURG |
| 9 | PRPT |
| 10 | SDVA |
| 11 | SEPA |
| 12 | SVDE |
| 13 | URGP |
| 14 | URNS |
| 15 | INST |
| 16 | SRTP |
| 17 | SVAT |
| 18 | G006 |
| 19 | G007 |
| 20 | G005 |
| 21 | G009 |
| 22 | WFSM |
| 23 | EOLO |
| 24 | SPLI |
| 25 | IRCA |
| 26 | EAPS |
| 27 | SPSC |
| 28 | SD01 |
| 29 | NOLO |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
