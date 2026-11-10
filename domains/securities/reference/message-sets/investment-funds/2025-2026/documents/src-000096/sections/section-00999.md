---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.2 Instrument <Instrm>", "38.4.15.8.2.1 Security <Scty>", "38.4.15.8.2.1.6 AlternateSecurity <AltrnScty>"]
file_pages: [1388]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.2.1.6 AlternateSecurity <AltrnScty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1388 to 1388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1388

```text
• Meaning When True: Yes
• Meaning When False: No
38.4.15.8.2.1.6  AlternateSecurity <AltrnScty>
Presence: [0..*]
Definition: Alternative security offered in place of a restricted security.
Impacted by: C24 "IdentificationGuideline"
AlternateSecurity <AltrnScty> contains the following FinancialInstrumentIdentification9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1389
{Or     ISIN <ISIN> [1..1] IdentifierSet 1389
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1390
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or     RIC <RIC> [1..1] IdentifierSet 1390
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Or     CTA <CTA> [1..1] IdentifierSet 1390
Or     QUICK <QUICK> [1..1] IdentifierSet 1390
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1391
Or     Dutch <Dtch> [1..1] IdentifierSet 1391
Or     Valoren <Vlrn> [1..1] IdentifierSet 1391
Or     Sicovam <SCVM> [1..1] IdentifierSet 1391
Or     Belgian <Belgn> [1..1] IdentifierSet 1391
Or     Common <Cmon> [1..1] IdentifierSet 1391
Or     DTI <DTI> [1..1] IdentifierSet 1391
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1391
       Identification <Id> [1..1] Text 1392
       IdentificationSource <IdSrc> [1..1] ± 1392
   Name <Nm> [0..1] Text 1392
   ShortName <ShrtNm> [0..1] Text 1392
   ClassificationType <ClssfctnTp> [0..1] ± 1392
   AlternateSecurityType <AltrnSctyTp> [0..1] ± 1393
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1388 May 2026
```

