---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.87 UnmatchedReason4Code"]
file_pages: [659, 660, 661]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.87 UnmatchedReason4Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 659 to 661.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 659

```text
CodeName Name Definition
HECT Hectare Unit of measure that is equal to 10, 000
square meters.
ARES Are Unit of measure equal to a 100 square
meters.
SMET SquareMetre Measure of a surface, one metre by one
metre.
SCMT SquareCentimetre Measure of a surface, one centimetre by
one centimetre.
SMIL SquareMillimetre Measure of a surface, one millimetre by
one millimetre.
SQMI SquareMile Measure of a surface, one mile by one
mile.
SQYA SquareYard Measure of a surface, one yard by one
yard.
SQFO SquareFoot Measure of a surface, one foot by one
foot.
SQIN SquareInch Measure of a surface, one inch by one
inch.
ACRE Acre Unit of measure equal to 4, 840 square
yards.
7.2.2.87  UnmatchedReason4Code
Definition: Specifies the reason the transaction, transfer or settlement instruction is unmatched.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
CADE RepurchaseCallDelay Transaction call delay does not match.
CHAR ChargesAmount Charges amount does not match.
CMIS NoMatch A matching instruction from your
counterparty could not be found.
CPCA CounterpartyCancelled Counterparty cancelled their instruction.
DDAT SettlementDate Settlement date/time does not match.
DDEA DealPrice Deal price does not match.
DEAL TransactionDealAmount Deal amount does not match.
DELN TransactionDirection Direction of the trade does not match.
Counterparty expects a delivery from
you, not a receipt or vice versa.
DEPT ReceivingDeliveringDepository Depository does not match.
DMON SettlementAmount Settlement amount does not match.
DQUA FinancialInstrumentQuantity Quantity of financial instruments does
not match.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 659 February 2025
```

## File page 660

```text
CodeName Name Definition
DSEC FinancialInstrument Financial instrument identification does
not match, for example, ISIN, financial
instrument attributes differs.
DTRD TradeDate Trade date does not match.
EXEC ExecutionBrokerCommission Executing broker's commission does not
match.
FORF ForfeitRepurchaseAmount Forfeit amount does not match.
LATE MarketDeadlineMissed Your instruction was too late for
matching.
LEOG LetterOfGuarantee Counterparty is for settlement through
letter of guarantee, your instruction is
not, or vice versa.
MCAN MatchingRecordCancelled Corresponding matching record has
been cancelled.
NARR NarrativeReason See narrative field for the reason.
PHYS PhysicalSettlement Counterparty's instruction is physical
settlement, your instruction is not, or vice
versa.
PLCE PlaceOfTrade Place of trade does not match.
PODU PossibleDuplicate Instruction has not been matched. It is a
possible duplicate instruction.
REPA RepurchaseAmount Termination transaction amount does not
match.
REPO RepurchaseRate Repurchase rate does not match.
REPP RepurchasePremiumAmount Premium amount does not match.
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
SETR SettlementTransaction Settlement transaction type does not
match (relates to the settlement
transaction type codes available for field:
22F:: SETR.).
SETS SettlementSystemMethod Settlement system/method does not
match (for example, instruction is to
settle using settlement system/method
A. Counterparty expects settlement to
occur using settlement system/method
B).
TERM ClosingDateTime Closing date/time does not match.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 660 February 2025
```

## File page 661

```text
CodeName Name Definition
TXST TaxStatus Disagreement on the tax status of the
financial instruments to be settled.
VASU VariableRateSupport Variable rate support does not match
(repo).
POSE PositionEffect Position effect does not match.
BORT BorrowingRate Borrowing rate does not match.
COAX ConsumptionTax Consumption tax amount does not
match.
OTHI OtherFinancialInstrumentIdentification OtherIdentification of financial instrument
identification does not match.
BOFE BorrowingFee Borrowing fee does not match.
TACR AccruedInterestTax1 Accrued interest tax indicator does not
match.
SDAT SettlementDate2 Settlement date in the second leg does
not match.
COID CommonIdentification CommonIdentification does not match.
SCRA StandardCollateralRatio Standard collateral ratio does not match.
ACRU AccruedInterestAmount1 Accrued interest amount does not
match.
SHAI SecuritiesHaircut Securities haircut rate does not match.
ACRS AccruedInterestAmount2 Accrued interest amount in the second
leg does not match.
DEAS DealAmount2 Deal amount in the second leg does not
match.
CATI CallableTradeIndicator CallableTradeIndicator does not match.
TACS AccruedInterestTax2 Accrued interest tax indicator in the
second leg does not match.
DBNM StandingSettlementInstruction Counterparty's instruction is for
settlement through standing settlement
instruction, your instruction is not, or vice
versa.
MADA MaturityDate Maturity date does not match.
OLID ClientOrderLinkIdentification ClientOrderLinkIdentification does not
match.
TRSA ClosingSettlementAmount Closing settlement amount does not
match.
TRTE TypeOfFinancingClosing Type of financing closing does not
match.
BOIA BorrowingInterestAmount Borrowing interest amount does not
match.
OPLI OpeningLegIdentification OpeningLegIdentification does not
match.
TRTR TradeTransactionType Trade transaction type does not match.
LWCO LendingWithCollateral LendingWithCollateral does not match.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 661 February 2025
```

