---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.21 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.21.5 MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate>"]
file_pages: [160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.21.5 MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 160 to 160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 160

```text
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
3.4.11.21.5  MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate>
Presence: [0..1]
Definition: Maximum percentage of shares available through the over subscription privilege, usually a
percentage of the basic subscription shares, for example, an account owner subscribing to 100 shares
may over subscribe to a maximum of 50 additional shares when the over subscription maximum is 50
percent.
MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate> contains one of the following
elements (see "RateFormat24Choice" on page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.21.6  ProrationRate <PrratnRate>
Presence: [0..1]
Definition: Percentage of securities accepted by the offeror/issuer.
ProrationRate <PrratnRate> contains one of the following elements (see "RateFormat32Choice" on
page 1103 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1104
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1104
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 160 February 2026
```

