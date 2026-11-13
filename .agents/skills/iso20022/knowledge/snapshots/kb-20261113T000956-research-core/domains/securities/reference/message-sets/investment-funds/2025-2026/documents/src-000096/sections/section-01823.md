---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.1 MasterReference <MstrRef>"]
file_pages: [2561]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2561 to 2561.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2561

```text
Constraints
• BulkCashSettlementDetails3Rule
Either IndividualOrderDetails/CashSettlementDetails or BulkCashSettlementDetails may be present,
but not both.
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences of
IndividualOrderDetails/SettlementAmount, if present.
• SettlementCurrency2Rule
If BulkCashSettlementDetails is present, then Currency in IndividualOrderDetails/SettlementAmount,
if present, must be the same in all occurrences of IndividualOrderDetails.
47.4.4.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
47.4.4.2  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
PlaceOfTrade <PlcOfTrad> contains one of the following elements (see
"PlaceOfTradeIdentification4Choice" on page 4808 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C12 4809
Or   Exchange <Xchg> [1..1] IdentifierSet 4809
Or   Party <Pty> [1..1] IdentifierSet C4 4809
Or}   OverTheCounter <OverTheCntr> [1..1] Text 4809
47.4.4.3  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Definition: Date and time the order is placed by the investor or its agent.
Datatype: "ISODateTime" on page 5388
47.4.4.4  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date on which the order expires.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2561 May 2026
```

