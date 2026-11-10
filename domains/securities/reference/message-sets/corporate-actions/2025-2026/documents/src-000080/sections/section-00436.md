---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.7 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.7.2 NetDistributionRate <NetDstrbtnRate>"]
file_pages: [588]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.7.2 NetDistributionRate <NetDstrbtnRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 588 to 588.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 588

```text
8.4.12.7.2  NetDistributionRate <NetDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate after tax has been deducted.
NetDistributionRate <NetDstrbtnRate> contains one of the following elements (see
"NetDividendRateFormat37Choice" on page 895 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 895
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  896
     Amount <Amt> [1..1] Amount C1 896
     RateStatus <RateSts> [1..1] CodeSet 896
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  896
     RateType <RateTp> [1..1]  897
{Or       Code <Cd> [1..1] CodeSet 897
Or}       Proprietary <Prtry> [1..1] ± 898
     Amount <Amt> [1..1] Amount C1 898
     RateStatus <RateSts> [0..1]  C52 898
{Or       Code <Cd> [1..1] CodeSet 899
Or}       Proprietary <Prtry> [1..1] ± 899
8.4.12.7.3  GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>
Presence: [0..*]
Definition: Actual interest rate before tax used for the payment of the interest for the specified interest
period.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 588 February 2026
```

