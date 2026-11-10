---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.10 ConfirmationParties <ConfPties>", "6.4.10.10 ClearingFirm <ClrFirm>"]
file_pages: [207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.10.10 ClearingFirm <ClrFirm>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 207 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 207

```text
StepOutFirm <StepOutFirm> contains the following elements (see "ConfirmationPartyDetails11" on
page 465 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  466
{Or     BIC <BIC> [1..1] IdentifierSet C3 467
Or     ProprietaryIdentification <PrtryId> [1..1] ± 467
Or}     NameAndAddress <NmAndAdr> [1..1]  468
       Name <Nm> [1..1] Text 468
       Address <Adr> [0..1]  468
         AddressType <AdrTp> [0..1] CodeSet 469
         AddressLine <AdrLine> [0..5] Text 469
         StreetName <StrtNm> [0..1] Text 469
         BuildingNumber <BldgNb> [0..1] Text 469
         PostCode <PstCd> [0..1] Text 470
         TownName <TwnNm> [0..1] Text 470
         CountrySubDivision <CtrySubDvsn> [0..1] Text 470
         Country <Ctry> [1..1] CodeSet C4 470
   AlternateIdentification <AltrnId> [0..1] ± 470
   ProcessingIdentification <PrcgId> [0..1] Text 470
   AdditionalInformation <AddtlInf> [0..1] ± C1 471
6.4.10.10  ClearingFirm <ClrFirm>
Presence: [0..1]
Definition: Party, also know as take up broker, that settles security transactions from another broker for
a fee.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 207 February 2025
```

