---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.15 ProcessingCharacteristics11", "66.1.26.15.14 LimitedPeriod <LtdPrd>"]
file_pages: [4761]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.15.14 LimitedPeriod <LtdPrd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4761 to 4761.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4761

```text
DealConfirmationTimeFrame <DealConfTmFrame> contains the following elements (see
"TimeFrame11" on page 4473 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherTimeFrameDescription <OthrTmFrameDesc> [0..1] Text 4474
   TradePlus <TPlus> [0..1] Quantity 4474
   NonWorkingDayAdjustment <NonWorkgDayAdjstmnt> [0..1] CodeSet 4474
   ReferToOrderDesk <RefrToOrdrDsk> [0..1] CodeSet 4474
Constraints
• NonWorkingDayAdjustmentRule
If NonWorkingDayAdjustment is present then TradePlus must also be present.
On Condition
    /NonWorkingDayAdjustment is present
Following Must be True
    /TradePlus Must be present
• TradePlusRule
If TradePlus is present then NonWorkingDayAdjustment must also be present.
On Condition
    /TradePlus is present
Following Must be True
    /NonWorkingDayAdjustment Must be present
66.1.26.15.14  LimitedPeriod <LtdPrd>
Presence: [0..1]
Definition: Specific period, for example, for some guaranteed funds, during which the units/shares may
be subscribed.
Datatype: "Max350Text" on page 5403
66.1.26.15.15  SettlementCycle <SttlmCycl>
Presence: [0..1]
Definition: Settlement timing.
SettlementCycle <SttlmCycl> contains one of the following TimeFrame7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TradePlus <TPlus> [1..1] Quantity 4761
Or}   Prepayment <Prepmt> [1..1] Indicator 4762
66.1.26.15.15.1  TradePlus <TPlus>
Presence: [1..1]
Definition: Number of days after the trade date (T) for the standard settlement timeframe.
Datatype: "Number" on page 5400
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4761 May 2026
```

