---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.14 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.25.14.8 FiscalStamp <FsclStmp>"]
file_pages: [239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.14.8 FiscalStamp <FsclStmp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 239 to 239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 239

```text
EarlySolicitationFeeRate <EarlySlctnFeeRate> contains one of the following elements (see
"SolicitationFeeRateFormat11Choice" on page 1024 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1024
Or   AmountToQuantity <AmtToQty> [1..1]  1025
     Amount <Amt> [1..1] Amount C1 1025
     Quantity <Qty> [1..1] Quantity 1025
Or   Amount <Amt> [1..1] Amount C1 1025
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1026
3.4.11.25.14.8  FiscalStamp <FsclStmp>
Presence: [0..1]
Definition: Percentage of fiscal tax to apply.
FiscalStamp <FsclStmp> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
3.4.11.25.14.9  ThirdPartyIncentiveRate <ThrdPtyIncntivRate>
Presence: [0..1]
Definition: Cash rate made available in an event in order to encourage participation in the offer. As
information, payment is made to a third party who has solicited an entity to take part in the offer.
ThirdPartyIncentiveRate <ThrdPtyIncntivRate> contains one of the following elements (see
"RateFormat26Choice" on page 1120 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1120
Or   Amount <Amt> [1..1] Amount C1 1120
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1120
3.4.11.25.14.10  NetDistributionRate <NetDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate after tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 239 February 2026
```

