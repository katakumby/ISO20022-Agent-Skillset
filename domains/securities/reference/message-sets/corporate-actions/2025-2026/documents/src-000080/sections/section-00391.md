---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.13 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.23.13.11 ApplicableRate <AplblRate>"]
file_pages: [520]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.13.11 ApplicableRate <AplblRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 520 to 520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 520

```text
NetDistributionRate <NetDstrbtnRate> contains one of the following elements (see
"NetDividendRateFormat39Choice" on page 959 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 959
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  959
     Amount <Amt> [1..1] Amount C1 960
     RateStatus <RateSts> [1..1] CodeSet 960
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  960
     RateType <RateTp> [1..1]  961
{Or       Code <Cd> [1..1] CodeSet 961
Or}       Proprietary <Prtry> [1..1] ± 962
     Amount <Amt> [1..1] Amount C1 962
     RateStatus <RateSts> [0..1]  C52 962
{Or       Code <Cd> [1..1] CodeSet 963
Or}       Proprietary <Prtry> [1..1] ± 963
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 963
7.4.13.23.13.11  ApplicableRate <AplblRate>
Presence: [0..1]
Definition: Rate applicable to the event announced, for example, redemption rate for a redemption
event.
ApplicableRate <AplblRate> contains one of the following elements (see "RateFormat31Choice" on
page 1104 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1104
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1104
Or}   Amount <Amt> [1..1] Amount C1 1105
7.4.13.23.13.12  SolicitationFeeRate <SlctnFeeRate>
Presence: [0..1]
Definition: Rate of the cash premium made available if the securities holder consents or participates to
an event, for example consent fees or solicitation fee.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 520 February 2026
```

