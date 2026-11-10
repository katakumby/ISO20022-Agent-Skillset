---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.170 UnmatchedReason14Code"]
file_pages: [2182, 2183, 2184]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.170 UnmatchedReason14Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2182 to 2184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2182

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
VASU VariableRateSupport Variable rate support does not match
(repo).
DMCT AutomaticGeneration Disagreement on automatic generation
of market claim or transformation.
DCMX CumEx Disagreement if trade was executed cum
or ex.
35.2.2.170  UnmatchedReason14Code
Definition: Specifies the reason the transaction, transfer or settlement instruction is unmatched.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
ACRU AccruedInterestAmount1 Accrued interest amount does not
match.
CHAR ChargesAmount Charges amount does not match.
TERM ClosingDateTime Closing date/time does not match.
IIND CommonReference Common reference does not match.
CPCA CounterpartyCancelled Counterparty cancelled their instruction.
CLAT CounterpartyTooLateForMatching Counterparty's instruction was too late
for matching.
NCRR CurrencySettlementAmount Settlement amount currency does not
match.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2182 March 2026
```

## File page 2183

```text
CodeName Name Definition
DDEA DealPrice Deal price does not match.
EXEC ExecutionBrokerCommission Executing broker's commission does not
match.
DSEC FinancialInstrument Financial instrument identification does
not match, for example, ISIN, financial
instrument attributes differs.
DQUA FinancialInstrumentQuantity Quantity of financial instruments does
not match.
FORF ForfeitRepurchaseAmount Forfeit amount does not match.
LEOG LetterOfGuarantee Counterparty is for settlement through
letter of guarantee, your instruction is
not, or vice versa.
INVE InvestorParty Investor party does not match.
LATE MarketDeadlineMissed Your instruction was too late for
matching.
MCAN MatchingRecordCancelled Corresponding matching record has
been cancelled.
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
PLIS PlaceOfListing Place of listing does not match.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2183 March 2026
```

## File page 2184

```text
CodeName Name Definition
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
does not match.
REGD RegistrationDetails Registration details linked to the
transaction are incorrect.
REPA RepurchaseAmount Termination transaction amount does not
match.
CADE RepurchaseCallDelay Transaction call delay does not match.
REPP RepurchasePremiumAmount Premium amount does not match.
REPO RepurchaseRate Repurchase rate does not match.
RERT RepurchaseRateType Repurchase rate type does not match.
RSPR RepurchaseSpreadRate Spread rate does not match.
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
DEAL TransactionDealAmount Deal amount does not match.
DELN TransactionDirection Direction of the trade does not match.
Counterparty expects a delivery from
you, not a receipt or vice versa.
UNBR UnmatchedMarketSide Market side trade is unmatched.
VASU VariableRateSupport Variable rate support does not match
(repo).
DCMX CumEx Disagreement if trade was executed cum
or ex.
DMCT AutomaticGeneration Disagreement on automatic generation
of market claim or transformation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2184 March 2026
```

