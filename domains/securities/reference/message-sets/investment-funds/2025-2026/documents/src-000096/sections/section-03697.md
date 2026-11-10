---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.17 ContactAttributes6", "66.1.30.17.3 PhoneNumber <PhneNb>"]
file_pages: [4965]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.17.3 PhoneNumber <PhneNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4965 to 4965.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4965

```text
Definition: Address of the party.
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
66.1.30.17.3  PhoneNumber <PhneNb>
Presence: [0..1]
Definition: Phone number of the party.
Datatype: "PhoneNumber" on page 5405
66.1.30.17.4  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Fax number of the party.
Datatype: "PhoneNumber" on page 5405
66.1.30.17.5  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail) for the party.
Datatype: "Max256Text" on page 5403
66.1.30.17.6  URLAddress <URLAdr>
Presence: [0..1]
Definition: Address for the Universal Resource Locator (URL), for example, used over the www (HTTP)
service.
Datatype: "Max2048Text" on page 5403
66.1.30.17.7  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Identification of the party expressed as a BIC.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4965 May 2026
```

