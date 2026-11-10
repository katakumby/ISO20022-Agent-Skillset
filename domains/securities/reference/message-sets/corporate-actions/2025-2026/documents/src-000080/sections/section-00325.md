---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.19 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.19.4 GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>"]
file_pages: [445]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.19.4 GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 445 to 445.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 445

```text
NetDistributionRate <NetDstrbtnRate> contains one of the following elements (see
"NetDividendRateFormat38Choice" on page 926 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 927
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  927
     Amount <Amt> [1..1] Amount C1 927
     RateStatus <RateSts> [1..1] CodeSet 927
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  928
     RateType <RateTp> [1..1]  928
{Or       Code <Cd> [1..1] CodeSet 928
Or}       Proprietary <Prtry> [1..1] ± 929
     Amount <Amt> [1..1] Amount C1 929
     RateStatus <RateSts> [0..1]  C52 930
{Or       Code <Cd> [1..1] CodeSet 930
Or}       Proprietary <Prtry> [1..1] ± 930
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 930
7.4.13.19.4  GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>
Presence: [0..*]
Definition: The actual interest rate before tax used for the payment of the interest for the specified
interest period.
Usage guideline: It is used to provide the applicable rate for the current payment, after all calculations
have been performed, that is, application of period and method of interest computation.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 445 February 2026
```

