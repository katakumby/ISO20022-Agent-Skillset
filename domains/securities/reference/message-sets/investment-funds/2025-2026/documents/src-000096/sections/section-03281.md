---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.14 FinancialInstrument13", "66.1.18.14.2 Name <Nm>"]
file_pages: [4518]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.14.2 Name <Nm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4518 to 4518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4518

```text
Definition: Identification of a security by an ISIN.
Identification <Id> contains one of the following elements (see "SecurityIdentification3Choice" on
page 5139 for details)
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
66.1.18.14.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
66.1.18.14.3  SupplementaryIdentification <SplmtryId>
Presence: [0..1]
Definition: Additional information about a financial instrument to help identify the instrument.
Datatype: "Max35Text" on page 5403
66.1.18.14.4  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. For example, a unit may have a specific load structure,
eg, front end or back end, an income policy, eg, pay out or accumulate, or a trailer policy, eg, with or
without. Fund classes are typically denoted by a single character, eg, 'Class A', 'Class 2'.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4518 May 2026
```

