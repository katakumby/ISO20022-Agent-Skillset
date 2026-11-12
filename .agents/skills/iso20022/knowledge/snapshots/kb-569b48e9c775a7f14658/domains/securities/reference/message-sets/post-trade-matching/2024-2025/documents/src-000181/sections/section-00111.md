---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "4.4 Message Building Blocks", "4.4.3 OtherBusinessParties <OthrBizPties>", "4.4.3.2 StockExchange <StockXchg>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4.4.3.2 StockExchange <StockXchg>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

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
4.4.3.2  StockExchange <StockXchg>
Presence: [0..1]
Definition: Party that identifies the stock exchange.
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 144 February 2025
```

