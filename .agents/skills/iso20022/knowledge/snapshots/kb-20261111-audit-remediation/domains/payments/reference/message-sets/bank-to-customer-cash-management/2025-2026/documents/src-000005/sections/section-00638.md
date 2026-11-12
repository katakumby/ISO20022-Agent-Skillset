---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Payment Type", "6.1.17.1 PaymentTypeInformation27", "6.1.17.1.5 SequenceType <SeqTp>"]
file_pages: [871]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17.1.5 SequenceType <SeqTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 871 to 871.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 871

```text
6.1.17.1.5  SequenceType <SeqTp>
Presence: [0..1]
Definition: Identifies the direct debit sequence, such as first, recurrent, final or one-off.
Datatype: "SequenceType3Code" on page 905
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
6.1.17.1.6  CategoryPurpose <CtgyPurp>
Presence: [0..1]
Definition: Specifies the high level purpose of the instruction based on a set of pre-defined categories.
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
CategoryPurpose <CtgyPurp> contains one of the following CategoryPurpose1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 871
Or}   Proprietary <Prtry> [1..1] Text 871
6.1.17.1.6.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 894
6.1.17.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
871 March 2026
```

