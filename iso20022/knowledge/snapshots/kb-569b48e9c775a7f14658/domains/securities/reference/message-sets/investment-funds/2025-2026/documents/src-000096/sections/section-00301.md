---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.7 TransactionOnAccount <TxOnAcct>", "22.4.7.2 Name <Nm>"]
file_pages: [417]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.7.2 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 417 to 417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 417

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
22.4.7.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
22.4.7.3  SupplementaryIdentification <SplmtryId>
Presence: [0..1]
Definition: Additional information about a financial instrument to help identify the instrument.
Datatype: "Max35Text" on page 5403
22.4.7.4  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Form, ie, ownership, of the security, eg, registered or bearer.
Datatype: "FormOfSecurity1Code" on page 5304
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 417 May 2026
```

