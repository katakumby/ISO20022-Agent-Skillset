---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.14 Date Time Period", "66.1.14.2 TimeFrame9", "66.1.14.2.1 OtherTimeFrameDescription <OthrTmFrameDesc>"]
file_pages: [4470]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.14.2.1 OtherTimeFrameDescription <OthrTmFrameDesc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4470 to 4470.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4470

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
66.1.14.2.1  OtherTimeFrameDescription <OthrTmFrameDesc>
Presence: [0..1]
Definition: Description of the timeframe.
Datatype: "Max350Text" on page 5403
66.1.14.2.2  TradeMinus <TMns>
Presence: [0..1]
Definition: Number of days before the trade date (T) used for the standard timeframe for the dealing cut-
off.
Datatype: "Number" on page 5400
66.1.14.2.3  NonWorkingDayAdjustment <NonWorkgDayAdjstmnt>
Presence: [0..1]
Definition: Convention used for adjusting a date when it is not a business day.
Datatype: "BusinessDayConvention1Code" on page 5278
CodeName Name Definition
FWNG Following The date will be the first following day
that is a business day.
PREC Preceding The date will be the first preceding day
that is a business day.
66.1.14.2.4  ReferToOrderDesk <RefrToOrdrDsk>
Presence: [0..1]
Definition: For the dealing cut-off time, the order desk must be contacted.
Datatype: "ReferToFundOrderDesk1Code" on page 5347
CodeName Name Definition
RFOD ReferToFundOrderDesk Indicates that the operation is only
possible in restricted circumstances.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4470 May 2026
```

