---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.13 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.23.13.1 AdditionalTax <AddtlTax>"]
file_pages: [516]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.13.1 AdditionalTax <AddtlTax>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 516 to 516.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 516

```text
7.4.13.23.13.1  AdditionalTax <AddtlTax>
Presence: [0..1]
Definition: Rate used for additional tax that cannot be categorised.
AdditionalTax <AddtlTax> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
7.4.13.23.13.2  GrossDistributionRate <GrssDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate before tax has been deducted.
GrossDistributionRate <GrssDstrbtnRate> contains one of the following elements (see
"GrossDividendRateFormat38Choice" on page 936 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 937
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  937
     Amount <Amt> [1..1] Amount C1 938
     RateStatus <RateSts> [1..1] CodeSet 938
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  938
     RateType <RateTp> [1..1]  938
{Or       Code <Cd> [1..1] CodeSet 939
Or}       Proprietary <Prtry> [1..1] ± 940
     Amount <Amt> [1..1] Amount C1 940
     RateStatus <RateSts> [0..1]  C52 940
{Or       Code <Cd> [1..1] CodeSet 940
Or}       Proprietary <Prtry> [1..1] ± 941
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 941
7.4.13.23.13.3  GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt>
Presence: [0..*]
Definition: The actual interest rate before tax used for the payment of the interest for the specified
interest period.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 516 February 2026
```

