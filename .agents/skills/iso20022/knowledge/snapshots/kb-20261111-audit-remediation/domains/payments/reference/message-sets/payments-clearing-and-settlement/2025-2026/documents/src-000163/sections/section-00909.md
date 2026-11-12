---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.14 Payment Type", "10.1.14.1 PaymentTypeInformation28", "10.1.14.1.1 InstructionPriority <InstrPrty>"]
file_pages: [1204]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.14.1.1 InstructionPriority <InstrPrty>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1204 to 1204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 1204
   ClearingChannel <ClrChanl> [0..1] CodeSet 1204
   ServiceLevel <SvcLvl> [0..*]  1204
{Or     Code <Cd> [1..1] CodeSet 1205
Or}     Proprietary <Prtry> [1..1] Text 1205
   LocalInstrument <LclInstrm> [0..1]  1205
{Or     Code <Cd> [1..1] CodeSet 1205
Or}     Proprietary <Prtry> [1..1] Text 1205
   CategoryPurpose <CtgyPurp> [0..1]  1205
{Or     Code <Cd> [1..1] CodeSet 1206
Or}     Proprietary <Prtry> [1..1] Text 1206
10.1.14.1.1  InstructionPriority <InstrPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the instruction.
Datatype: "Priority2Code" on page 1236
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
10.1.14.1.2  ClearingChannel <ClrChanl>
Presence: [0..1]
Definition: Specifies the clearing channel to be used to process the payment instruction.
Datatype: "ClearingChannel2Code" on page 1226
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
10.1.14.1.3  ServiceLevel <SvcLvl>
Presence: [0..*]
Definition: Agreement under which or rules under which the transaction should be processed.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1204 March 2026
```

