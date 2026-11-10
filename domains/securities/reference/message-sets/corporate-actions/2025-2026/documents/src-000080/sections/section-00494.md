---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.5 EarlySolicitationFeeRate <EarlySlctnFeeRate>"]
file_pages: [654]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.5 EarlySolicitationFeeRate <EarlySlctnFeeRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 654 to 654.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 654

```text
GrossDistributionRate <GrssDstrbtnRate> contains one of the following elements (see
"GrossDividendRateFormat37Choice" on page 909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 909
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  910
     Amount <Amt> [1..1] Amount C1 910
     RateStatus <RateSts> [1..1] CodeSet 910
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  910
     RateType <RateTp> [1..1]  911
{Or       Code <Cd> [1..1] CodeSet 911
Or}       Proprietary <Prtry> [1..1] ± 912
     Amount <Amt> [1..1] Amount C1 912
     RateStatus <RateSts> [0..1]  C52 913
{Or       Code <Cd> [1..1] CodeSet 913
Or}       Proprietary <Prtry> [1..1] ± 913
8.4.12.11.14.5  EarlySolicitationFeeRate <EarlySlctnFeeRate>
Presence: [0..1]
Definition: Cash rate made available, as an incentive, in addition to the solicitation fee, in order to
encourage early participation in an offer.
EarlySolicitationFeeRate <EarlySlctnFeeRate> contains one of the following elements (see
"SolicitationFeeRateFormat12Choice" on page 1105 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1105
Or   AmountToQuantity <AmtToQty> [1..1]  1105
     Amount <Amt> [1..1] Amount C1 1106
     Quantity <Qty> [1..1] Quantity 1106
Or}   Amount <Amt> [1..1] Amount C1 1106
8.4.12.11.14.6  ThirdPartyIncentiveRate <ThrdPtyIncntivRate>
Presence: [0..1]
Definition: Cash rate made available in an event in order to encourage participation in the offer. As
information, Payment is made to a third party who has solicited an entity to take part in the offer.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 654 February 2026
```

