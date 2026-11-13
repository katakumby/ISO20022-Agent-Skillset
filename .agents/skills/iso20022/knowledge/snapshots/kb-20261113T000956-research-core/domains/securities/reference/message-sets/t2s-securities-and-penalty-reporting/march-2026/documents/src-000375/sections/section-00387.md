---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.11 MatchingStatus24Choice", "7.1.28.11.2 Unmatched <Umtchd>", "7.1.28.11.2.2 Reason <Rsn>", "7.1.28.11.2.2.1 Code <Cd>", "7.1.28.11.2.2.1.1 Code <Cd>"]
file_pages: [479, 480]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.11.2.2.1.1 Code <Cd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 479 to 480.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 479

```text
7.1.28.11.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Datatype: "UnmatchedReason11Code" on page 548
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
DMCT AutomaticGeneration Disagreement on automatic generation
of market claim or transformation.
DCMX CumEx Disagreement if trade was executed cum
or ex.
DSEC FinancialInstrument Financial instrument identification does
not match, for example, ISIN, financial
instrument attributes differs.
DQUA FinancialInstrumentQuantity Quantity of financial instruments does
not match.
INVE InvestorParty Investor party does not match.
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
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 479 March 2026
```

## File page 480

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 480 March 2026
```

