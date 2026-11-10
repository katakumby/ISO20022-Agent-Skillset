---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.6 Pledgee3", "82.1.20.6.1 PledgeeTypeAndIdentification <PldgeeTpAndId>"]
file_pages: [3064]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.6.1 PledgeeTypeAndIdentification <PldgeeTpAndId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3064 to 3064.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3064

```text
Following Must be True
    /PledgeeTypeAndIdentification Must be present
 Or    /LEI Must be present
82.1.20.6.1  PledgeeTypeAndIdentification <PldgeeTpAndId>
Presence: [0..1]
Definition: Unique identification of the party.
PledgeeTypeAndIdentification <PldgeeTpAndId> contains one of the following
PledgeeFormat5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TypeAndIdentification <TpAndId> [1..1]  3064
     Identification <Id> [1..1] IdentifierSet C2 3064
     PledgeeType <PldgeeTp> [1..1] CodeSet 3065
Or   Identification <Id> [1..1]  3065
     Identification <Id> [0..1] Text 3065
     PledgeeType <PldgeeTp> [1..1] CodeSet 3065
Or}   Proprietary <Prtry> [1..1] ± 3066
82.1.20.6.1.1  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged expressed as a code
and a BIC.
TypeAndIdentification <TpAndId> contains the following PledgeeTypeAndAnyBICIdentifier2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet C2 3064
   PledgeeType <PldgeeTp> [1..1] CodeSet 3065
82.1.20.6.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged, expressed as a BIC.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3064 August 2026
```

