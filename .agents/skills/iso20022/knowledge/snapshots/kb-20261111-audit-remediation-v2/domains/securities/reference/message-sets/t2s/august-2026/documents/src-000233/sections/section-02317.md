---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.4 NameAndAddress4", "82.1.22.4.1 Name <Nm>"]
file_pages: [3098]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.4.1 Name <Nm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3098 to 3098.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3098

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 3098
   Address <Adr> [1..1] ± 3098
82.1.22.4.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 3328
82.1.22.4.2  Address <Adr>
Presence: [1..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 3091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 3092
   AddressLine <AdrLine> [0..5] Text 3092
   StreetName <StrtNm> [0..1] Text 3092
   BuildingNumber <BldgNb> [0..1] Text 3092
   PostCode <PstCd> [0..1] Text 3093
   TownName <TwnNm> [0..1] Text 3093
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3093
   Country <Ctry> [1..1] CodeSet C3 3093
82.1.22.5  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 3098
   Address <Adr> [0..1] ± 3098
82.1.22.5.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 3328
82.1.22.5.2  Address <Adr>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3098 August 2026
```

