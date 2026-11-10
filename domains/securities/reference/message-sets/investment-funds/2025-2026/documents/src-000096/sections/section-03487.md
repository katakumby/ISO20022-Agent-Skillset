---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.7 ProcessingCharacteristics9", "66.1.26.7.3 AmountIndicator <AmtInd>"]
file_pages: [4737]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.7.3 AmountIndicator <AmtInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4737 to 4737.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4737

```text
66.1.26.7.3  AmountIndicator <AmtInd>
Presence: [0..1]
Definition: Indicates whether a switch can be instructed by amount.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.7.4  UnitsIndicator <UnitsInd>
Presence: [0..1]
Definition: Indicates whether a switch can be instructed as a number of units.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.7.5  Rounding <Rndg>
Presence: [0..1]
Definition: Indicates the rounding direction applied to nearest unit.
Datatype: "RoundingDirection2Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
66.1.26.7.6  MainFundOrderDeskLocation <MainFndOrdrDskLctn>
Presence: [0..1]
Definition: Location of the main fund order desk.
MainFundOrderDeskLocation <MainFndOrdrDskLctn> contains the following elements (see
"MainFundOrderDeskLocation1" on page 4783 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 4783
   TimeZoneOffSet <TmZoneOffSet> [1..1]  4784
     Sign <Sgn> [1..1] Indicator 4784
     NumberOfHours <NbOfHrs> [1..1] Time 4784
66.1.26.7.7  DealingFrequency <DealgFrqcy>
Presence: [0..1]
Definition: Frequency at which the switches are done.
Datatype: "EventFrequency5Code" on page 5298
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4737 May 2026
```

