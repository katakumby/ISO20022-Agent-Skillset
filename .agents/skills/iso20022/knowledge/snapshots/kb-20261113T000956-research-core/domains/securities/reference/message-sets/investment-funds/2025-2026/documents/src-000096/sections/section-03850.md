---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.39 Securities Identification", "66.1.39.2 SecurityIdentification3Choice"]
file_pages: [5139]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.39.2 SecurityIdentification3Choice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5139 to 5139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5139

```text
Definition: Entity that issues the proprietary identification.
Datatype: "Max35Text" on page 5403
66.1.39.2  SecurityIdentification3Choice
Definition: Choice between formats for the identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 5139
Or   SEDOL <SEDOL> [1..1] IdentifierSet 5139
Or   CUSIP <CUSIP> [1..1] IdentifierSet 5140
Or   RIC <RIC> [1..1] IdentifierSet 5140
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 5140
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 5140
Or   CTA <CTA> [1..1] IdentifierSet 5140
Or   QUICK <QUICK> [1..1] IdentifierSet 5140
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 5140
Or   Dutch <Dtch> [1..1] IdentifierSet 5141
Or   Valoren <Vlrn> [1..1] IdentifierSet 5141
Or   Sicovam <SCVM> [1..1] IdentifierSet 5141
Or   Belgian <Belgn> [1..1] IdentifierSet 5141
Or   Common <Cmon> [1..1] IdentifierSet 5141
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1] ± 5141
66.1.39.2.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINIdentifier" on page 5395
66.1.39.2.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5139 May 2026
```

