---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.2 Instrument <Instrm>", "35.4.14.10.2.1 Security <Scty>", "35.4.14.10.2.1.1 Identification <Id>"]
file_pages: [1021]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.2.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1021 to 1021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1021

```text
Security <Scty> contains the following FinancialInstrumentIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1021
{Or     ISIN <ISIN> [1..1] IdentifierSet 1022
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1022
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1023
Or     RIC <RIC> [1..1] IdentifierSet 1023
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1023
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1023
Or     CTA <CTA> [1..1] IdentifierSet 1023
Or     QUICK <QUICK> [1..1] IdentifierSet 1023
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1023
Or     Dutch <Dtch> [1..1] IdentifierSet 1024
Or     Valoren <Vlrn> [1..1] IdentifierSet 1024
Or     Sicovam <SCVM> [1..1] IdentifierSet 1024
Or     Belgian <Belgn> [1..1] IdentifierSet 1024
Or     Common <Cmon> [1..1] IdentifierSet 1024
Or     DTI <DTI> [1..1] IdentifierSet 1024
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1024
       Identification <Id> [1..1] Text 1025
       IdentificationSource <IdSrc> [1..1] ± 1025
   Name <Nm> [0..1] Text 1025
   ShortName <ShrtNm> [0..1] Text 1025
   ClassificationType <ClssfctnTp> [0..1] ± 1025
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
35.4.14.10.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1021 May 2026
```

