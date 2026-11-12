---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.17 Price", "9.1.17.3 PriceType4Choice"]
file_pages: [262]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.17.3 PriceType4Choice

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 262 to 262.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 262

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
9.1.17.3  PriceType4Choice
Definition: Choice of price type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Market <Mkt> [1..1] ± 262
Or}   Indicative <Indctv> [1..1] ± 262
9.1.17.3.1  Market <Mkt>
Presence: [1..1]
Definition: Last reported price of a financial instrument in a market, determined by supply and demand.
Market <Mkt> contains the following elements (see "Price7" on page 260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
9.1.17.3.2  Indicative <Indctv>
Presence: [1..1]
Definition: Estimated price, for valuation purposes.
Indicative <Indctv> contains the following elements (see "Price7" on page 260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
9.1.18 Quantity
9.1.18.1  QuantityBreakdown32
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 263
   LotQuantity <LotQty> [0..1] ± 263
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 263
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 262 September 2025
```

