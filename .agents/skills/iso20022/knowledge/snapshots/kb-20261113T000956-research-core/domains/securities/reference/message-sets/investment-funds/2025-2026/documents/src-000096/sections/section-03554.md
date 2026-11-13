---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.33 ProcessingCharacteristics10", "66.1.26.33.8 DealingFrequency <DealgFrqcy>"]
file_pages: [4804]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.33.8 DealingFrequency <DealgFrqcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4804 to 4804.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4804

```text
MainFundOrderDeskLocation <MainFndOrdrDskLctn> contains the following elements (see
"MainFundOrderDeskLocation1" on page 4783 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 4783
   TimeZoneOffSet <TmZoneOffSet> [1..1]  4784
     Sign <Sgn> [1..1] Indicator 4784
     NumberOfHours <NbOfHrs> [1..1] Time 4784
66.1.26.33.8  DealingFrequency <DealgFrqcy>
Presence: [0..1]
Definition: Frequency at which the redemptions are done.
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
66.1.26.33.9  DealingFrequencyDescription <DealgFrqcyDesc>
Presence: [0..1]
Definition: Description of frequency at which the redemption is done.
Datatype: "Max350Text" on page 5403
66.1.26.33.10  DealingCutOffTime <DealgCutOffTm>
Presence: [0..1]
Definition: Latest time at which an order to redeem can be given.
Datatype: "ISOTime" on page 5405
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4804 May 2026
```

