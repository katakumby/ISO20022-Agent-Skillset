---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.2 NewPaymentValueSet <NewPmtValSet>", "6.4.2.2.3 Priority <Prty>"]
file_pages: [345]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.2.3 Priority <Prty>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 345 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 345

```text
6.4.2.2.3  Priority <Prty>
Presence: [0..1]
Definition: Urgency or order of importance that the originator would like the recipient of the payment
instruction to apply to the processing of the payment instruction.
.
Priority <Prty> contains one of the following Priority1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 345
Or}   Proprietary <Prtry> [1..1] Text 345
6.4.2.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Priority code, in a coded form.
Datatype: "Priority5Code" on page 871
CodeName Name Definition
HIGH High Priority level is high.
LOWW Low Priority level is low.
NORM Normal Priority level is normal.
URGT Urgent Priority level is urgent (highest priority
possible).
6.4.2.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Priority code bilaterally agreed between parties.
Datatype: "Max35Text" on page 889
6.4.2.2.4  ProcessingValidityTime <PrcgVldtyTm>
Presence: [0..1]
Definition: Date and time range within which the payment instruction must be processed.
.
ProcessingValidityTime <PrcgVldtyTm> contains one of the following DateTimePeriod1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 346
Or   ToDateTime <ToDtTm> [1..1] DateTime 346
Or}   DateTimeRange <DtTmRg> [1..1] ± 346
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 345 February 2025
```

