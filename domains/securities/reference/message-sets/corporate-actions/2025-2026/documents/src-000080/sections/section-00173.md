---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.14 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.25.14.6 ChargesFees <ChrgsFees>"]
file_pages: [238]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.14.6 ChargesFees <ChrgsFees>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 238 to 238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
Definition: Rate at which the income will be withheld by a jurisdiction other than the jurisdiction of the
issuer's country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is
levied in complement or offset of the withholding tax rate (TAXR) levied by the jurisdiction of the issuer's
tax domicile.
SecondLevelTax <ScndLvlTax> contains one of the following elements (see
"RateAndAmountFormat60Choice" on page 1026 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1026
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1026
Or   Amount <Amt> [1..1] Amount C1 1026
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1027
     RateType <RateTp> [1..1]  1027
{Or       Code <Cd> [1..1] CodeSet 1027
Or}       Proprietary <Prtry> [1..1] ± 1028
     Rate <Rate> [1..1] Rate 1028
3.4.11.25.14.6  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charges/fees that cannot be categorised.
ChargesFees <ChrgsFees> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
3.4.11.25.14.7  EarlySolicitationFeeRate <EarlySlctnFeeRate>
Presence: [0..1]
Definition: Cash rate made available, as an incentive, in addition to the solicitation fee, in order to
encourage early participation in an offer.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 238 February 2026
```

