---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks"]
file_pages: [2329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2329 to 2329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2329

```text
C32 PriceDifferenceReasonRule
Any occurrence of InformativePriceDetails/PriceDifferenceReason may not be present.
C33 ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present.
If ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
C34 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C35 RedemptionEqualisationMethodologyTypes1Rule
Contingent Liquidation and Depreciation Deposit are mutually exclusive.
C36 RedemptionEqualisationMethodologyTypes2Rule
Contingent Liquidation and Depreciation Deposit are mutually exclusive.
C37 RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in
SettlementAmount, if present.
C38 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C39 SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualExecutionDetails/
SettlementAmount must be the same in all occurrences of IndividualExecutionDetails.
C40 TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
C41 TotalSettlementCurrencyRule
If TotalSettlementAmount is present, then Currency in IndividualExecutionDetails/
SettlementAmount, must be the same in all occurrences of IndividualExecutionDetails.
C42 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
C43 WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
46.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
46.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2329 May 2026
```

