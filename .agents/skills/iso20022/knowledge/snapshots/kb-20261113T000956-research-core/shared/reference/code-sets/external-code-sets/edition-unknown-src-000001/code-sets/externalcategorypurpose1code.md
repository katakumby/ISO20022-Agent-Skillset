---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCategoryPurpose1Code"]
code_set: "ExternalCategoryPurpose1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCategoryPurpose1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCategoryPurpose1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the category purpose, as published in an external category purpose code list.
External code sets can be downloaded from www.iso20022.org.
*`BONU`-Transaction is the payment of a bonus.
*`CASH`-Transaction is a general cash management instruction.
*`CBLK`-A service that is settling money for a bulk of card transactions, while referring to a specific transaction file or other information like terminal ID, card acceptor ID or other transaction details.
*`CCRD`-Transaction is related to a payment of credit card.
*`CORT`-Transaction is related to settlement of a trade, eg a foreign exchange deal or a securities transaction.
*`DCRD`-Transaction is related to a payment of debit card.
*`DIVI`-Transaction is the payment of dividends.
*`DVPM`-Code used to pre-advise the account servicer of a forthcoming deliver against payment instruction.
*`EPAY`-Transaction is related to ePayment.
*`FCIN`-Transaction is related to the payment of a fee and interest.
*`FCOL`-A service that is settling card transaction related fees between two parties.
*`GP2P`-General Person-to-Person Payment. Debtor and Creditor are natural persons.
*`GOVT`-Transaction is a payment to or from a government department.
*`HEDG`-Transaction is related to the payment of a hedging operation.
*`ICCP`-Transaction is reimbursement of credit card payment.
*`IDCP`-Transaction is reimbursement of debit card payment.
*`INTC`-Transaction is an intra-company payment, ie, a payment between two companies belonging to the same group.
*`INTE`-Transaction is the payment of interest.
*`LBOX`-Transaction is related to identify cash handling via Night Safe or Lockbox by bank or vendor on behalf of a physical store.
*`LOAN`-Transaction is related to the transfer of a loan to a borrower.
*`MP2B`-Mobile P2B Payment
*`MP2P`-Mobile P2P Payment
*`OTHR`-Other payment purpose.
*`PENS`-Transaction is the payment of pension.
*`RPRE`-Collection used to re-present previously reversed or returned direct debit transactions.
*`RRCT`-Transaction is related to a reimbursement for commercial reasons of a correctly received credit transfer.
*`RVPM`-Code used to pre-advise the account servicer of a forthcoming receive against payment instruction.
*`SALA`-Transaction is the payment of salaries.
*`SECU`-Transaction is the payment of securities.
*`SSBE`-Transaction is a social security benefit, ie payment made by a government to support individuals.
*`SUPP`-Transaction is related to a payment to a supplier.
*`TAXS`-Transaction is the payment of taxes.
*`TRAD`-Transaction is related to the payment of a trade finance transaction.
*`TREA`-Transaction is related to treasury operations.  E.g. financial contract settlement.
*`VATX`-Transaction is the payment of value added tax.
*`WHLD`-Transaction is the payment of withholding tax.
*`SWEP`-Classification: Cash Management. Transaction relates to a cash management instruction, requesting a sweep of the account of the Debtor above an agreed floor amount, up to a target or zero balance.
The purpose is to move the funds from multiple accounts to a single bank account. Funds can move domestically or across border and more than one bank can be used.
*`TOPG`-Classification: Cash Management. Transaction relates to a cash management instruction, requesting to top the account of the Creditor above a certain floor amount, up to a target or zero balance. 
The floor amount, if not pre-agreed by the parties involved, may be specified.
*`ZABA`-Transaction relates to a cash management instruction, requesting to zero balance the account of the Debtor.
Zero Balance Accounts empty or fill the balances in accounts at the same bank, in the same country into or out of a main account each day.
*`VOST`-Transaction to be processed as a domestic payment instruction originated from a foreign bank.
*`FCDT`-Foreign Currency Transaction that is processed between two domestic financial institutions.
*`CIPC`-Transaction is a direct debit for a cash order of notes and/or coins.
*`CONC`-Transaction is a direct debit for a cash order of notes and/or coins.
*`CGWV`-Transaction is a payment towards a Party for the collection of cash by the Cash in Transit company.
*`SAVG`-Transfer to / from savings or to retirement account.
*`CTDF`-Cross border transaction initiated by US natural person that is subject to compliance with Dodd Frank 1073.
*`CPAY`-Transaction is related to the payment of a claim though a claim payment system.
*`CDIS`-Additional disposition following a claim payment made through a claim payment system.
*`CRYP`-Transaction is related to the purchase or sale of crypto assets.

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
| 1 | BONU |
| 2 | CASH |
| 3 | CBLK |
| 4 | CCRD |
| 5 | CORT |
| 6 | DCRD |
| 7 | DIVI |
| 8 | DVPM |
| 9 | EPAY |
| 10 | FCIN |
| 11 | FCOL |
| 12 | GP2P |
| 13 | GOVT |
| 14 | HEDG |
| 15 | ICCP |
| 16 | IDCP |
| 17 | INTC |
| 18 | INTE |
| 19 | LBOX |
| 20 | LOAN |
| 21 | MP2B |
| 22 | MP2P |
| 23 | OTHR |
| 24 | PENS |
| 25 | RPRE |
| 26 | RRCT |
| 27 | RVPM |
| 28 | SALA |
| 29 | SECU |
| 30 | SSBE |
| 31 | SUPP |
| 32 | TAXS |
| 33 | TRAD |
| 34 | TREA |
| 35 | VATX |
| 36 | WHLD |
| 37 | SWEP |
| 38 | TOPG |
| 39 | ZABA |
| 40 | VOST |
| 41 | FCDT |
| 42 | CIPC |
| 43 | CONC |
| 44 | CGWV |
| 45 | SAVG |
| 46 | CTDF |
| 47 | CPAY |
| 48 | CDIS |
| 49 | CRYP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
