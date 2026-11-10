---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.6 Pledgee3", "82.1.20.6.1 PledgeeTypeAndIdentification <PldgeeTpAndId>", "82.1.20.6.1.3 Proprietary <Prtry>"]
file_pages: [3066]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.6.1.3 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3066 to 3066.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3066

```text
82.1.20.6.1.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged expressed as a
proprietary type and narrative description.
Proprietary <Prtry> contains the following elements (see "GenericIdentification80" on page 2963 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 2963
   Identification <Id> [0..1] Text 2963
82.1.20.6.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 3322
82.1.20.7  PartyIdentification148
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3066
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3066
Or     NameAndAddress <NmAndAdr> [1..1] ± 3067
Or}     Country <Ctry> [1..1] CodeSet C3 3067
   LEI <LEI> [0..1] IdentifierSet 3067
   ProcessingIdentification <PrcgId> [0..1] Text 3067
82.1.20.7.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following PartyIdentification122Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3066
Or   NameAndAddress <NmAndAdr> [1..1] ± 3067
Or}   Country <Ctry> [1..1] CodeSet C3 3067
82.1.20.7.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3066 August 2026
```

