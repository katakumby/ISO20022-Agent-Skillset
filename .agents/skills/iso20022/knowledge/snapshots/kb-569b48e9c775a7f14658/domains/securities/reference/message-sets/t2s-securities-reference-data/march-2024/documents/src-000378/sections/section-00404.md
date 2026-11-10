---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.13 Price"]
file_pages: [497]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.13 Price

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 497 to 497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 497

```text
Address <Adr> contains the following elements (see "PostalAddress1" on page 493 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 494
   AddressLine <AdrLine> [0..5] Text 494
   StreetName <StrtNm> [0..1] Text 494
   BuildingNumber <BldgNb> [0..1] Text 494
   PostCode <PstCd> [0..1] Text 495
   TownName <TwnNm> [0..1] Text 495
   CountrySubDivision <CtrySubDvsn> [0..1] Text 495
   Country <Ctry> [1..1] CodeSet C4 495
13.1.13 Price
13.1.13.1  PriceRateOrAmount3Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 497
Or}   Amount <Amt> [1..1] Amount C2 497
13.1.13.1.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Datatype: "PercentageRate" on page 532
13.1.13.1.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 507
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 497 March 2024
```

