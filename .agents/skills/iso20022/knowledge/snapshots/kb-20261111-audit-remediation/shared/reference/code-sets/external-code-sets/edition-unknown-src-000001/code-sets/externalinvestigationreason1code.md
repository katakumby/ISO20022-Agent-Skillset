---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationReason1Code"]
code_set: "ExternalInvestigationReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the investigation reason, as published in an external investigation reason code set.
External code sets can be downloaded from www.iso20022.org.
*`RERE`-Related transaction reference is incorrect, incomplete or missing.
*`SVLV`-Payment type service level is incorrect, incomplete or missing.
*`CAPU`-Payment type category purpose is incorrect, incomplete or missing.
*`REDT`-Requested execution date is incorrect or missing.
*`ISDT`-Interbank settlement date is incorrect.
*`ISAM`-Interbank settlement amount is incorrect.
*`AMNT`-An amount element has triggered the investigation.
*`DTOR`-Further information pertaining to the debtor is requested.
*`DTAG`-Further information pertaining to the debtor agent is requested.
*`IGRA`-Further information pertaining to the instructing reimbursement agent is requested.
*`IDRA`-Further information pertaining to the instructed reimbursement agent is requested.
*`TDRA`-Further information pertaining to the third reimbursement agent is requested.
*`INAG`-Further information pertaining to an intermediary agent is requested.
*`PYCC`-Payment type clearing channel is incorrect, incomplete or missing.
*`CTAG`-Further information pertaining to the creditor agent is requested.
*`CTOR`-Further information pertaining to the creditor is requested.
*`REIN`-Remittance information is incorrect, incomplete or missing.
*`PYPU`-Transaction payment purpose is incorrect, incomplete or missing.
*`CHBE`-Further information pertaining to the charge bearer is requested.
*`INNA`-Further information pertaining to the instruction for next agent is requested.
*`INCA`-Further information pertaining to the instruction for creditor agent is requested.
*`STET`-Further information pertaining to a statement entry is requested.
*`SEAC`-Further information pertaining to the settlement account is requested.
*`CHIN`-Further information pertaining to the charges information is requested.
*`ULTD`-Further information pertaining to the ultimate debtor is requested.
*`ULTC`-Further information pertaining to the ultimate creditor is requested.
*`PURP`-Further information pertaining to the purpose is requested.
*`INPA`-Further information pertaining to the initiating party is requested.
*`REGR`-Regulatory reporting is incomplete or missing.
*`TAXD`-Tax data is incomplete or missing.
*`FRAD`-Instrument is confirmed as fraudulent.
*`FCCI`-Investigation relates to financial crimes compliance.
*`FWTR`-Investigation relates to funds transfer regulation or wire transfer regulation.
*`CHCO`-Copy of cheque is requested.
*`DRCO`-Copy of draft is requested.
*`AMLI`-Request message relates to anti-money laundering.
*`RQPR`-Clarification over a party relationship is requested.
*`RQVD`-Clarification over a vessel or aircraft is requested.
*`RQLD`-Clarification over location details is requested.
*`RQSG`-Clarification over goods or services involved is requested.
*`RQED`-Clarification over when goods or services were exchanged is requested.
*`RQDO`-Documentation relating to the transaction is requested.
*`CHNP`-Cheque not yet paid despite being sent to agent.
*`NARR`-See AdditionalRequestData element for additional information
*`RQCD`-Account closure date is requested.
*`UTAP`-A booked entry cannot be applied by the creditor.
*`CCNR`-Creditor claims non-receipt of payment.
*`CONR`-Creditor agent claims non-receipt of cover or settlement.
*`PINC`-Payment initiation has not been settled or confirmed.
*`RQVA`-Revaluation of an entry is requested.
*`RQUF`-Use of funds on an entry is requested.
*`RQDA`-Debit authorisation on an entry is requested.
*`ACCT`-Investigation relating to an account.
*`RQCH`-Investigation relating to charges that have been taken or are unpaid.
*`RIMF`-Request from International Monetary Fund.
*`MCAT`-Missing credit amount on statement.
*`MDAT`-Missing debit amount on statement.
*`IIRT`-Invalid interest rate.
*`INCB`-Incorrect closing balance.
*`IAIB`-Incorrect accrued interest balance.
*`IDAI`-Incorrect daily accrued interest amount.
*`INTA`-Incorrect transaction amount.

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
| 1 | RERE |
| 2 | SVLV |
| 3 | CAPU |
| 4 | REDT |
| 5 | ISDT |
| 6 | ISAM |
| 7 | AMNT |
| 8 | DTOR |
| 9 | DTAG |
| 10 | IGRA |
| 11 | IDRA |
| 12 | TDRA |
| 13 | INAG |
| 14 | PYCC |
| 15 | CTAG |
| 16 | CTOR |
| 17 | REIN |
| 18 | PYPU |
| 19 | CHBE |
| 20 | INNA |
| 21 | INCA |
| 22 | STET |
| 23 | SEAC |
| 24 | CHIN |
| 25 | ULTD |
| 26 | ULTC |
| 27 | PURP |
| 28 | INPA |
| 29 | REGR |
| 30 | TAXD |
| 31 | FRAD |
| 32 | FCCI |
| 33 | FWTR |
| 34 | CHCO |
| 35 | DRCO |
| 36 | AMLI |
| 37 | RQPR |
| 38 | RQVD |
| 39 | RQLD |
| 40 | RQSG |
| 41 | RQED |
| 42 | RQDO |
| 43 | CHNP |
| 44 | NARR |
| 45 | RQCD |
| 46 | UTAP |
| 47 | CCNR |
| 48 | CONR |
| 49 | PINC |
| 50 | RQVA |
| 51 | RQUF |
| 52 | RQDA |
| 53 | ACCT |
| 54 | RQCH |
| 55 | RIMF |
| 56 | MCAT |
| 57 | MDAT |
| 58 | IIRT |
| 59 | INCB |
| 60 | IAIB |
| 61 | IDAI |
| 62 | INTA |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
