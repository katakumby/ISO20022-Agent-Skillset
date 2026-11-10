---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.12 OtherAmounts <OthrAmts>"]
file_pages: [1204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.12 OtherAmounts <OthrAmts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1204 to 1204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1204

```text
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection95" on
page 1362 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 1363
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 1363
   BrokerageAmountIndicator <BrkrgAmtInd> [0..1] Indicator 1363
   ResearchFeeIndicator <RsrchFeeInd> [0..1] Indicator 1363
   Amount <Amt> [0..1] Amount C1, C9 1363
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1364
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1364
   ForeignExchangeDetails <FXDtls> [0..1] ± 1364
   ValueDate <ValDt> [0..1] ± 1365
32.4.2.1.12  OtherAmounts <OthrAmts>
Presence: [0..1]
Definition: Other amounts than the settlement amount.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1204 March 2026
```

