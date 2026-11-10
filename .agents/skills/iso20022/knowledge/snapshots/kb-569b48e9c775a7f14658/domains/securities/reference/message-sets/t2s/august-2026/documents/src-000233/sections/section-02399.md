---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.44 RepairStatus12Choice", "82.1.30.44.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [3189, 3190]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.44.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3189 to 3190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3189

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3189
Or}   Reason <Rsn> [1..*]  3189
     Code <Cd> [1..1]  3189
{Or       Code <Cd> [1..1] CodeSet 3189
Or}       Proprietary <Prtry> [1..1] ± 3191
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3191
82.1.30.44.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.44.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the repair status.
Reason <Rsn> contains the following RepairReason8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3189
{Or     Code <Cd> [1..1] CodeSet 3189
Or}     Proprietary <Prtry> [1..1] ± 3191
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3191
82.1.30.44.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RepairReason10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3189
Or}   Proprietary <Prtry> [1..1] ± 3191
82.1.30.44.2.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3189 August 2026
```

## File page 3190

```text
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RepairReason4Code" on page 3285
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3190 August 2026
```

