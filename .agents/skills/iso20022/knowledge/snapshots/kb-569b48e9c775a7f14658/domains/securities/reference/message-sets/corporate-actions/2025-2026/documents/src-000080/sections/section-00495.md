---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.7 GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>"]
file_pages: [655]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.7 GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 655 to 655.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 655

```text
ThirdPartyIncentiveRate <ThrdPtyIncntivRate> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
8.4.12.11.14.7  GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>
Presence: [0..*]
Definition: Actual interest rate before tax used for the payment of the interest for the specified interest
period.
GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt> contains one of the following
elements (see "InterestRateUsedForPaymentFormat12Choice" on page 1107 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1107
Or   Amount <Amt> [1..1] Amount C1 1107
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  1108
     RateType <RateTp> [1..1]  1108
{Or       Code <Cd> [1..1] CodeSet 1108
Or}       Proprietary <Prtry> [1..1] ± 1109
     Amount <Amt> [1..1] Amount C1 1109
     RateStatus <RateSts> [0..1]  C52 1109
{Or       Code <Cd> [1..1] CodeSet 1109
Or}       Proprietary <Prtry> [1..1] ± 1110
8.4.12.11.14.8  NetDistributionRate <NetDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate after tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 655 February 2026
```

