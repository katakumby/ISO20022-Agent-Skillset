---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.3 FinancialInstrument9", "66.1.18.3.2 Name <Nm>"]
file_pages: [4494]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.3.2 Name <Nm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4494 to 4494.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4494

```text
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
66.1.18.3.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
66.1.18.3.3  SupplementaryIdentification <SplmtryId>
Presence: [0..1]
Definition: Additional information about a financial instrument to help identify the instrument.
Datatype: "Max35Text" on page 5403
66.1.18.3.4  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4494 May 2026
```

