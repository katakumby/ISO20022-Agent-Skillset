---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.2 SecurityIdentification25Choice", "66.1.19.2.1 ISIN <ISIN>"]
file_pages: [4522]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.2.1 ISIN <ISIN>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4522 to 4522.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4522

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 4522
Or   SEDOL <SEDOL> [1..1] IdentifierSet 4522
Or   CUSIP <CUSIP> [1..1] IdentifierSet 4522
Or   RIC <RIC> [1..1] IdentifierSet 4523
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 4523
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 4523
Or   CTA <CTA> [1..1] IdentifierSet 4523
Or   QUICK <QUICK> [1..1] IdentifierSet 4523
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 4523
Or   Dutch <Dtch> [1..1] IdentifierSet 4524
Or   Valoren <Vlrn> [1..1] IdentifierSet 4524
Or   Sicovam <SCVM> [1..1] IdentifierSet 4524
Or   Belgian <Belgn> [1..1] IdentifierSet 4524
Or   Common <Cmon> [1..1] IdentifierSet 4524
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  4524
     Identification <Id> [1..1] Text 4524
     IdentificationSource <IdSrc> [1..1] ± 4525
66.1.19.2.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
66.1.19.2.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
66.1.19.2.3  CUSIP <CUSIP>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4522 May 2026
```

