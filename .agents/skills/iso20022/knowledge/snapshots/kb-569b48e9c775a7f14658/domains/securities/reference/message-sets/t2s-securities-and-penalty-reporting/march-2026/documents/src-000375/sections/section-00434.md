---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.83 TypeOfPrice14Code"]
file_pages: [548, 549]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.83 TypeOfPrice14Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 548 to 549.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 548

```text
CodeName Name Definition
offer price, which includes charges, will
be higher.
CANC Cancellation Price is the calculated cancellation price
of a dual-priced investment fund
(creation-cancellation price), and the
lowest possible valuation of the units on
any one-day. The actual selling or bid
price is usually higher.
INTE Interim Price is the non-official interim price
given to an investor before the executed
price.
SWNG Swing Price is the calculated net asset value
price of a single-priced investment fund.
The price is adjusted to take into account
the dealing costs due to individual large
deals, or due to a significant imbalance
in volumes of subscriptions vs
redemptions, as an alternative to dilution
levy.
MIDD Mid Price is the average price between the
bid and offer prices.
RINV Reinvestment Price is the price used when reinvesting
units after distribution.
SWIC Switch Price is the price used when transferring
units between products.
MRKT Market Price is the current market price.
INDC Indicative Price is the estimated indicative price.
7.2.2.83  TypeOfPrice14Code
Definition: Specifies the type of transaction price.
Type: CodeSet
CodeName Name Definition
AVER Average Price is an average execution price.
7.2.2.84  UnmatchedReason11Code
Definition: Specifies the reason the transaction, transfer or settlement instruction is unmatched.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
ACRU AccruedInterestAmount1 Accrued interest amount does not
match.
IIND CommonReference Common reference does not match.
CPCA CounterpartyCancelled Counterparty cancelled their instruction.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 548 March 2026
```

## File page 549

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 549 March 2026
```

