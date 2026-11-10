---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.1 FinancialInstrument96", "66.1.18.1.7 DividendFrequency <DvddFrqcy>"]
file_pages: [4487]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.1.7 DividendFrequency <DvddFrqcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4487 to 4487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4487

```text
CodeName Name Definition
CASH Cash Dividend is paid in cash.
UNIT Units Dividend is paid in units.
BOTH Both Dividend is paid in both Cash and Units.
66.1.18.1.7  DividendFrequency <DvddFrqcy>
Presence: [0..1]
Definition: Frequency with which the income is allocated to investors.
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
66.1.18.1.8  ReinvestmentFrequency <RinvstmtFrqcy>
Presence: [0..1]
Definition: Frequency with which the reinvestment takes place, this is the same or less than the
dividend frequency.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4487 May 2026
```

