---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.13 OtherAmounts <OthrAmts>"]
file_pages: [859]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.13 OtherAmounts <OthrAmts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 859 to 859.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 859

```text
26.4.12 SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities.
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection94" on
page 1365 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 1365
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 1366
   BrokerageAmountIndicator <BrkrgAmtInd> [0..1] Indicator 1366
   ResearchFeeIndicator <RsrchFeeInd> [0..1] Indicator 1366
   Amount <Amt> [1..1] Amount C1, C9 1366
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1367
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1367
   ForeignExchangeDetails <FXDtls> [0..1] ± 1367
   ValueDate <ValDt> [0..1] ± 1368
26.4.13 OtherAmounts <OthrAmts>
Presence: [0..1]
Definition: Other amounts than the settlement amount.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 859 March 2026
```

