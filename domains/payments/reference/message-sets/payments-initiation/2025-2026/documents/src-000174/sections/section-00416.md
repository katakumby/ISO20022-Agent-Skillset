---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Payment Type", "6.1.14.1 PaymentTypeInformation27", "6.1.14.1.6 CategoryPurpose <CtgyPurp>", "6.1.14.1.6.2 Proprietary <Prtry>"]
file_pages: [567]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.1.6.2 Proprietary <Prtry>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 567 to 567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 567

```text
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 592
6.1.14.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 609
6.1.14.2  PaymentTypeInformation26
Definition: Provides further details of the type of payment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 567
   ServiceLevel <SvcLvl> [0..*]  567
{Or     Code <Cd> [1..1] CodeSet 568
Or}     Proprietary <Prtry> [1..1] Text 568
   LocalInstrument <LclInstrm> [0..1]  568
{Or     Code <Cd> [1..1] CodeSet 568
Or}     Proprietary <Prtry> [1..1] Text 568
   CategoryPurpose <CtgyPurp> [0..1]  568
{Or     Code <Cd> [1..1] CodeSet 569
Or}     Proprietary <Prtry> [1..1] Text 569
6.1.14.2.1  InstructionPriority <InstrPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the instruction.
Datatype: "Priority2Code" on page 600
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
6.1.14.2.2  ServiceLevel <SvcLvl>
Presence: [0..*]
Definition: Agreement under which or rules under which the transaction should be processed.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 567 March 2026
```

