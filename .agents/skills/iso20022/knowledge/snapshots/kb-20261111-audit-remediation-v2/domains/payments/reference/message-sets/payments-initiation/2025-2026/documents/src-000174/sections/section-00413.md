---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.13 Payment", "6.1.13.1 InstructionForCreditorAgent3", "6.1.13.1.2 InstructionInformation <InstrInf>"]
file_pages: [564]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.13.1.2 InstructionInformation <InstrInf>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 564 to 564.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 564

```text
6.1.13.1.2  InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Further information complementing the coded instruction or instruction to the creditor's agent
that is bilaterally agreed or specific to a user community.
Datatype: "Max140Text" on page 608
6.1.14 Payment Type
6.1.14.1  PaymentTypeInformation27
Definition: Provides further details of the type of payment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 564
   ClearingChannel <ClrChanl> [0..1] CodeSet 564
   ServiceLevel <SvcLvl> [0..*]  565
{Or     Code <Cd> [1..1] CodeSet 565
Or}     Proprietary <Prtry> [1..1] Text 565
   LocalInstrument <LclInstrm> [0..1]  565
{Or     Code <Cd> [1..1] CodeSet 566
Or}     Proprietary <Prtry> [1..1] Text 566
   SequenceType <SeqTp> [0..1] CodeSet 566
   CategoryPurpose <CtgyPurp> [0..1]  566
{Or     Code <Cd> [1..1] CodeSet 566
Or}     Proprietary <Prtry> [1..1] Text 567
6.1.14.1.1  InstructionPriority <InstrPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the instruction.
Datatype: "Priority2Code" on page 600
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
6.1.14.1.2  ClearingChannel <ClrChanl>
Presence: [0..1]
Definition: Specifies the clearing channel to be used to process the payment instruction.
Datatype: "ClearingChannel2Code" on page 590
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 564 March 2026
```

