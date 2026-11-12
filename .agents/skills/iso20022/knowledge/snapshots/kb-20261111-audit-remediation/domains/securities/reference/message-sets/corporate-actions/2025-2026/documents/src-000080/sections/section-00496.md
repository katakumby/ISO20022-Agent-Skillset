---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.9 ApplicableRate <AplblRate>"]
file_pages: [656]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.9 ApplicableRate <AplblRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 656 to 656.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 656

```text
NetDistributionRate <NetDstrbtnRate> contains one of the following elements (see
"NetDividendRateFormat40Choice" on page 900 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 901
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  901
     Amount <Amt> [1..1] Amount C1 902
     RateStatus <RateSts> [1..1] CodeSet 902
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  902
     RateType <RateTp> [1..1]  902
{Or       Code <Cd> [1..1] CodeSet 903
Or}       Proprietary <Prtry> [1..1] ± 903
     Amount <Amt> [1..1] Amount C1 904
     RateStatus <RateSts> [0..1]  C52 904
{Or       Code <Cd> [1..1] CodeSet 904
Or}       Proprietary <Prtry> [1..1] ± 905
8.4.12.11.14.9  ApplicableRate <AplblRate>
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
8.4.12.11.14.10  SolicitationFeeRate <SlctnFeeRate>
Presence: [0..1]
Definition: Rate of the cash premium made available if the securities holder consents or participates to
an event, for example consent fees or solicitation fee.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 656 February 2026
```

