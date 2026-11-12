---
template: false
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "concept"
concept_id: "bank-transaction-code-reporting"
source_locations: ["P91–P183; §§3.1–3.4.1", "P321–P354; §3.5", "T1–T55"]
issues: ["issue-000002", "issue-000033"]
---

# Bank Transaction Code reporting and code selection

[src-000003](../../../../../evidence/omitted/1dcbe16191b6c8898a146b17.md) is titled Bank Transaction Codes — External Code Sets, November 2025, Version 8.0 — Approved Version (P10–P11, cover; T55 final revision row). The original footer still states May 2025. Publication metadata and the separately supplied combination workbook remain distinct; [issue-000002](../../../../../tracking/issues.md) records the conflict.

## Purpose and participants

The code supplies harmonised transaction reasons in bank-to-customer cash-account reporting. The servicer reports the transaction; the owner uses it for cash management, reconciliation and routing to a suitable customer processing system (P92–P101, §3.1.1; rendered page 5). Use the [scoped participant library](participants.md) and [narrative flow references](flows/index.md). These reporting codes do not choose an exact ISO message or assign its transport sender.

## Structure and conditional rules

The structured part has Domain, Family and Sub-family levels. Domain identifies the highest business area/sub-ledger; Family refines the activity; Sub-family refines the product. They use ExternalBankTransactionDomain1Code, ExternalBankTransactionFamily1Code and ExternalBankTransactionSubFamily1Code respectively (T1, P106–P108). The source allows a structured code and proprietary code together. If Domain is absent, Proprietary must be present; if Proprietary is absent, Domain must be present (P110–P112). These are business conditions distinct from the illustrative optional child multiplicities.

[Complete field table, cardinalities and definitions](documents/src-000003/tables/tbl-0002.md) · [Source structure diagram](documents/src-000003/diagrams/fig-0003.md). The source illustration names BankTransactionCodeStructure4/5/6 and ProprietaryBankTransactionCodeStructure1; it does not replace the supplied schema for a particular message.

## Proprietary and generic codes

The proprietary element supports initial migration from national code sets and codes not yet registered but proposed for inclusion. Available structured Domain/Family/Sub-family information may still be supplied (P119–P123, §3.1.3). The supplied 143/BAI sample is preserved as a source example, without inventing its meaning.

The four generic families are Not available, Other, Miscellaneous Credit Operations and Miscellaneous Debit Operations (T4). Not available means no further family detail; Other means further detail exists but no listed family matches. Extended Domain is special: only Not available Family and Not available Sub-family are allowed (T15 and P175, §3.3.12).

T16/§3.4.1 states 12 generic sub-families, with a single Adjustments definition. T47/§4.3.2 instead lists 13, including Credit Adjustments=DAJT and Debit Adjustments=CAJT exactly as printed. [issue-000033](../../../../../tracking/issues.md) preserves the discrepancy; neither count nor code pairing is silently corrected. Foreign Exchange, Precious Metal and Commodities, and exceptionally Securities/Custody Collection, are described as using only the generic sub-family codes (§3.5, pages 58–61). Read that statement with the recorded count discrepancy.

## Definitions and complete code tables

[Document and table index](documents/src-000003/index.md) preserves all 55 tables, 1,188 physical rows including source headers, 3,721 nonempty physical cells and three substantive footnotes. Definitions remain separate from the four-character code lists and status dates. The source labels and historical status dates are literal evidence, not assertions of current market policy.

The source Sweep definition directs users to Cash Management / Account Balancing / Sweeping instead (T41 row 20, rendered page 54); the note is retained. Securities source overview diagrams omit the LACK family that is present in T13/T45; use complete tables rather than treating an overview as exhaustive.

## Cancellation, return and reversal distinctions

In the credit-transfer definition, Reversal due to Payment Cancellation Request concerns a debtor request after the debtor was debited and before interbank settlement completes (T17 row 15; code RPCR in T48). Reversal due to Payment Return/reimbursement is separately defined (T17 row 16; RRTN in T48), as is ACH Reversal under pre-established rules (T17 row 23; AREV).

For direct debit, the cancellation request comes from the creditor after crediting and before interbank settlement completes (T19 row 11; RCDD in T48). Return/Unpaid Direct Debit (T19 row 12; UPDD) and Payment Reversal (T19 row 13; PRDD) have separate definitions. These are cash-reporting classifications. They do not establish that a payment cancellation message, securities settlement cancellation or securities movement reversal uses the same semantics or direction.

## Review and limitations

All 91 Word-rendered pages were visually inspected on 2026-11-09. All 55 table cell texts were reconciled against their mapped PDF page spans; the composite figure cell was handled separately. All 15 substantive reference diagrams were reconstructed, rendered using Mermaid 12.3.0 and visually compared; one additional drawing occurrence is a prose text box. Source checkums are unchanged. The publication remains needs-review for the explicit edition and generic-subfamily discrepancies, while transcription reviews are recorded individually.
