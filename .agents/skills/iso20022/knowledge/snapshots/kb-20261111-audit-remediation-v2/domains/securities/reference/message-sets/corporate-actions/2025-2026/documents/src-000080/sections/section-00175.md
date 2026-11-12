---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.14 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.25.14.11 ApplicableRate <AplblRate>"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.14.11 ApplicableRate <AplblRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

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
3.4.11.25.14.11  ApplicableRate <AplblRate>
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
3.4.11.25.14.12  SolicitationFeeRate <SlctnFeeRate>
Presence: [0..1]
Definition: Rate of the cash premium made available if the securities holder consents or participates to
an event, for example consent fees or solicitation fee.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 240 February 2026
```

