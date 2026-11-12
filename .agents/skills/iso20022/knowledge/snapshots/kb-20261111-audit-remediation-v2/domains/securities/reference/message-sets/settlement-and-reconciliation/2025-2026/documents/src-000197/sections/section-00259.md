---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.25 SecuritiesFinancingDetails <SctiesFincgDtls>", "10.4.6.25.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>"]
file_pages: [390]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.25.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 390 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
SecuritiesFinancingDetails <SctiesFincgDtls> contains the following
SecuritiesFinancingTransactionDetails54 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 390
   SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 390
   ClosingLegIdentification <ClsgLegId> [0..1] Text 390
   TerminationDate <TermntnDt> [0..1] ± 390
   RateType <RateTp> [0..1] ± 391
   LegalFramework <LglFrmwk> [0..1] ± 391
   MaturityDateModification <MtrtyDtMod> [0..1] Indicator 391
   InterestPayment <IntrstPmt> [0..1] Indicator 391
   VariableRateSupport <VarblRateSpprt> [0..1] ± 392
   RepurchaseRate <RpRate> [0..1] ± C45 392
   TransactionCallDelay <TxCallDely> [0..1] Text 392
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 392
   TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 393
   SecondLegNarrative <ScndLegNrrtv> [0..1] Text 393
10.4.6.25.1  SecuritiesFinancingTradeIdentification <SctiesFincgTradId>
Presence: [0..1]
Definition: Unambiguous identification of the underlying securities financing trade as assigned by the
instructing party. The identification is common to all collateral pieces (one or many).
Datatype: "Max35Text" on page 2192
10.4.6.25.2  SecuritiesFinancingUniqueTransactionIdentifier <SctiesFincgUnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
10.4.6.25.3  ClosingLegIdentification <ClsgLegId>
Presence: [0..1]
Definition: Unambiguous identification of the second leg of the transaction as known by the account
owner (or the instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
10.4.6.25.4  TerminationDate <TermntnDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 390 March 2026
```

