---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.17 Price", "9.1.17.1 Price7", "9.1.17.1.2 Value <Val>"]
file_pages: [261]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.17.1.2 Value <Val>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 261 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
Type <Tp> contains one of the following elements (see "YieldedOrValueType1Choice" on page 243 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 243
Or}   ValueType <ValTp> [1..1] CodeSet 243
9.1.17.1.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 261
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 261
Or}   Amount <Amt> [1..1] Amount C1 261
9.1.17.2  PriceRateOrAmount3Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 261
Or}   Amount <Amt> [1..1] Amount C1 261
9.1.17.2.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Datatype: "PercentageRate" on page 343
9.1.17.2.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 312
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 261 September 2025
```

