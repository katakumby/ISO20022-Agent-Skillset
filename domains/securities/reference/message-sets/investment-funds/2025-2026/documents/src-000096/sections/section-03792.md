---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.6 IndividualPerson8", "66.1.32.6.4 NameSuffix <NmSfx>"]
file_pages: [5080]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.6.4 NameSuffix <NmSfx>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5080 to 5080.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5080

```text
66.1.32.6.4  NameSuffix <NmSfx>
Presence: [0..1]
Definition: Additional information about a person that follows a person's name, for example, qualification
such as Doctor of Philosophy (PhD).
Datatype: "Max35Text" on page 5403
66.1.32.6.5  Gender <Gndr>
Presence: [0..1]
Definition: Specifies the gender of the person.
Datatype: "GenderCode" on page 5308
CodeName Name Definition
MALE Male Individual is a male.
FEMA Female Individual is a female.
66.1.32.6.6  BirthDate <BirthDt>
Presence: [0..1]
Definition: Date on which a person is born.
Datatype: "ISODate" on page 5388
66.1.32.6.7  SocialSecurityNumber <SclSctyNb>
Presence: [0..1]
Definition: Number assigned by a social security agency.
Datatype: "Max35Text" on page 5403
66.1.32.6.8  IndividualInvestorAddress <IndvInvstrAdr>
Presence: [1..1]
Definition: Postal address of a party.
IndividualInvestorAddress <IndvInvstrAdr> contains the following elements (see "PostalAddress1"
on page 5098 for details)
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5080 May 2026
```

