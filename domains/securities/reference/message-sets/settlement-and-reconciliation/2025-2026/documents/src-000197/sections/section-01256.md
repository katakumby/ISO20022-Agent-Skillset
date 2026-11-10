---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.20 Price", "35.1.20.6 Price10", "35.1.20.6.2 Value <Val>"]
file_pages: [1713]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.20.6.2 Value <Val>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1713 to 1713.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1713

```text
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PARV Par Price is the face amount.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
NEGA NegativeActualAmount Price must be interpreted as a negative
amount of currency per unit or per share.
35.1.20.6.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 1710
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1710
Or}   Amount <Amt> [1..1] Amount C2 1710
35.1.20.7  PriceRateOrAmountOrUnknown2Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1713
Or   Amount <Amt> [1..1] Amount C2 1713
Or}   UnknownIndicator <UknwnInd> [1..1] Indicator 1714
35.1.20.7.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is, percentage.
Datatype: "PercentageRate" on page 2190
35.1.20.7.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 2041
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1713 March 2026
```

