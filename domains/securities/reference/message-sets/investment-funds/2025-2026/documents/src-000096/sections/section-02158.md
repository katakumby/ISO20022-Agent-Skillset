---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks"]
file_pages: [3021]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3021 to 3021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3021

```text
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
50.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
50.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
50.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3021 May 2026
```

