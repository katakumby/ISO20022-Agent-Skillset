---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.2 Instrument <Instrm>"]
file_pages: [1379, 1380]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.2 Instrument <Instrm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1379 to 1380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1379

```text
38.4.15.8.2  Instrument <Instrm>
Presence: [1..1]
Definition: Identification of the asset.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1379 May 2026
```

## File page 1380

```text
Instrument <Instrm> contains one of the following FinancialInstrument102Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Security <Scty> [1..1]  C23 1381
     Identification <Id> [1..1]  1383
{Or       ISIN <ISIN> [1..1] IdentifierSet 1384
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1384
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1385
Or       RIC <RIC> [1..1] IdentifierSet 1385
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1385
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1385
Or       CTA <CTA> [1..1] IdentifierSet 1385
Or       QUICK <QUICK> [1..1] IdentifierSet 1385
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1385
Or       Dutch <Dtch> [1..1] IdentifierSet 1386
Or       Valoren <Vlrn> [1..1] IdentifierSet 1386
Or       Sicovam <SCVM> [1..1] IdentifierSet 1386
Or       Belgian <Belgn> [1..1] IdentifierSet 1386
Or       Common <Cmon> [1..1] IdentifierSet 1386
Or       DTI <DTI> [1..1] IdentifierSet 1386
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1386
         Identification <Id> [1..1] Text 1387
         IdentificationSource <IdSrc> [1..1] ± 1387
     Name <Nm> [0..1] Text 1387
     ShortName <ShrtNm> [0..1] Text 1387
     ClassificationType <ClssfctnTp> [0..1] ± 1387
     RestrictedIndicator <RstrctdInd> [0..1] Indicator 1387
     AlternateSecurity <AltrnScty> [0..*]  C24 1388
       Identification <Id> [1..1]  1389
{Or         ISIN <ISIN> [1..1] IdentifierSet 1389
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1390
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or         RIC <RIC> [1..1] IdentifierSet 1390
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1380 May 2026
```

