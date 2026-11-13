---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.10 Mandate", "10.1.10.2 MandateTypeInformation2", "10.1.10.2.2 LocalInstrument <LclInstrm>", "10.1.10.2.2.1 Code <Cd>"]
file_pages: [1188]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.10.2.2.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1188 to 1188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1188

```text
LocalInstrument <LclInstrm> contains one of the following LocalInstrument2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1188
Or}   Proprietary <Prtry> [1..1] Text 1188
10.1.10.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the local instrument, as published in an external local instrument code list.
Datatype: "ExternalLocalInstrument1Code" on page 1230
10.1.10.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the local instrument, as a proprietary code.
Datatype: "Max35Text" on page 1246
10.1.10.2.3  CategoryPurpose <CtgyPurp>
Presence: [0..1]
Definition: Specifies the high level purpose of the mandate based on a set of pre-defined categories.
CategoryPurpose <CtgyPurp> contains one of the following CategoryPurpose1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1188
Or}   Proprietary <Prtry> [1..1] Text 1188
10.1.10.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 1228
10.1.10.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.10.2.4  Classification <Clssfctn>
Presence: [0..1]
Definition: Type of direct debit instruction.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1188 March 2026
```

