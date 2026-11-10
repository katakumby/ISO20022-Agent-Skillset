---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.2 Instrument <Instrm>", "38.4.15.8.2.1 Security <Scty>", "38.4.15.8.2.1.6 AlternateSecurity <AltrnScty>", "38.4.15.8.2.1.6.1 Identification <Id>"]
file_pages: [1389]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.2.1.6.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1389 to 1389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1389

```text
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
38.4.15.8.2.1.6.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 1389
Or   SEDOL <SEDOL> [1..1] IdentifierSet 1390
Or   CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or   RIC <RIC> [1..1] IdentifierSet 1390
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Or   CTA <CTA> [1..1] IdentifierSet 1390
Or   QUICK <QUICK> [1..1] IdentifierSet 1390
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 1391
Or   Dutch <Dtch> [1..1] IdentifierSet 1391
Or   Valoren <Vlrn> [1..1] IdentifierSet 1391
Or   Sicovam <SCVM> [1..1] IdentifierSet 1391
Or   Belgian <Belgn> [1..1] IdentifierSet 1391
Or   Common <Cmon> [1..1] IdentifierSet 1391
Or   DTI <DTI> [1..1] IdentifierSet 1391
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  1391
     Identification <Id> [1..1] Text 1392
     IdentificationSource <IdSrc> [1..1] ± 1392
38.4.15.8.2.1.6.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1389 May 2026
```

