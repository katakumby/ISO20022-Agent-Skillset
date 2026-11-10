---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.29 ModificationCancellationAllowed <ModCxlAllwd>"]
file_pages: [582, 583, 584]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.29 ModificationCancellationAllowed <ModCxlAllwd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 582 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 582

```text
7.1.27.1.29  ModificationCancellationAllowed <ModCxlAllwd>
Presence: [0..1]
Definition: Specifies whether a third party is allowed to modify or cancel the transaction.
ModificationCancellationAllowed <ModCxlAllwd> contains one of the following elements (see
"ModificationCancellationAllowed4Choice" on page 335 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 335
Or}   Proprietary <Prtry> [1..1] ± 335
7.1.27.1.30  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.28 Status
7.1.28.1  UnmatchedReason32Choice
Definition: Choice of format for the statement query unmatched reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 582
Or}   Proprietary <Prtry> [1..1] ± 585
7.1.28.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Datatype: "UnmatchedReason4Code" on page 659
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
CADE RepurchaseCallDelay Transaction call delay does not match.
CHAR ChargesAmount Charges amount does not match.
CMIS NoMatch A matching instruction from your
counterparty could not be found.
CPCA CounterpartyCancelled Counterparty cancelled their instruction.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 582 February 2025
```

## File page 583

```text
CodeName Name Definition
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 583 February 2025
```

## File page 584

```text
CodeName Name Definition
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 584 February 2025
```

