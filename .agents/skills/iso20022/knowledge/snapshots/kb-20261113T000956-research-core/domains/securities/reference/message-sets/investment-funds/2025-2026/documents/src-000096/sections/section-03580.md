---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.12 FundCashOutBreakdown3", "66.1.28.12.7 CommissionDetails <ComssnDtls>"]
file_pages: [4830]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.12.7 CommissionDetails <ComssnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4830 to 4830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4830

```text
Definition: Charge for the placement of an order.
ChargeDetails <ChrgDtls> contains the following elements (see "Charge26" on page 4450 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  4451
{Or     Code <Cd> [1..1] CodeSet 4451
Or}     Proprietary <Prtry> [1..1] ± 4452
   ChargeApplied <ChrgApld> [1..1]  4452
{Or     Amount <Amt> [1..1] Amount C1 4452
Or}     Rate <Rate> [1..1] Rate 4452
66.1.28.12.7  CommissionDetails <ComssnDtls>
Presence: [0..*]
Definition: Information related to the commission applied to an order, for example, back-end or front-end
commission.
CommissionDetails <ComssnDtls> contains the following elements (see "Commission21" on
page 4462 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommissionType <ComssnTp> [1..1]  4462
{Or     Code <Cd> [1..1] CodeSet 4462
Or}     Proprietary <Prtry> [1..1] ± 4463
   CommissionApplied <ComssnApld> [1..1]  4463
{Or     Amount <Amt> [1..1] Amount C1 4463
Or}     Rate <Rate> [1..1] Rate 4463
66.1.28.12.8  SettlementCurrency <SttlmCcy>
Presence: [0..1]
Definition: Settlement currency for the transaction.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4830 May 2026
```

