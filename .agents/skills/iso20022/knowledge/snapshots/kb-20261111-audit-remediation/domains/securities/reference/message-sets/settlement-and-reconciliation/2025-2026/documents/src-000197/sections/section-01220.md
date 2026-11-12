---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.10 Pledgee3", "35.1.18.10.1 PledgeeTypeAndIdentification <PldgeeTpAndId>", "35.1.18.10.1.2 Identification <Id>"]
file_pages: [1677]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.10.1.2 Identification <Id>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1677 to 1677.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1677

```text
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
35.1.18.10.1.2  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged, expressed as a
code and a narrative description.
Identification <Id> contains the following PledgeeTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 1677
   PledgeeType <PldgeeTp> [1..1] CodeSet 1677
35.1.18.10.1.2.1  Identification <Id>
Presence: [0..1]
Definition: Additional information about the entity to which the financial instruments are pledged.
Datatype: "Max35Text" on page 2192
35.1.18.10.1.2.2  PledgeeType <PldgeeTp>
Presence: [1..1]
Definition: Entity to which the financial instruments are pledged expressed as a code.
Datatype: "PledgeeType1Code" on page 2111
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
35.1.18.10.1.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged expressed as a
proprietary type and narrative description.
Proprietary <Prtry> contains the following elements (see "GenericIdentification80" on page 1486 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1487
   Identification <Id> [0..1] Text 1487
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1677 March 2026
```

