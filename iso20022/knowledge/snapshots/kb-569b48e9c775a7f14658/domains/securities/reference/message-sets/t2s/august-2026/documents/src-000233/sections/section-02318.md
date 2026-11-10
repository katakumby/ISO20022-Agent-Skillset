---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.6 PostalAddress3"]
file_pages: [3099]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.6 PostalAddress3

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3099 to 3099.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3099

```text
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
82.1.22.6  PostalAddress3
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [1..1] CodeSet 3099
   MailingIndicator <MlngInd> [1..1] Indicator 3099
   RegistrationAddressIndicator <RegnAdrInd> [1..1] Indicator 3100
   NameAndAddress <NmAndAdr> [1..1] ± 3100
Constraints
• MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
82.1.22.6.1  AddressType <AdrTp>
Presence: [1..1]
Definition: Type of address.
Datatype: "AddressType1Code" on page 3213
CodeName Name Definition
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
82.1.22.6.2  MailingIndicator <MlngInd>
Presence: [1..1]
Definition: Indicates whether mail should be sent to an address.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3099 August 2026
```

