---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.13 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.23.13.8 FiscalStamp <FsclStmp>"]
file_pages: [519]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.13.8 FiscalStamp <FsclStmp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 519 to 519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

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
7.4.13.23.13.8  FiscalStamp <FsclStmp>
Presence: [0..1]
Definition: Percentage of fiscal tax to apply.
FiscalStamp <FsclStmp> contains one of the following elements (see "RateFormat24Choice" on
page 1098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1098
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1098
7.4.13.23.13.9  ThirdPartyIncentiveRate <ThrdPtyIncntivRate>
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
7.4.13.23.13.10  NetDistributionRate <NetDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate after tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 519 February 2026
```

