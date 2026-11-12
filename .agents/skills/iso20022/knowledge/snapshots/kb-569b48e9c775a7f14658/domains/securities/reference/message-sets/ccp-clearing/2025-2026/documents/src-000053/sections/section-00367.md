---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.16 Postal Address"]
file_pages: [460]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.16 Postal Address

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 460 to 460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 460

```text
12.1.16 Postal Address
12.1.16.1  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 460
   Address <Adr> [0..1] ± 460
12.1.16.1.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: Max350Text on page 493
12.1.16.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see PostalAddress1 on page 460 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 461
   AddressLine <AdrLine> [0..5] Text 461
   StreetName <StrtNm> [0..1] Text 461
   BuildingNumber <BldgNb> [0..1] Text 461
   PostCode <PstCd> [0..1] Text 462
   TownName <TwnNm> [0..1] Text 462
   CountrySubDivision <CtrySubDvsn> [0..1] Text 462
   Country <Ctry> [1..1] CodeSet   'C5 462
12.1.16.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 460
```

