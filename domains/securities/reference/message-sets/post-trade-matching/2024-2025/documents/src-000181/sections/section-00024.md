---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.4 Message Building Blocks", "2.4.5 SupplementaryData <SplmtryData>"]
file_pages: [26, 27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.4.5 SupplementaryData <SplmtryData>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 26 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount220" on
page 484 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  485
{Or     BIC <BIC> [1..1] IdentifierSet C3 486
Or     ProprietaryIdentification <PrtryId> [1..1] ± 486
Or}     NameAndAddress <NmAndAdr> [1..1]  487
       Name <Nm> [1..1] Text 487
       Address <Adr> [0..1]  487
         AddressType <AdrTp> [0..1] CodeSet 488
         AddressLine <AdrLine> [0..5] Text 488
         StreetName <StrtNm> [0..1] Text 488
         BuildingNumber <BldgNb> [0..1] Text 488
         PostCode <PstCd> [0..1] Text 489
         TownName <TwnNm> [0..1] Text 489
         CountrySubDivision <CtrySubDvsn> [0..1] Text 489
         Country <Ctry> [1..1] CodeSet C4 489
   SafekeepingAccount <SfkpgAcct> [0..1] Text 489
   CashAccount <CshAcct> [0..1] ± 489
   ProcessingIdentification <PrcgId> [0..1] Text 490
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C4 490
   AdditionalInformation <AddtlInf> [0..1] ± C2 490
   AlternateIdentification <AltrnId> [0..1] ± 491
Constraints
• IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
2.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C7 "SupplementaryDataRule"
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 26 February 2025
```

## File page 27

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 321
   Envelope <Envlp> [1..1] (External Schema) 322
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 27 February 2025
```

