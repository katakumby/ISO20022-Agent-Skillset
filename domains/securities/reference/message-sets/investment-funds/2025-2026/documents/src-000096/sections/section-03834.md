---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.9 ValuationDealingProcessingCharacteristics3", "66.1.34.9.2 ValuationFrequencyDescription <ValtnFrqcyDesc>"]
file_pages: [5123]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.9.2 ValuationFrequencyDescription <ValtnFrqcyDesc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5123 to 5123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5123

```text
Definition: Frequency of the valuation.
Datatype: "EventFrequency5Code" on page 5298
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
66.1.34.9.2  ValuationFrequencyDescription <ValtnFrqcyDesc>
Presence: [0..1]
Definition: Further details regarding the dealing frequency, for example, Tuesday (for weekly dealing) or
last business day of the month.
Datatype: "Max350Text" on page 5403
66.1.34.9.3  ValuationTime <ValtnTm>
Presence: [0..1]
Definition: Valuation time of the fund.
Datatype: "ISOTime" on page 5405
66.1.34.9.4  DecimalisationUnits <DcmlstnUnits>
Presence: [0..1]
Definition: Number of decimal places to which quantities of units/shares are rounded.
Datatype: "Number" on page 5400
66.1.34.9.5  DecimalisationPrice <DcmlstnPric>
Presence: [0..1]
Definition: Number of decimal places to which the price is rounded.
Datatype: "Number" on page 5400
66.1.34.9.6  DualFundIndicator <DualFndInd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5123 May 2026
```

