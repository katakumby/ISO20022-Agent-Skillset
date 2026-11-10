---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.7 ProcessingCharacteristics9", "66.1.26.7.8 DealingFrequencyDescription <DealgFrqcyDesc>"]
file_pages: [4738]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.7.8 DealingFrequencyDescription <DealgFrqcyDesc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4738 to 4738.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4738

```text
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
MNTH Monthly Event takes place every month or once a
month.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
CLOS Closed Event cannot take place, because, for
example, the fund is closed.
TOMN EveryTwoMonths Event takes place every two months.
TOWK EveryTwoWeeks Event takes place every two weeks.
TWMN TwiceAMonth Event takes place two times a month.
66.1.26.7.8  DealingFrequencyDescription <DealgFrqcyDesc>
Presence: [0..1]
Definition: Description of frequency at which the switch is done.
Datatype: "Max350Text" on page 5403
66.1.26.7.9  DealingCutOffTime <DealgCutOffTm>
Presence: [0..1]
Definition: Latest time at which an order to switch can be given.
Datatype: "ISOTime" on page 5405
66.1.26.7.10  DealingCutOffTimeFrame <DealgCutOffTmFrame>
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4738 May 2026
```

