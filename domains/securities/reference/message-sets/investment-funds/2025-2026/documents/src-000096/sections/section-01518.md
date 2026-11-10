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
---

# 44.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2118 to 2118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

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

