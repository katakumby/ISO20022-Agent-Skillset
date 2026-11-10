---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.6 Pledgee3", "7.1.19.6.1 PledgeeTypeAndIdentification <PldgeeTpAndId>", "7.1.19.6.1.2 Identification <Id>"]
file_pages: [419]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.6.1.2 Identification <Id>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 419 to 419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 419

```text
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
7.1.19.6.1.2  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged, expressed as a
code and a narrative description.
Identification <Id> contains the following PledgeeTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 419
   PledgeeType <PldgeeTp> [1..1] CodeSet 419
7.1.19.6.1.2.1  Identification <Id>
Presence: [0..1]
Definition: Additional information about the entity to which the financial instruments are pledged.
Datatype: "Max35Text" on page 557
7.1.19.6.1.2.2  PledgeeType <PldgeeTp>
Presence: [1..1]
Definition: Entity to which the financial instruments are pledged expressed as a code.
Datatype: "PledgeeType1Code" on page 525
CodeName Name Definition
CPTY Counterparty Financial instruments are pledged to a
counterparty.
REGB RegulatoryBody Financial instruments are pledged to a
regulatory body.
7.1.19.6.1.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged expressed as a
proprietary type and narrative description.
Proprietary <Prtry> contains the following elements (see "GenericIdentification80" on page 349 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 349
   Identification <Id> [0..1] Text 349
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 419 March 2026
```

