---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.29 ProcessingCharacteristics12", "66.1.26.29.11 DealingCutOffTimeFrame <DealgCutOffTmFrame>"]
file_pages: [4789]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.29.11 DealingCutOffTimeFrame <DealgCutOffTmFrame>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4789 to 4789.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4789

```text
66.1.26.29.11  DealingCutOffTimeFrame <DealgCutOffTmFrame>
Presence: [0..1]
Definition: Dealing cut-off timeframe.
Impacted by: C23 "NonWorkingDayAdjustmentRule", C33 "TradeMinusRule"
DealingCutOffTimeFrame <DealgCutOffTmFrame> contains the following elements (see
"TimeFrame9" on page 4469 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherTimeFrameDescription <OthrTmFrameDesc> [0..1] Text 4470
   TradeMinus <TMns> [0..1] Quantity 4470
   NonWorkingDayAdjustment <NonWorkgDayAdjstmnt> [0..1] CodeSet 4470
   ReferToOrderDesk <RefrToOrdrDsk> [0..1] CodeSet 4470
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
66.1.26.29.12  DealConfirmationTime <DealConfTm>
Presence: [0..1]
Definition: Time at which the deal confirmation is issued.
Datatype: "ISOTime" on page 5405
66.1.26.29.13  DealConfirmationTimeFrame <DealConfTmFrame>
Presence: [0..1]
Definition: Time frame within which the deal confirmation is issued.
Impacted by: C25 "NonWorkingDayAdjustmentRule", C35 "TradePlusRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4789 May 2026
```

