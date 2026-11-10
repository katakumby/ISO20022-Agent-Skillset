---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.4 Message Building Blocks", "2.4.4 Investor <Invstr>"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.4.4 Investor <Invstr>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

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
2.4.4 Investor <Invstr>
Presence: [0..*]
Definition: Party that identifies the underlying investor.
Impacted by: C6 "IdentificationUsageRule"
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 25 February 2025
```

