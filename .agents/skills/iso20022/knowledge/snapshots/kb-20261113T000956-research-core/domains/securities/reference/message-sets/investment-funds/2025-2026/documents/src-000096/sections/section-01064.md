---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.4 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "39.4.15.4.2 Instrument <Instrm>", "39.4.15.4.2.1 Security <Scty>", "39.4.15.4.2.1.1 Identification <Id>", "39.4.15.4.2.1.1.1 ISIN <ISIN>"]
file_pages: [1471]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.4.2.1.1.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1471 to 1471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1471

```text
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 1471
Or   SEDOL <SEDOL> [1..1] IdentifierSet 1471
Or   CUSIP <CUSIP> [1..1] IdentifierSet 1472
Or   RIC <RIC> [1..1] IdentifierSet 1472
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 1472
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 1472
Or   CTA <CTA> [1..1] IdentifierSet 1472
Or   QUICK <QUICK> [1..1] IdentifierSet 1472
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 1472
Or   Dutch <Dtch> [1..1] IdentifierSet 1473
Or   Valoren <Vlrn> [1..1] IdentifierSet 1473
Or   Sicovam <SCVM> [1..1] IdentifierSet 1473
Or   Belgian <Belgn> [1..1] IdentifierSet 1473
Or   Common <Cmon> [1..1] IdentifierSet 1473
Or   DTI <DTI> [1..1] IdentifierSet 1473
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  1473
     Identification <Id> [1..1] Text 1474
     IdentificationSource <IdSrc> [1..1] ± 1474
39.4.15.4.2.1.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
39.4.15.4.2.1.1.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1471 May 2026
```

