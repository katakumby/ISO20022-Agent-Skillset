---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.2 Instrument <Instrm>", "38.4.15.8.2.1 Security <Scty>"]
file_pages: [1381, 1382]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.2.1 Security <Scty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1381 to 1382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1381

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Or         CTA <CTA> [1..1] IdentifierSet 1390
Or         QUICK <QUICK> [1..1] IdentifierSet 1390
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1391
Or         Dutch <Dtch> [1..1] IdentifierSet 1391
Or         Valoren <Vlrn> [1..1] IdentifierSet 1391
Or         Sicovam <SCVM> [1..1] IdentifierSet 1391
Or         Belgian <Belgn> [1..1] IdentifierSet 1391
Or         Common <Cmon> [1..1] IdentifierSet 1391
Or         DTI <DTI> [1..1] IdentifierSet 1391
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1391
           Identification <Id> [1..1] Text 1392
           IdentificationSource <IdSrc> [1..1] ± 1392
       Name <Nm> [0..1] Text 1392
       ShortName <ShrtNm> [0..1] Text 1392
       ClassificationType <ClssfctnTp> [0..1] ± 1392
       AlternateSecurityType <AltrnSctyTp> [0..1] ± 1393
Or   CashAsset <CshAsst> [1..1] ± 1393
Or}   OtherAsset <OthrAsst> [1..1] ± 1393
38.4.15.8.2.1  Security <Scty>
Presence: [1..1]
Definition: Identification of the security.
Impacted by: C23 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1381 May 2026
```

## File page 1382

```text
Security <Scty> contains the following FinancialInstrumentIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1383
{Or     ISIN <ISIN> [1..1] IdentifierSet 1384
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1384
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1385
Or     RIC <RIC> [1..1] IdentifierSet 1385
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1385
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1385
Or     CTA <CTA> [1..1] IdentifierSet 1385
Or     QUICK <QUICK> [1..1] IdentifierSet 1385
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1385
Or     Dutch <Dtch> [1..1] IdentifierSet 1386
Or     Valoren <Vlrn> [1..1] IdentifierSet 1386
Or     Sicovam <SCVM> [1..1] IdentifierSet 1386
Or     Belgian <Belgn> [1..1] IdentifierSet 1386
Or     Common <Cmon> [1..1] IdentifierSet 1386
Or     DTI <DTI> [1..1] IdentifierSet 1386
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1386
       Identification <Id> [1..1] Text 1387
       IdentificationSource <IdSrc> [1..1] ± 1387
   Name <Nm> [0..1] Text 1387
   ShortName <ShrtNm> [0..1] Text 1387
   ClassificationType <ClssfctnTp> [0..1] ± 1387
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 1387
   AlternateSecurity <AltrnScty> [0..*]  C24 1388
     Identification <Id> [1..1]  1389
{Or       ISIN <ISIN> [1..1] IdentifierSet 1389
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1390
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or       RIC <RIC> [1..1] IdentifierSet 1390
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1382 May 2026
```

