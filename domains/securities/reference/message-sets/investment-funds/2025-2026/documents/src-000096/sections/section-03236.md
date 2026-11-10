---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.14 Date Time Period", "66.1.14.3 TimeFrame8", "66.1.14.3.4 ReferToOrderDesk <RefrToOrdrDsk>"]
file_pages: [4472]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.14.3.4 ReferToOrderDesk <RefrToOrdrDsk>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4472 to 4472.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4472

```text
CodeName Name Definition
PREC Preceding The date will be the first preceding day
that is a business day.
66.1.14.3.4  ReferToOrderDesk <RefrToOrdrDsk>
Presence: [0..1]
Definition: For the time of the issuance of the deal confirmation, the order desk must be contacted.
Datatype: "ReferToFundOrderDesk1Code" on page 5347
CodeName Name Definition
RFOD ReferToFundOrderDesk Indicates that the operation is only
possible in restricted circumstances.
66.1.14.4  TimeFrame10
Definition: Time frame elements that define a period as number of days before or after a activity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherTimeFrameDescription <OthrTmFrameDesc> [0..1] Text 4472
   TradePlus <TPlus> [0..1] Quantity 4472
   NonWorkingDayAdjustment <NonWorkgDayAdjstmnt> [0..1] CodeSet 4473
   ReferToOrderDesk <RefrToOrdrDsk> [0..1] CodeSet 4473
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
66.1.14.4.1  OtherTimeFrameDescription <OthrTmFrameDesc>
Presence: [0..1]
Definition: Description of the timeframe.
Datatype: "Max350Text" on page 5403
66.1.14.4.2  TradePlus <TPlus>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4472 May 2026
```

