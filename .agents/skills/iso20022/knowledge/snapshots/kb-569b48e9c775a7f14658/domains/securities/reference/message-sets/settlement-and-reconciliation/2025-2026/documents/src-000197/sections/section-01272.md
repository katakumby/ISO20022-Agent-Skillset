---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.8 QuantityBreakdown58", "35.1.21.8.4 LotPrice <LotPric>"]
file_pages: [1729]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.8.4 LotPrice <LotPric>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1729 to 1729.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1729

```text
LotDateTime <LotDtTm> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.21.8.4  LotPrice <LotPric>
Presence: [0..1]
Definition: Price at which the lot was purchased.
LotPrice <LotPric> contains the following elements (see "Price7" on page 1715 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.21.8.5  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of price and information about the price.
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice29Choice" on
page 1711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1711
Or}   Proprietary <Prtry> [1..1] ± 1711
35.1.21.8.6  AccountBaseCurrencyAmounts <AcctBaseCcyAmts>
Presence: [0..1]
Definition: Valuation amounts for the lot provided in the base currency of the account.
AccountBaseCurrencyAmounts <AcctBaseCcyAmts> contains the following elements (see
"BalanceAmounts2" on page 1421 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1421
   BookValue <BookVal> [0..1] ± 1421
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1421
35.1.21.8.7  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts for the lot provided in the currency of the financial instrument.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1729 March 2026
```

