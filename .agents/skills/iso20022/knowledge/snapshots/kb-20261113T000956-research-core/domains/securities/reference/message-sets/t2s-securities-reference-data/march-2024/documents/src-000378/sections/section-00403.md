---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.12 Postal Address", "13.1.12.4 NameAndAddress5", "13.1.12.4.2 Address <Adr>"]
file_pages: [496]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.12.4.2 Address <Adr>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 496 to 496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 496

```text
13.1.12.4.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 493 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 494
   AddressLine <AdrLine> [0..5] Text 494
   StreetName <StrtNm> [0..1] Text 494
   BuildingNumber <BldgNb> [0..1] Text 494
   PostCode <PstCd> [0..1] Text 495
   TownName <TwnNm> [0..1] Text 495
   CountrySubDivision <CtrySubDvsn> [0..1] Text 495
   Country <Ctry> [1..1] CodeSet C4 495
13.1.12.5  NameAndAddress4
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 496
   Address <Adr> [1..1] ± 496
13.1.12.5.1  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 534
13.1.12.5.2  Address <Adr>
Presence: [1..1]
Definition: Postal address of the party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 496 March 2024
```

