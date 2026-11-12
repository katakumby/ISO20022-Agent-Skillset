---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.2 Instrument <Instrm>", "36.4.15.11.2.1 Security <Scty>", "36.4.15.11.2.1.1 Identification <Id>", "36.4.15.11.2.1.1.1 ISIN <ISIN>"]
file_pages: [1217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.2.1.1.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1217 to 1217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1217

```text
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 1217
Or   SEDOL <SEDOL> [1..1] IdentifierSet 1217
Or   CUSIP <CUSIP> [1..1] IdentifierSet 1218
Or   RIC <RIC> [1..1] IdentifierSet 1218
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 1218
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 1218
Or   CTA <CTA> [1..1] IdentifierSet 1218
Or   QUICK <QUICK> [1..1] IdentifierSet 1218
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 1218
Or   Dutch <Dtch> [1..1] IdentifierSet 1219
Or   Valoren <Vlrn> [1..1] IdentifierSet 1219
Or   Sicovam <SCVM> [1..1] IdentifierSet 1219
Or   Belgian <Belgn> [1..1] IdentifierSet 1219
Or   Common <Cmon> [1..1] IdentifierSet 1219
Or   DTI <DTI> [1..1] IdentifierSet 1219
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  1219
     Identification <Id> [1..1] Text 1220
     IdentificationSource <IdSrc> [1..1] ± 1220
36.4.15.11.2.1.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
36.4.15.11.2.1.1.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1217 May 2026
```

