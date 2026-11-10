---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "5.4 Message Building Blocks", "5.4.6 SupplementaryData <SplmtryData>"]
file_pages: [160, 161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5.4.6 SupplementaryData <SplmtryData>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 160 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 160

```text
TradeBeneficiaryParty <TradBnfcryPty> contains the following elements (see
"ConfirmationPartyDetails14" on page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  392
{Or     BIC <BIC> [1..1] IdentifierSet C3 393
Or     ProprietaryIdentification <PrtryId> [1..1] ± 393
Or}     NameAndAddress <NmAndAdr> [1..1]  394
       Name <Nm> [1..1] Text 394
       Address <Adr> [0..1]  394
         AddressType <AdrTp> [0..1] CodeSet 395
         AddressLine <AdrLine> [0..5] Text 395
         StreetName <StrtNm> [0..1] Text 395
         BuildingNumber <BldgNb> [0..1] Text 395
         PostCode <PstCd> [0..1] Text 396
         TownName <TwnNm> [0..1] Text 396
         CountrySubDivision <CtrySubDvsn> [0..1] Text 396
         Country <Ctry> [1..1] CodeSet C4 396
   SafekeepingAccount <SfkpgAcct> [0..1] ± 396
   CashDetails <CshDtls> [0..1] ± 396
   AlternateIdentification <AltrnId> [0..1] ± 397
   ProcessingIdentification <PrcgId> [0..1] Text 397
   AdditionalInformation <AddtlInf> [0..1] ± C1 397
   PartyCapacity <PtyCpcty> [0..1] ± 398
5.4.6 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C9 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 321
   Envelope <Envlp> [1..1] (External Schema) 322
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 160 February 2025
```

## File page 161

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 161 February 2025
```

