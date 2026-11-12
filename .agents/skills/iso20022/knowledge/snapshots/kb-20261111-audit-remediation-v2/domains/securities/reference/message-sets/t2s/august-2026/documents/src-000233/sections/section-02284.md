---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.6 Pledgee3", "82.1.20.6.1 PledgeeTypeAndIdentification <PldgeeTpAndId>", "82.1.20.6.1.1 TypeAndIdentification <TpAndId>", "82.1.20.6.1.1.2 PledgeeType <PldgeeTp>"]
file_pages: [3065]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.6.1.1.2 PledgeeType <PldgeeTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3065 to 3065.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3065

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
82.1.20.6.1.1.2  PledgeeType <PldgeeTp>
Presence: [1..1]
Definition: Entity to which the financial instruments are pledged expressed as a code.
Datatype: "PledgeeType1Code" on page 3280
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
82.1.20.6.1.2  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged, expressed as a
code and a narrative description.
Identification <Id> contains the following PledgeeTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 3065
   PledgeeType <PldgeeTp> [1..1] CodeSet 3065
82.1.20.6.1.2.1  Identification <Id>
Presence: [0..1]
Definition: Additional information about the entity to which the financial instruments are pledged.
Datatype: "Max35Text" on page 3328
82.1.20.6.1.2.2  PledgeeType <PldgeeTp>
Presence: [1..1]
Definition: Entity to which the financial instruments are pledged expressed as a code.
Datatype: "PledgeeType1Code" on page 3280
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3065 August 2026
```

