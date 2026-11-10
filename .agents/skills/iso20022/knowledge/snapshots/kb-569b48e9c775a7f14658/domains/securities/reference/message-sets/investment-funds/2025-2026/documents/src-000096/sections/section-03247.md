---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.17 Financial Institution Identification", "66.1.17.3 BranchData2"]
file_pages: [4483]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.17.3 BranchData2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4483 to 4483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4483

```text
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress1" on page 5098 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 5098
   AddressLine <AdrLine> [0..5] Text 5099
   StreetName <StrtNm> [0..1] Text 5099
   BuildingNumber <BldgNb> [0..1] Text 5099
   PostCode <PstCd> [0..1] Text 5099
   TownName <TwnNm> [0..1] Text 5099
   CountrySubDivision <CtrySubDvsn> [0..1] Text 5099
   Country <Ctry> [1..1] CodeSet C12 5100
66.1.17.3  BranchData2
Definition: Information that locates and identifies a specific branch of a financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4483
   Name <Nm> [0..1] Text 4483
   PostalAddress <PstlAdr> [0..1] ± 4483
66.1.17.3.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a branch of a financial institution.
Datatype: "Max35Text" on page 5403
66.1.17.3.2  Name <Nm>
Presence: [0..1]
Definition: Name by which an agent is known and which is usually used to identify that agent.
Datatype: "Max140Text" on page 5402
66.1.17.3.3  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4483 May 2026
```

