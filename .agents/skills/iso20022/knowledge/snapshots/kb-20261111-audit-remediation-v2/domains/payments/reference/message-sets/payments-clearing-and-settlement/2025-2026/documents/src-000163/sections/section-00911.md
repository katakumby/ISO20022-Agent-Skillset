---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.14 Payment Type", "10.1.14.1 PaymentTypeInformation28", "10.1.14.1.5 CategoryPurpose <CtgyPurp>", "10.1.14.1.5.1 Code <Cd>"]
file_pages: [1206]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.14.1.5.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1206 to 1206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1206

```text
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
CategoryPurpose <CtgyPurp> contains one of the following CategoryPurpose1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1206
Or}   Proprietary <Prtry> [1..1] Text 1206
10.1.14.1.5.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 1228
10.1.14.1.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.14.2  PaymentTypeInformation27
Definition: Provides further details of the type of payment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 1206
   ClearingChannel <ClrChanl> [0..1] CodeSet 1207
   ServiceLevel <SvcLvl> [0..*]  1207
{Or     Code <Cd> [1..1] CodeSet 1207
Or}     Proprietary <Prtry> [1..1] Text 1207
   LocalInstrument <LclInstrm> [0..1]  1208
{Or     Code <Cd> [1..1] CodeSet 1208
Or}     Proprietary <Prtry> [1..1] Text 1208
   SequenceType <SeqTp> [0..1] CodeSet 1208
   CategoryPurpose <CtgyPurp> [0..1]  1208
{Or     Code <Cd> [1..1] CodeSet 1209
Or}     Proprietary <Prtry> [1..1] Text 1209
10.1.14.2.1  InstructionPriority <InstrPrty>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1206 March 2026
```

