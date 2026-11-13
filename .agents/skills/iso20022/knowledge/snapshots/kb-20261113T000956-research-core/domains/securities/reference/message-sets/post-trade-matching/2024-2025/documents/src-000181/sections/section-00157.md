---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.10 ConfirmationParties <ConfPties>", "6.4.10.4 Seller <Sellr>"]
file_pages: [201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.10.4 Seller <Sellr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 201 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
Borrower <Brrwr> contains the following elements (see "ConfirmationPartyDetails12" on page 426 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  427
{Or     BIC <BIC> [1..1] IdentifierSet C3 427
Or     ProprietaryIdentification <PrtryId> [1..1] ± 427
Or}     NameAndAddress <NmAndAdr> [1..1]  428
       Name <Nm> [1..1] Text 428
       Address <Adr> [0..1]  428
         AddressType <AdrTp> [0..1] CodeSet 429
         AddressLine <AdrLine> [0..5] Text 429
         StreetName <StrtNm> [0..1] Text 429
         BuildingNumber <BldgNb> [0..1] Text 429
         PostCode <PstCd> [0..1] Text 430
         TownName <TwnNm> [0..1] Text 430
         CountrySubDivision <CtrySubDvsn> [0..1] Text 430
         Country <Ctry> [1..1] CodeSet C4 430
   AlternateIdentification <AltrnId> [0..1] ± 430
   ProcessingIdentification <PrcgId> [0..1] Text 430
   AdditionalInformation <AddtlInf> [0..1] ± C1 431
   InvestorCapacity <InvstrCpcty> [0..1] ± 431
   TradingPartyCapacity <TradgPtyCpcty> [0..1] ± 431
6.4.10.4  Seller <Sellr>
Presence: [0..1]
Definition: Party that sells goods or services, or a financial instrument.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 201 February 2025
```

