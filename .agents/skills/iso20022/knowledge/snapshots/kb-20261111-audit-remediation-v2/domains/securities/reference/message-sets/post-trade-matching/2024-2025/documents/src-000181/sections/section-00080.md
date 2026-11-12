---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.35 PriceRange <PricRg>"]
file_pages: [105]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.35 PriceRange <PricRg>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 105 to 105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
3.4.8.35  PriceRange <PricRg>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond within a particular price range.
PriceRange <PricRg> contains the following elements (see "AmountOrPercentageRange1" on
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
3.4.8.36  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.37  ConvertibleIndicator <ConvtblInd>
Presence: [0..1]
Definition: Indicates whether the interest bearing security is convertible into another type of security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.38  PutableIndicator <PutblInd>
Presence: [0..1]
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 105 February 2025
```

