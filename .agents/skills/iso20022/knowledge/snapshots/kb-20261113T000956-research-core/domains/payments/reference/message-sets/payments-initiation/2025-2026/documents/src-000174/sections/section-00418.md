---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Payment Type", "6.1.14.2 PaymentTypeInformation26", "6.1.14.2.4 CategoryPurpose <CtgyPurp>", "6.1.14.2.4.1 Code <Cd>"]
file_pages: [569]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.2.4.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 569 to 569.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 569

```text
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
CategoryPurpose <CtgyPurp> contains one of the following CategoryPurpose1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 569
Or}   Proprietary <Prtry> [1..1] Text 569
6.1.14.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 592
6.1.14.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 609
6.1.14.3  PaymentTypeInformation29
Definition: Provides further details of the type of payment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 569
   ServiceLevel <SvcLvl> [0..*]  570
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] Text 570
   LocalInstrument <LclInstrm> [0..1]  570
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] Text 571
   SequenceType <SeqTp> [0..1] CodeSet 571
   CategoryPurpose <CtgyPurp> [0..1]  571
{Or     Code <Cd> [1..1] CodeSet 571
Or}     Proprietary <Prtry> [1..1] Text 571
6.1.14.3.1  InstructionPriority <InstrPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the instruction.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 569 March 2026
```

