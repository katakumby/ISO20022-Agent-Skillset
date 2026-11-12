---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.6 Person Identification", "11.1.6.1 Contact14", "11.1.6.1.14 ValidFrom <VldFr>"]
file_pages: [174]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.6.1.14 ValidFrom <VldFr>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 174 to 174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 174

```text
11.1.6.1.14  ValidFrom <VldFr>
Presence: [0..1]
Definition: Starting validity date for the contact.
Datatype: "ISODate" on page 184
11.1.6.1.15  ValidTo <VldTo>
Presence: [0..1]
Definition: Ending validity date for the contact.
Datatype: "ISODate" on page 184
11.1.7 Postal Address
11.1.7.1  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 174
   Address <Adr> [0..1] ± 174
11.1.7.1.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 187
11.1.7.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 179 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 179
   AddressLine <AdrLine> [0..5] Text 179
   StreetName <StrtNm> [0..1] Text 179
   BuildingNumber <BldgNb> [0..1] Text 180
   PostCode <PstCd> [0..1] Text 180
   TownName <TwnNm> [0..1] Text 180
   CountrySubDivision <CtrySubDvsn> [0..1] Text 180
   Country <Ctry> [1..1] CodeSet C2 180
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
174 March 2024
```

