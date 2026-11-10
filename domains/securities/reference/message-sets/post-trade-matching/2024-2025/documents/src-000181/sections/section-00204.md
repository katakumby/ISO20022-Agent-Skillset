---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Commission", "7.1.8.3 Commission24", "7.1.8.3.3 RecipientIdentification <RcptId>"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.3.3 RecipientIdentification <RcptId>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
Commission <Comssn> contains one of the following elements (see "AmountOrRate2Choice" on
page 245 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C9 245
Or}   Rate <Rate> [1..1] Rate 246
7.1.8.3.3  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Information related to an identification, eg, party identification or account identification.
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification117" on
page 471 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 472
   ProprietaryIdentification <PrtryId> [1..1] ± 472
   NameAndAddress <NmAndAdr> [0..1]  472
     Name <Nm> [1..1] Text 473
     Address <Adr> [0..1]  473
       AddressType <AdrTp> [0..1] CodeSet 473
       AddressLine <AdrLine> [0..5] Text 474
       StreetName <StrtNm> [0..1] Text 474
       BuildingNumber <BldgNb> [0..1] Text 474
       PostCode <PstCd> [0..1] Text 474
       TownName <TwnNm> [0..1] Text 474
       CountrySubDivision <CtrySubDvsn> [0..1] Text 474
       Country <Ctry> [1..1] CodeSet C4 475
7.1.8.3.4  CalculationDate <ClctnDt>
Presence: [0..1]
Definition: Date at which an operation is triggered to calculate, for instance, a commission, fee, asset
values, etc.
Datatype: "ISODate" on page 662
7.1.8.3.5  TotalCommission <TtlComssn>
Presence: [0..1]
Definition: Total value of the commissions for a specific trade.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 258 February 2025
```

