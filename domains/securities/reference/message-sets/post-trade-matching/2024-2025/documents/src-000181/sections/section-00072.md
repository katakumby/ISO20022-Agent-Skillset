---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.4 CouponRange <CpnRg>"]
file_pages: [97]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.4 CouponRange <CpnRg>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 97 to 97.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 97

```text
Rating <Ratg> contains the following elements (see "Rating1" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RatingScheme <RatgSchme> [1..1] Text 518
   ValueDate <ValDt> [1..1] DateTime 518
   ValueIdentification <ValId> [1..1] IdentifierSet 518
3.4.8.4  CouponRange <CpnRg>
Presence: [0..1]
Definition: Identification of a range of coupon numbers attached to its related financial instrument.
CouponRange <CpnRg> contains the following elements (see "AmountOrPercentageRange1" on
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
3.4.8.5  AmortisableIndicator <AmtsblInd>
Presence: [0..1]
Definition: Indicates whether the financial instrument repays the principal amount in parts during the life
cycle of the security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.6  Purpose <Purp>
Presence: [0..1]
Definition: Reason for which money is raised through the issuance of a security.
Datatype: "Max256Text" on page 668
3.4.8.7  AlternativeMinimumTaxIndicator <AltrntvMinTaxInd>
Presence: [0..1]
Definition: Identifies whether the issue is subject to alternative minimum taxation (used for municipal
bonds).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 97 February 2025
```

