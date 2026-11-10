---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Payment Type", "6.1.14.3 PaymentTypeInformation29", "6.1.14.3.3 LocalInstrument <LclInstrm>", "6.1.14.3.3.2 Proprietary <Prtry>"]
file_pages: [571]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.3.3.2 Proprietary <Prtry>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 571 to 571.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 571

```text
6.1.14.3.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the local instrument, as a proprietary code.
Datatype: "Max35Text" on page 609
6.1.14.3.4  SequenceType <SeqTp>
Presence: [0..1]
Definition: Identifies the direct debit sequence, such as first, recurrent, final or one-off.
Datatype: "SequenceType3Code" on page 601
CodeName Name Definition
FRST First First collection of a series of direct debit
instructions.
RCUR Recurring Direct debit instruction where the
debtor's authorisation is used for regular
direct debit transactions initiated by the
creditor.
FNAL Final Final collection of a series of direct debit
instructions.
OOFF OneOff Direct debit instruction where the
debtor's authorisation is used to initiate
one single direct debit transaction.
RPRE Represented Collection used to re-present previously
reversed or returned direct debit
transactions.
6.1.14.3.5  CategoryPurpose <CtgyPurp>
Presence: [0..1]
Definition: Specifies the high level purpose of the instruction based on a set of pre-defined categories.
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
CategoryPurpose <CtgyPurp> contains one of the following CategoryPurpose1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 571
Or}   Proprietary <Prtry> [1..1] Text 571
6.1.14.3.5.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 592
6.1.14.3.5.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 571 March 2026
```

