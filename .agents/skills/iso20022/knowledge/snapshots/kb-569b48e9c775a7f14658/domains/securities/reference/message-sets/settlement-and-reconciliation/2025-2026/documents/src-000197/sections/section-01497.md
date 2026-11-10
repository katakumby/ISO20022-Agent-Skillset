---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.74 CancellationReason20Choice", "35.1.29.74.2 Proprietary <Prtry>"]
file_pages: [1989, 1990]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.74.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1989 to 1990.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1989

```text
CodeName Name Definition
market infrastructure such as a stock
exchange.
CREG CancelledByIssuerRegistrar Transaction has been cancelled by the
issuer/registrar.
35.1.29.74.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.75  RepairReason11Choice
Definition: Choice of format for the repair reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1989
Or}   Proprietary <Prtry> [1..1] ± 1991
35.1.29.75.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RepairReason6Code" on page 2130
CodeName Name Definition
BATC ProcessingBatch Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
CAEV CorporateAction Corporate action pending on the
financial instrument instructed.
CASH CashAccount Unrecognised or invalid cash account.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
DDAT SettlementDate Unrecognised or invalid settlement date.
DDEA DealPrice Unrecognised or invalid deal price.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1989 March 2026
```

## File page 1990

```text
CodeName Name Definition
DMON SettlementAmount Unrecognised or invalid settlement
amount.
DQUA Quantity Unrecognised or invalid settlement
quantity.
DSEC Security Unrecognised or invalid financial
instrument identification.
DTRD TradeDate Unrecognised or invalid trade date.
IIND CommonReference Unrecognised, invalid or missing
common reference.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementQuantity Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NCRR SettlementAmountCurrency Unrecognised or invalid settlement
amount currency.
PHYS PhysicalSettlementImpossible Physical settlement is impossible for the
instructed financial instrument.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
REFE Reference Instruction has a reference identical to
another previously received instruction.
RTGS ImpossibleToUseTheRTGSSystemInstructed Impossible to use the RTGS system
instructed (NRTG or YRTG).
SAFE SafekeepingAccount Unrecognised or invalid message
sender's safekeeping account.
SETR SettlementTransaction Unrecognised or invalid settlement
transaction type.
SETS SettlementSystemMethod Unrecognised or invalid settlement
system/method instructed.
TXST TaxStatus Unrecognised or invalid tax status of the
securities instructed.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing Place
of Safekeeping.
SDUT StampDuty Required stamp duty information is
missing.
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
mismatch.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository mismatch.
DEPT ReceivingDeliveringDepository Depository mismatch.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
mismatch.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1990 March 2026
```

