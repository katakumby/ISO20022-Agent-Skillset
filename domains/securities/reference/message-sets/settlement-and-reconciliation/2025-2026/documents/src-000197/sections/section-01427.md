---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.5 CorporateActionEventStage <CorpActnEvtStag>", "35.1.29.22.5.2 Proprietary <Prtry>"]
file_pages: [1910, 1911]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.5.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1910 to 1911.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1910

```text
CodeName Name Definition
LAPS Lapsed The event/offer conditions have not been
met and the event/offer is terminated or
lapsed.
35.1.29.22.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Corporate action event stage expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.6  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [1..1]
Definition: Provides the matching status of an instruction as known by the account servicer based on an
allegement. At this time no matching took place on the market (at the CSD/ICSD).
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus27Choice" on page 1924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1924
Or}   Proprietary <Prtry> [1..1] ± 1925
35.1.29.22.7  InstructionProcessingStatus <InstrPrcgSts>
Presence: [1..1]
Definition: Provides the status of an instruction.
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus23Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1910
Or}   Proprietary <Prtry> [1..1] ± 1912
35.1.29.22.7.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of an instruction.
Datatype: "InstructionProcessingStatus1Code" on page 2080
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1910 March 2026
```

## File page 1911

```text
CodeName Name Definition
CAN1 Cancellation1 Pending cancellation; only one side has
been input and a cancellation request
has been sent.
CAN2 Cancellation2 Pending cancellation; both sides have
been input, the trade has not yet been
matched, and one side has sent a
cancellation request.
CAN3 Cancellation3 Pending cancellation; both sides have
been input, the trade is matched, and
one side has sent a cancellation request.
CAND Cancelled Instruction has been cancelled.
CANO CancelledByAnotherParty Instruction has been cancelled by
another party than the instructing party,
for example, market infrastructure such
as a stock exchange.
CANP PendingCancellation Cancellation request from yourself for
this instruction is pending waiting for
further processing.
CGEN Generated Account servicer or third party created
the transaction. It was not instructed
directly by the account owner.
COSE FullyExecutedConfirmationSent Order is fully executed and the
confirmation was sent.
CPRC CancellationRequested Cancellation request from the
counterparty is awaiting for your
cancellation request or your consent.
DFLA DefaultAction Default action is taken.
DONE Done Order is partially filled and no further
executions forthcoming for the trading
day.
DONF PartiallyFilledOrder Order is partially filled and no further
executions will take place.
EXCH ReceivedAtStockExchange Order has been received at the stock
exchange.
EXSE FullyExecutedExecutionSent Order was fully executed and the
execution sent.
FORC ForcedRejection Message has been sent automatically by
the service provider to notify that
settlement will not take place.
FUTU Future All checks relative to the instruction
(except collateral) are successful.
INTE ReceivedAtIntermediary Order has been received at the
intermediary.
NOTC AlreadyMatchedAndAffirmed Instruction cannot be cancelled as it has
already been matched and affirmed.
OPOD OpenOrder Order is open.
OVER OverAllocated Quantity of financial instrument of the
block trade has been overallocated.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1911 March 2026
```

