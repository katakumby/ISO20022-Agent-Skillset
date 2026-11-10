---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.21 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.21.3 NetDistributionRate <NetDstrbtnRate>"]
file_pages: [158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.21.3 NetDistributionRate <NetDstrbtnRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 158 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 158

```text
GrossDistributionRate <GrssDstrbtnRate> contains one of the following elements (see
"GrossDividendRateFormat36Choice" on page 949 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 949
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  950
     Amount <Amt> [1..1] Amount C1 950
     RateStatus <RateSts> [1..1] CodeSet 950
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  950
     RateType <RateTp> [1..1]  951
{Or       Code <Cd> [1..1] CodeSet 951
Or}       Proprietary <Prtry> [1..1] ± 952
     Amount <Amt> [1..1] Amount C1 952
     RateStatus <RateSts> [0..1]  C52 952
{Or       Code <Cd> [1..1] CodeSet 953
Or}       Proprietary <Prtry> [1..1] ± 953
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 953
3.4.11.21.3  NetDistributionRate <NetDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate after tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 158 February 2026
```

