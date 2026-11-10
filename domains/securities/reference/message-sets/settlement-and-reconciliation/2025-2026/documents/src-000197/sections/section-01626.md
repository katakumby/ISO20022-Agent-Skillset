---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.168 UnmatchedReason12Code"]
file_pages: [2178, 2179]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.168 UnmatchedReason12Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2178 to 2179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2178

```text
CodeName Name Definition
not match. This includes Buyer/seller's
account, direct client's account at the
receiving/delivering agent, or receiving/
delivering agent's account at the CSD.
DMON SettlementAmount Settlement amount does not match.
DDAT SettlementDate Settlement date/time does not match.
SETS SettlementSystemMethod Settlement system/method does not
match (for example, instruction is to
settle using settlement system/method
A. Counterparty expects settlement to
occur using settlement system/method
B).
SETR SettlementTransaction Settlement transaction type does not
match (relates to the settlement
transaction type codes available for field:
22F:: SETR.).
TXST TaxStatus Disagreement on the tax status of the
financial instruments to be settled.
DTRD TradeDate Trade date does not match.
DELN TransactionDirection Direction of the trade does not match.
Counterparty expects a delivery from
you, not a receipt or vice versa.
UNBR UnmatchedMarketSide Market side trade is unmatched.
35.2.2.168  UnmatchedReason12Code
Definition: Specifies the reason the transaction, transfer or settlement instruction is unmatched.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
ACRU AccruedInterestAmount1 Accrued interest amount does not
match.
IIND CommonReference Common reference does not match.
CPCA CounterpartyCancelled Counterparty cancelled their instruction.
CLAT CounterpartyTooLateForMatching Counterparty's instruction was too late
for matching.
NCRR CurrencySettlementAmount Settlement amount currency does not
match.
DDEA DealPrice Deal price does not match.
DSEC FinancialInstrument Financial instrument identification does
not match, for example, ISIN, financial
instrument attributes differs.
DQUA FinancialInstrumentQuantity Quantity of financial instruments does
not match.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2178 March 2026
```

## File page 2179

```text
CodeName Name Definition
LEOG LetterOfGuarantee Counterparty is for settlement through
letter of guarantee, your instruction is
not, or vice versa.
LATE MarketDeadlineMissed Your instruction was too late for
matching.
MIME MissingMarketSide Missing market execution details.
CMIS NoMatch A matching instruction from your
counterparty could not be found.
NMAS NoMatchingStarted Matching process has not yet started.
DTRA NotRecognised Counterparty has been contacted or
contacted us, and does not recognise
the transaction.
OTHR Other Proprietary unmatched reason code
described in a narrative field.
FRAP PaymentCode Payment type does not match: your
instruction is free of payment, your
counterparty's instruction is against
payment or vice versa.
PHYS PhysicalSettlement Counterparty's instruction is physical
settlement, your instruction is not, or vice
versa.
INPS PlaceOfSafekeeping Place of safekeeping information does
not allow matching to take place.
PLCE PlaceOfTrade Place of trade does not match.
PODU PossibleDuplicate Instruction has not been matched. It is a
possible duplicate instruction.
DEPT ReceivingDeliveringDepository Depository does not match.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository does not match.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
does not match.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
does not match.
REGD RegistrationDetails Registration details linked to the
transaction are incorrect.
RTGS RTGSSystem Counterparty is for Real Time Gross
Settlement (RTGS) system, you are for
non-RTGS or vice versa.
SAFE SafekeepingAccount Safekeeping account used as matching
criteria on the market concerned does
not match. This includes Buyer/seller's
account, direct client's account at the
receiving/delivering agent, or receiving/
delivering agent's account at the CSD.
DMON SettlementAmount Settlement amount does not match.
SETS SettlementSystemMethod Settlement system/method does not
match (for example, instruction is to
settle using settlement system/method
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2179 March 2026
```

