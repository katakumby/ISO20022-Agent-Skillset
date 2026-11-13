---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.86 RepairStatus12Choice", "35.1.29.86.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [2011, 2012]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.86.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2011 to 2012.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2011

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2011
Or}   Reason <Rsn> [1..*]  2011
     Code <Cd> [1..1]  2011
{Or       Code <Cd> [1..1] CodeSet 2011
Or}       Proprietary <Prtry> [1..1] ± 2013
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2013
35.1.29.86.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.86.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the repair status.
Reason <Rsn> contains the following RepairReason8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2011
{Or     Code <Cd> [1..1] CodeSet 2011
Or}     Proprietary <Prtry> [1..1] ± 2013
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2013
35.1.29.86.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RepairReason10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2011
Or}   Proprietary <Prtry> [1..1] ± 2013
35.1.29.86.2.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2011 March 2026
```

## File page 2012

```text
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RepairReason4Code" on page 2127
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2012 March 2026
```

