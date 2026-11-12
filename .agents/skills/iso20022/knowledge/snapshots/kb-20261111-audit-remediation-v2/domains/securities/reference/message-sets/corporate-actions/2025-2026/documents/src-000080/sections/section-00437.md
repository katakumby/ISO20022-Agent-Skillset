---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.7 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.7.4 MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate>"]
file_pages: [589]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.7.4 MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 589 to 589.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 589

```text
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
8.4.12.7.4  MaximumAllowedOversubscriptionRate <MaxAllwdOvrsbcptRate>
Presence: [0..1]
Definition: A maximum percentage of shares available through the over subscription privilege, usually a
percentage of the basic subscription shares, for example, an account owner subscribing to 100 shares
may over subscribe to a maximum of 50 additional shares when the over subscription maximum is 50
percent.
Datatype: "Percentage14Rate" on page 1247
8.4.12.7.5  ProrationRate <PrratnRate>
Presence: [0..1]
Definition: Percentage of securities accepted by the offeror/issuer.
ProrationRate <PrratnRate> contains one of the following elements (see "RateFormat32Choice" on
page 1103 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1104
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1104
8.4.12.7.6  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..*]
Definition: Percentage of a cash distribution that will be withheld by the tax authorities of the jurisdiction
of the issuer, for which a relief at source and/or reclaim may be possible.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 589 February 2026
```

