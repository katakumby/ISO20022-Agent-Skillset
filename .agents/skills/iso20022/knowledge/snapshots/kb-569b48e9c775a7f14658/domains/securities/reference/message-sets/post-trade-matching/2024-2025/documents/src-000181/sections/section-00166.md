---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.10 ConfirmationParties <ConfPties>", "6.4.10.13 TradeBeneficiaryParty <TradBnfcryPty>"]
file_pages: [210]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.10.13 TradeBeneficiaryParty <TradBnfcryPty>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 210 to 210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 210

```text
AffirmingParty <AffrmgPty> contains the following elements (see "ConfirmationPartyDetails14" on
page 392 for details)
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
6.4.10.13  TradeBeneficiaryParty <TradBnfcryPty>
Presence: [0..1]
Definition: Party involved in a legal proceeding, agreement, or other transaction.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 210 February 2025
```

