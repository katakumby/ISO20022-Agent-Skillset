---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Commission", "7.1.8.1 Commission25", "7.1.8.1.2 Commission <Comssn>"]
file_pages: [251]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.2 Commission <Comssn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 251 to 251.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 251

```text
7.1.8.1.2  Commission <Comssn>
Presence: [1..1]
Definition: Amount of money due to a party as compensation for a service.
Commission <Comssn> contains one of the following elements (see "AmountOrRate2Choice" on
page 245 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C9 245
Or}   Rate <Rate> [1..1] Rate 246
7.1.8.1.3  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Information related to an identification, eg, party identification or account identification.
RecipientIdentification <RcptId> contains the following PartyIdentification267 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BIC <BIC> [1..1] IdentifierSet C3 251
   ProprietaryIdentification <PrtryId> [1..1] ± 252
   NameAndAddress <NmAndAdr> [0..1]  252
     Name <Nm> [1..1] Text 252
     Address <Adr> [0..1]  253
       AddressType <AdrTp> [0..1] CodeSet 253
       AddressLine <AdrLine> [0..5] Text 253
       StreetName <StrtNm> [0..1] Text 253
       BuildingNumber <BldgNb> [0..1] Text 254
       PostCode <PstCd> [0..1] Text 254
       TownName <TwnNm> [0..1] Text 254
       CountrySubDivision <CtrySubDvsn> [0..1] Text 254
       Country <Ctry> [1..1] CodeSet C4 254
7.1.8.1.3.1  BIC <BIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 662
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 251 February 2025
```

