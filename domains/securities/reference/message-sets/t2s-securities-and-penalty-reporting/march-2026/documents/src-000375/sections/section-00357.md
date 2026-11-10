---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.21 Postal Address", "7.1.21.3 NameAndAddress5", "7.1.21.3.2 Address <Adr>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.21.3.2 Address <Adr>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
7.1.21.3.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 442
   AddressLine <AdrLine> [0..5] Text 442
   StreetName <StrtNm> [0..1] Text 442
   BuildingNumber <BldgNb> [0..1] Text 442
   PostCode <PstCd> [0..1] Text 443
   TownName <TwnNm> [0..1] Text 443
   CountrySubDivision <CtrySubDvsn> [0..1] Text 443
   Country <Ctry> [1..1] CodeSet C3 443
7.1.22 Price
7.1.22.1  Price7
Definition: Type and information about a price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
7.1.22.1.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the price type.
Type <Tp> contains one of the following elements (see "YieldedOrValueType1Choice" on page 385 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 385
Or}   ValueType <ValTp> [1..1] CodeSet 385
7.1.22.1.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 444 March 2026
```

