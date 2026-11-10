---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.18 CorporateActionRate122", "16.1.22.18.2 PercentageSought <PctgSght>"]
file_pages: [1127]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.18.2 PercentageSought <PctgSght>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1127 to 1127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1127

```text
Definition: Annualised interest rate of a financial instrument used to calculate the actual interest rate of
the coupon or the accrued interest.
InterestRate <IntrstRate> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
16.1.22.18.2  PercentageSought <PctgSght>
Presence: [0..1]
Definition: Percentage of securities the offeror/issuer will purchase or redeem under the terms of the
event.
PercentageSought <PctgSght> contains one of the following elements (see "RateFormat25Choice"
on page 1122 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1122
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
16.1.22.18.3  RelatedIndex <RltdIndx>
Presence: [0..1]
Definition: Index rate related to the interest rate of the forthcoming interest payment.
RelatedIndex <RltdIndx> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
16.1.22.18.4  Spread <Sprd>
Presence: [0..1]
Definition: Margin allowed over or under a given rate.
Spread <Sprd> contains one of the following elements (see "RateFormat24Choice" on page 1098 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1127 February 2026
```

