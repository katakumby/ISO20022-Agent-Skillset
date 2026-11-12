---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.9 Postal Address", "4.1.9.1 NameAndAddress5", "4.1.9.1.2 Address <Adr>"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.9.1.2 Address <Adr>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
4.1.9.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 69 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 70
   AddressLine <AdrLine> [0..5] Text 70
   StreetName <StrtNm> [0..1] Text 70
   BuildingNumber <BldgNb> [0..1] Text 70
   PostCode <PstCd> [0..1] Text 71
   TownName <TwnNm> [0..1] Text 71
   CountrySubDivision <CtrySubDvsn> [0..1] Text 71
   Country <Ctry> [1..1] CodeSet C5 71
4.1.9.2  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
65 March 2024
```

