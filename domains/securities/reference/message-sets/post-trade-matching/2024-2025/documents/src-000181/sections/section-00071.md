---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.1 Geographics <Geogcs>"]
file_pages: [96]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.1 Geographics <Geogcs>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 96 to 96.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExpirationDate <XprtnDt> [0..1] DateTime 104
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C13 104
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 104
   PriceRange <PricRg> [0..1] ± 105
   CallableIndicator <CllblInd> [0..1] Indicator 105
   ConvertibleIndicator <ConvtblInd> [0..1] Indicator 105
   PutableIndicator <PutblInd> [0..1] Indicator 105
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 106
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 106
   PerpetualIndicator <PerptlInd> [0..1] Indicator 106
3.4.8.1  Geographics <Geogcs>
Presence: [0..1]
Definition: Type of stipulation expressing geographical constraints on a fixed income instrument. It is
expressed with a state or country abbreviation and a minimum or maximum percentage. Example: CA
0-80 (minimum of 80 percent in Californian assests).
Datatype: "Max35Text" on page 669
3.4.8.2  YieldRange <YldRg>
Presence: [0..1]
Definition: Range of allowed yield.
YieldRange <YldRg> contains the following elements (see "AmountOrPercentageRange1" on
page 316 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 316
   Term <Term> [0..10]  316
     Operator <Oprtr> [1..1] CodeSet 317
     Value <Val> [1..1]  317
{Or       RateValue <RateVal> [1..1] Rate 317
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 317
3.4.8.3  Rating <Ratg>
Presence: [0..1]
Definition: Range of assessment of securities credit and investment risk.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 96 February 2025
```

