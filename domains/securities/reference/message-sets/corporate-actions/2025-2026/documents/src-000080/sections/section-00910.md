---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.18 CorporateActionRate122", "16.1.22.18.5 BidInterval <BidIntrvl>"]
file_pages: [1128]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.18.5 BidInterval <BidIntrvl>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1128 to 1128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1128

```text
16.1.22.18.5  BidInterval <BidIntrvl>
Presence: [0..1]
Definition: Acceptable price increment used for submitting a bid.
BidInterval <BidIntrvl> contains one of the following elements (see "RateAndAmountFormat58Choice"
on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1122
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1122
Or   Amount <Amt> [1..1] Amount C1 1122
Or}   IndexPoints <IndxPts> [1..1] Quantity 1122
16.1.22.18.6  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) until the next redemption (factor) date.
PreviousFactor <PrvsFctr> contains one of the following elements (see "RateFormat12Choice" on
page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
16.1.22.18.7  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) that will applicable after the redemption (factor) date.
NextFactor <NxtFctr> contains one of the following elements (see "RateFormat12Choice" on
page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
16.1.22.18.8  ReinvestmentDiscountRateToMarket <RinvstmtDscntRateToMkt>
Presence: [0..1]
Definition: Rate of discount for securities purchased through a reinvestment scheme as compared to
the current market price of security.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1128 February 2026
```

