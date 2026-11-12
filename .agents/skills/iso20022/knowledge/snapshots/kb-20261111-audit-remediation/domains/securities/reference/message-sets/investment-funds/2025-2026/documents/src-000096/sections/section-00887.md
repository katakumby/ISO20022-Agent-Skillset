---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.9 Conversion <Convs>", "36.4.15.11.9.1 TargetSecurity <TrgtScty>", "36.4.15.11.9.1.1 Identification <Id>"]
file_pages: [1226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.9.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1226 to 1226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1226

```text
TargetSecurity <TrgtScty> contains the following FinancialInstrumentIdentification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1226
{Or     ISIN <ISIN> [1..1] IdentifierSet 1227
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1227
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1228
Or     RIC <RIC> [1..1] IdentifierSet 1228
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1228
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1228
Or     CTA <CTA> [1..1] IdentifierSet 1228
Or     QUICK <QUICK> [1..1] IdentifierSet 1228
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1228
Or     Dutch <Dtch> [1..1] IdentifierSet 1229
Or     Valoren <Vlrn> [1..1] IdentifierSet 1229
Or     Sicovam <SCVM> [1..1] IdentifierSet 1229
Or     Belgian <Belgn> [1..1] IdentifierSet 1229
Or     Common <Cmon> [1..1] IdentifierSet 1229
Or     DTI <DTI> [1..1] IdentifierSet 1229
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1229
       Identification <Id> [1..1] Text 1230
       IdentificationSource <IdSrc> [1..1] ± 1230
   Name <Nm> [0..1] Text 1230
   ShortName <ShrtNm> [0..1] Text 1230
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
36.4.15.11.9.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1226 May 2026
```

