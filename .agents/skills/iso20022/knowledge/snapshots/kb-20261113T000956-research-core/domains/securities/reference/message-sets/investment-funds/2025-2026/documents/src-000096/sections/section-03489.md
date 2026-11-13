---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.7 ProcessingCharacteristics9", "66.1.26.7.11 DealConfirmationTime <DealConfTm>"]
file_pages: [4739]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.7.11 DealConfirmationTime <DealConfTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4739 to 4739.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4739

```text
Constraints
• NonWorkingDayAdjustmentRule
If NonWorkingDayAdjustment is present then TradeMinus must also be present.
On Condition
    /NonWorkingDayAdjustment is present
Following Must be True
    /TradeMinus Must be present
• TradeMinusRule
If TradeMinus is present then NonWorkingDayAdjustment must also be present.
On Condition
    /TradeMinus is present
Following Must be True
    /NonWorkingDayAdjustment Must be present
66.1.26.7.11  DealConfirmationTime <DealConfTm>
Presence: [0..1]
Definition: Time at which the deal confirmation is issued.
Datatype: "ISOTime" on page 5405
66.1.26.7.12  DealConfirmationTimeFrame <DealConfTmFrame>
Presence: [0..1]
Definition: Time frame within which the deal confirmation is issued.
Impacted by: C26 "NonWorkingDayAdjustmentRule", C36 "TradePlusRule"
DealConfirmationTimeFrame <DealConfTmFrame> contains the following elements (see
"TimeFrame8" on page 4471 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherTimeFrameDescription <OthrTmFrameDesc> [0..1] Text 4471
   TradePlus <TPlus> [0..1] Quantity 4471
   NonWorkingDayAdjustment <NonWorkgDayAdjstmnt> [0..1] CodeSet 4471
   ReferToOrderDesk <RefrToOrdrDsk> [0..1] CodeSet 4472
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4739 May 2026
```

