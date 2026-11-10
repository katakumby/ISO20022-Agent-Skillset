---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.4 FinancialInstrument87", "66.1.18.4.2 Name <Nm>"]
file_pages: [4497]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.4.2 Name <Nm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4497 to 4497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4497

```text
Identification <Id> contains one of the following elements (see "SecurityIdentification25Choice" on
page 4521 for details)
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
66.1.18.4.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
66.1.18.4.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
66.1.18.4.4  SupplementaryIdentification <SplmtryId>
Presence: [0..1]
Definition: Additional information about the financial instrument to help identify the instrument.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4497 May 2026
```

