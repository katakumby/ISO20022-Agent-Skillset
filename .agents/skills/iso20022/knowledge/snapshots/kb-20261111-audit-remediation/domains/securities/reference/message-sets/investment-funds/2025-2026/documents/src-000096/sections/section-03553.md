---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.33 ProcessingCharacteristics10", "66.1.26.33.3 AmountIndicator <AmtInd>"]
file_pages: [4803]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.33.3 AmountIndicator <AmtInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4803 to 4803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4803

```text
66.1.26.33.3  AmountIndicator <AmtInd>
Presence: [0..1]
Definition: Indicates whether a redemption can be instructed by amount.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.33.4  UnitsIndicator <UnitsInd>
Presence: [0..1]
Definition: Indicates whether a redemption can be instructed as a number of units.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.33.5  Rounding <Rndg>
Presence: [0..1]
Definition: Indicates the rounding direction applied to nearest unit.
Datatype: "RoundingDirection2Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
66.1.26.33.6  PercentageIndicator <PctgInd>
Presence: [0..1]
Definition: Indicates whether a redemption can be instructed as a percentage of holding.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.33.7  MainFundOrderDeskLocation <MainFndOrdrDskLctn>
Presence: [0..1]
Definition: Location of the main fund order desk.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4803 May 2026
```

