---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.2 Instrument <Instrm>", "36.4.15.11.2.1 Security <Scty>"]
file_pages: [1215]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.2.1 Security <Scty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1215 to 1215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1215

```text
Instrument <Instrm> contains one of the following FinancialInstrument101Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Security <Scty> [1..1]  C29 1215
     Identification <Id> [1..1]  1216
{Or       ISIN <ISIN> [1..1] IdentifierSet 1217
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1217
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1218
Or       RIC <RIC> [1..1] IdentifierSet 1218
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1218
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1218
Or       CTA <CTA> [1..1] IdentifierSet 1218
Or       QUICK <QUICK> [1..1] IdentifierSet 1218
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1218
Or       Dutch <Dtch> [1..1] IdentifierSet 1219
Or       Valoren <Vlrn> [1..1] IdentifierSet 1219
Or       Sicovam <SCVM> [1..1] IdentifierSet 1219
Or       Belgian <Belgn> [1..1] IdentifierSet 1219
Or       Common <Cmon> [1..1] IdentifierSet 1219
Or       DTI <DTI> [1..1] IdentifierSet 1219
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1219
         Identification <Id> [1..1] Text 1220
         IdentificationSource <IdSrc> [1..1] ± 1220
     Name <Nm> [0..1] Text 1220
     ShortName <ShrtNm> [0..1] Text 1220
     ClassificationType <ClssfctnTp> [0..1] ± 1220
Or   CashAsset <CshAsst> [1..1] ± C27 1220
Or}   OtherAsset <OthrAsst> [1..1] ± 1221
36.4.15.11.2.1  Security <Scty>
Presence: [1..1]
Definition: Identification of the security.
Impacted by: C29 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1215 May 2026
```

