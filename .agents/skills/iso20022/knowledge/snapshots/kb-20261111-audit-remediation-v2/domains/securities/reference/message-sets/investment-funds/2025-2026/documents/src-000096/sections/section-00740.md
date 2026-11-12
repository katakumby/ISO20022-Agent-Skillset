---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.2 Instrument <Instrm>", "35.4.14.10.2.1 Security <Scty>"]
file_pages: [1020]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.2.1 Security <Scty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1020 to 1020.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1020

```text
Instrument <Instrm> contains one of the following FinancialInstrument101Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Security <Scty> [1..1]  C27 1020
     Identification <Id> [1..1]  1021
{Or       ISIN <ISIN> [1..1] IdentifierSet 1022
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1022
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1023
Or       RIC <RIC> [1..1] IdentifierSet 1023
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1023
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1023
Or       CTA <CTA> [1..1] IdentifierSet 1023
Or       QUICK <QUICK> [1..1] IdentifierSet 1023
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1023
Or       Dutch <Dtch> [1..1] IdentifierSet 1024
Or       Valoren <Vlrn> [1..1] IdentifierSet 1024
Or       Sicovam <SCVM> [1..1] IdentifierSet 1024
Or       Belgian <Belgn> [1..1] IdentifierSet 1024
Or       Common <Cmon> [1..1] IdentifierSet 1024
Or       DTI <DTI> [1..1] IdentifierSet 1024
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1024
         Identification <Id> [1..1] Text 1025
         IdentificationSource <IdSrc> [1..1] ± 1025
     Name <Nm> [0..1] Text 1025
     ShortName <ShrtNm> [0..1] Text 1025
     ClassificationType <ClssfctnTp> [0..1] ± 1025
Or   CashAsset <CshAsst> [1..1] ± C25 1025
Or}   OtherAsset <OthrAsst> [1..1] ± 1026
35.4.14.10.2.1  Security <Scty>
Presence: [1..1]
Definition: Identification of the security.
Impacted by: C27 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1020 May 2026
```

