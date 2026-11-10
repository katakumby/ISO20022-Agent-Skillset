---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.18 CorporateActionRate122", "16.1.22.18.9 InterestShortfall <IntrstShrtfll>"]
file_pages: [1129]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.18.9 InterestShortfall <IntrstShrtfll>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1129 to 1129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1129

```text
ReinvestmentDiscountRateToMarket <RinvstmtDscntRateToMkt> contains one of the following
elements (see "RateFormat24Choice" on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
16.1.22.18.9  InterestShortfall <IntrstShrtfll>
Presence: [0..1]
Definition: For structured security issues where there is a set schedule of principal and interest
payments for the life of the issue, this is the difference between the actual rate of the interest payment
and the expected or scheduled rate of the interest payment.
InterestShortfall <IntrstShrtfll> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
16.1.22.18.10  RealisedLoss <RealsdLoss>
Presence: [0..1]
Definition: For structured security issues where there is a set schedule of principal and interest
payments for the life of the issue, this is the difference between the actual rate of the capital or principal
repayment and the scheduled capital repayment.
RealisedLoss <RealsdLoss> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
16.1.22.18.11  DeclaredRate <DclrdRate>
Presence: [0..1]
Definition: Dividend or interest rate declared by the issuer.
DeclaredRate <DclrdRate> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1129 February 2026
```

