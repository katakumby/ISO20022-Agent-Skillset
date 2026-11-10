---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.47 GatingOrHoldBackDetails <GtgOrHldBckDtls>"]
file_pages: [2047]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.47 GatingOrHoldBackDetails <GtgOrHldBckDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2047 to 2047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2047

```text
Definition: Information about a non-standard order.
Impacted by: C40 "WaiverElementRule"
OrderWaiverDetails <OrdrWvrDtls> contains the following elements (see "OrderWaiver1" on
page 4782 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderWaiverReason <OrdrWvrRsn> [0..*]  4782
{Or     Code <Cd> [1..1] CodeSet 4782
Or}     Proprietary <Prtry> [1..1] ± 4783
   InformationValue <InfVal> [0..1] Text 4783
Constraints
• WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
43.4.5.9.47  GatingOrHoldBackDetails <GtgOrHldBckDtls>
Presence: [0..1]
Definition: Information about gating and hold back of redemption proceeds.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2047 May 2026
```

