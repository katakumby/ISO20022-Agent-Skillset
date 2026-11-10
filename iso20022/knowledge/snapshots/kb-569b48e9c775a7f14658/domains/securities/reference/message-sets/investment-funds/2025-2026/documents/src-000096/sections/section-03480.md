---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.5 Equalisation4", "66.1.26.5.2 Rate <Rate>"]
file_pages: [4730]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.5.2 Rate <Rate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4730 to 4730.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4730

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.5.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used for calculation of the equalisation.
Datatype: "PercentageRate" on page 5401
66.1.26.5.3  EqualisationMethodologyType <EqulstnMthdlgyTp>
Presence: [0..1]
Definition: Methodology used for the allocation of the performance fees.
Datatype: "EqualisationMethodologyType1Code" on page 5296
CodeName Name Definition
COLI ContingentLiquidation Mandatory redemption of units
processed either at redemption or
crystallization, whose proceeds are due
to the asset manager as performance
fee. Performance fee to be paid by the
investor when the value of the
investment fund units were below their
applicable high-watermark on
subscription date, and above the high-
watermark on redemption date.
DDEP DepreciationDeposit Performance fee to be paid by the
investor when the net asset value
reaches the high-watermark if the net
asset value was under the high-
watermark on subscription date.
EQCR EqualisationCredit Prepayment amount to be paid by the
investor at the moment of the
subscription. The amount is based on
the positive difference between the gross
asset value at subscription and the high-
watermark, when the investment fund
units are subscribed to above their high-
watermark.
66.1.26.5.4  ContingentLiquidationPerUnit <CntngntLqdtnPerUnit>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4730 May 2026
```

