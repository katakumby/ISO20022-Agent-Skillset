---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks"]
file_pages: [2118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C30", "C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39"], "until_heading": "44.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 2118, "topic": "44.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01517.md"}]
---

# 44.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2118 to 2118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 2118, C30–C39 before **44.4 Message Building Blocks** continue [44.3 Constraints](section-01517.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 2118

```text
C30 PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
C31 ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present.
If ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
C32 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C33 RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in
SettlementAmount, if present.
C34 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C35 SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualOrderDetails/
SettlementAmount, if present, must be the same in all occurrences of IndividualOrderDetails.
C36 StandardFeeAmountCalculation
If StandardAmount, RequestedAmount and DiscountDetails/Amount are all present, then
StandardAmount minus DiscountDetails/Amount must equal RequestedAmount.
C37 StandardFeeRateCalculation
If StandardRate, RequestedRate and DiscountDetails/Rate are all present, then StandardRate
minus DiscountDetails/Rate must equal RequestedRate.
C38 TotalSettlementCurrencyRule
If TotalSettlementAmount is present, then Currency in IndividualOrderDetails/
SettlementAmount, if present, must be the same in all occurrences of IndividualOrderDetails.
C39 WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
44.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
44.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2118 May 2026
```

