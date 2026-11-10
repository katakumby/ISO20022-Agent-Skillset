---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.14 Date Time Period", "66.1.14.3 TimeFrame8"]
file_pages: [4471]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.14.3 TimeFrame8

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4471 to 4471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4471

```text
66.1.14.3  TimeFrame8
Definition: Time frame elements that define a period as number of days before or after a activity.
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
Following Must be True
    /NonWorkingDayAdjustment Must be present
66.1.14.3.1  OtherTimeFrameDescription <OthrTmFrameDesc>
Presence: [0..1]
Definition: Description of the timeframe.
Datatype: "Max350Text" on page 5403
66.1.14.3.2  TradePlus <TPlus>
Presence: [0..1]
Definition: Number of days after the trade date (T) used for the standard timeframe for the issue of a
deal confirmation.
Datatype: "Number" on page 5400
66.1.14.3.3  NonWorkingDayAdjustment <NonWorkgDayAdjstmnt>
Presence: [0..1]
Definition: Convention used for adjusting a date when it is not a business day.
Datatype: "BusinessDayConvention1Code" on page 5278
CodeName Name Definition
FWNG Following The date will be the first following day
that is a business day.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4471 May 2026
```

