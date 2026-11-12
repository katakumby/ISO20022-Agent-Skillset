---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.6 Postal Address", "11.1.6.2 PostalAddress1", "11.1.6.2.2 AddressLine <AdrLine>"]
file_pages: [93]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.6.2.2 AddressLine <AdrLine>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 93 to 93.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 93

```text
CodeName Name Definition
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
11.1.6.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max70Text" on page 100
11.1.6.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max70Text" on page 100
11.1.6.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Datatype: "Max16Text" on page 99
11.1.6.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 99
11.1.6.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 100
11.1.6.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 100
11.1.6.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 93 December 2019
```

