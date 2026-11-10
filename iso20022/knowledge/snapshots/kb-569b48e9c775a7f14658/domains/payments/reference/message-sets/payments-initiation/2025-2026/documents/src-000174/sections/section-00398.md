---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.9 Identification Information", "6.1.9.3 PaymentIdentification6", "6.1.9.3.2 EndToEndIdentification <EndToEndId>"]
file_pages: [549]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.9.3.2 EndToEndIdentification <EndToEndId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 549 to 549.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 549

```text
6.1.9.3.2  EndToEndIdentification <EndToEndId>
Presence: [1..1]
Definition: Unique identification assigned by the initiating party to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction. It can be included in several messages related to the transaction.
Datatype: "Max35Text" on page 609
6.1.9.3.3  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 605
6.1.10 Mandate
6.1.10.1  MandateClassification1Choice
Definition: Specifies the high level purpose of the instruction based on a set of pre-defined categories.
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 549
Or}   Proprietary <Prtry> [1..1] Text 549
6.1.10.1.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "MandateClassification1Code" on page 598
CodeName Name Definition
FIXE Fixed Direct debit amount is fixed.
USGB UsageBased Direct debit amount is based on usage.
VARI Variable Direct debit amount is variable.
6.1.10.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 549 March 2026
```

