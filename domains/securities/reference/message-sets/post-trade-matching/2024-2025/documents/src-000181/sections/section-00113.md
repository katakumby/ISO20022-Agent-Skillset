---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "4.4 Message Building Blocks", "4.4.4 SupplementaryData <SplmtryData>"]
file_pages: [146, 147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4.4.4 SupplementaryData <SplmtryData>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 146 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
Definition: Foreign Financial Institution which has been authorised by local authorities to act as account
management institution in the country.
QualifiedForeignIntermediary <QlfdFrgnIntrmy> contains the following elements (see
"PartyIdentificationAndAccount221" on page 498 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  498
{Or     BIC <BIC> [1..1] IdentifierSet C3 499
Or     ProprietaryIdentification <PrtryId> [1..1] ± 499
Or}     NameAndAddress <NmAndAdr> [1..1]  500
       Name <Nm> [1..1] Text 500
       Address <Adr> [0..1]  500
         AddressType <AdrTp> [0..1] CodeSet 501
         AddressLine <AdrLine> [0..5] Text 501
         StreetName <StrtNm> [0..1] Text 501
         BuildingNumber <BldgNb> [0..1] Text 501
         PostCode <PstCd> [0..1] Text 502
         TownName <TwnNm> [0..1] Text 502
         CountrySubDivision <CtrySubDvsn> [0..1] Text 502
         Country <Ctry> [1..1] CodeSet C4 502
   AlternateIdentification <AltrnId> [0..1] ± 502
   SafekeepingAccount <SfkpgAcct> [0..1] Text 502
   ProcessingIdentification <PrcgId> [0..1] Text 503
   AdditionalInformation <AddtlInf> [0..1] ± C2 503
4.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 321
   Envelope <Envlp> [1..1] (External Schema) 322
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 146 February 2025
```

## File page 147

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 147 February 2025
```

