---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.33 Postal Address", "66.1.33.8 PostalAddress6"]
file_pages: [5107]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.33.8 PostalAddress6

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5107 to 5107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5107

```text
ContactPerson <CtctPrsn> contains the following elements (see "ContactIdentification2" on
page 5095 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 5095
   GivenName <GvnNm> [0..1] Text 5095
   Name <Nm> [1..1] Text 5096
   PhoneNumber <PhneNb> [0..1] Text 5096
   MobileNumber <MobNb> [0..1] Text 5096
   FaxNumber <FaxNb> [0..1] Text 5096
   EmailAddress <EmailAdr> [0..1] Text 5096
66.1.33.8  PostalAddress6
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 5107
   Department <Dept> [0..1] Text 5108
   SubDepartment <SubDept> [0..1] Text 5108
   StreetName <StrtNm> [0..1] Text 5108
   BuildingNumber <BldgNb> [0..1] Text 5108
   PostCode <PstCd> [0..1] Text 5108
   TownName <TwnNm> [0..1] Text 5108
   CountrySubDivision <CtrySubDvsn> [0..1] Text 5108
   Country <Ctry> [0..1] CodeSet C12 5109
   AddressLine <AdrLine> [0..7] Text 5109
66.1.33.8.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 5276
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5107 May 2026
```

