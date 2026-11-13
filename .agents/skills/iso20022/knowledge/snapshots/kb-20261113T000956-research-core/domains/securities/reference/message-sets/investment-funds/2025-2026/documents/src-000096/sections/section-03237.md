---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.14 Date Time Period", "66.1.14.4 TimeFrame10", "66.1.14.4.3 NonWorkingDayAdjustment <NonWorkgDayAdjstmnt>"]
file_pages: [4473]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.14.4.3 NonWorkingDayAdjustment <NonWorkgDayAdjstmnt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4473 to 4473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4473

```text
Definition: Number of days after the trade date (T) used for the standard timeframe for the issue of a
deal confirmation.
Datatype: "Number" on page 5400
66.1.14.4.3  NonWorkingDayAdjustment <NonWorkgDayAdjstmnt>
Presence: [0..1]
Definition: Convention used for adjusting a date when it is not a business day.
Datatype: "BusinessDayConvention1Code" on page 5278
CodeName Name Definition
FWNG Following The date will be the first following day
that is a business day.
PREC Preceding The date will be the first preceding day
that is a business day.
66.1.14.4.4  ReferToOrderDesk <RefrToOrdrDsk>
Presence: [0..1]
Definition: For the time of the issuance of the deal confirmation, the order desk must be contacted.
Datatype: "ReferToFundOrderDesk1Code" on page 5347
CodeName Name Definition
RFOD ReferToFundOrderDesk Indicates that the operation is only
possible in restricted circumstances.
66.1.14.5  TimeFrame11
Definition: Time frame elements that define a period as number of days before or after a activity.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4473 May 2026
```

