---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks"]
file_pages: [1911]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C34", "C35", "C36", "C37", "C38", "C39", "C40"], "until_heading": "43.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1911, "topic": "43.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01367.md"}]
---

# 43.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1911 to 1911.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 1911, C34–C40 before **43.4 Message Building Blocks** continue [43.3 Constraints](section-01367.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 1911

```text
C34 ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be
present. If ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is
optional.
C35 RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences
of IndividualExecutionDetails/SettlementAmount.
C36 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
C37 SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualExecutionDetails/
SettlementAmount must be the same in all occurrences of IndividualExecutionDetails.
C38 TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
C39 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
C40 WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
43.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
43.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
43.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1911 May 2026
```

