---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.13 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.23.13.4 WithholdingTaxRate <WhldgTaxRate>"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.13.4 WithholdingTaxRate <WhldgTaxRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
Usage guideline: It is used to provide the applicable rate for the current payment, after all calculations
have been performed, that is, application of period and method of interest computation.
GrossInterestRateUsedForPayment <GrssIntrstRateUsdForPmt> contains one of the following
elements (see "InterestRateUsedForPaymentFormat11Choice" on page 1028 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1029
Or   Amount <Amt> [1..1] Amount C1 1029
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  1029
     RateType <RateTp> [1..1]  1029
{Or       Code <Cd> [1..1] CodeSet 1030
Or}       Proprietary <Prtry> [1..1] ± 1030
     Amount <Amt> [1..1] Amount C1 1030
     RateStatus <RateSts> [0..1]  C52 1030
{Or       Code <Cd> [1..1] CodeSet 1031
Or}       Proprietary <Prtry> [1..1] ± 1031
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1031
7.4.13.23.13.4  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..*]
Definition: Percentage of a cash distribution that will be withheld by the tax authorities of the jurisdiction
of the issuer, for which a relief at source and/or reclaim may be possible.
WithholdingTaxRate <WhldgTaxRate> contains one of the following elements (see
"RateAndAmountFormat56Choice" on page 886 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 886
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 886
Or   Amount <Amt> [1..1] Amount C1 886
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  887
     RateType <RateTp> [1..1]  887
{Or       Code <Cd> [1..1] CodeSet 887
Or}       Proprietary <Prtry> [1..1] ± 888
     Rate <Rate> [1..1] Rate 888
7.4.13.23.13.5  SecondLevelTax <ScndLvlTax>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 517 February 2026
```

