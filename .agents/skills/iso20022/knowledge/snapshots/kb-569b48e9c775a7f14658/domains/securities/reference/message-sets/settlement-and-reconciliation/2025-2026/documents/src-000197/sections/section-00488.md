---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>", "22.4.9.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>"]
file_pages: [749]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.9.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 749 to 749.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 749

```text
SecuritiesFinancingDetails <SctiesFincgDtls> contains the following
SecuritiesFinancingTransactionDetails55 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 749
   SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 749
   ClosingLegIdentification <ClsgLegId> [0..1] Text 749
   TerminationDate <TermntnDt> [0..1] ± 750
   RateType <RateTp> [0..1] ± 750
   LegalFramework <LglFrmwk> [0..1] ± 750
   MaturityDateModification <MtrtyDtMod> [0..1] Indicator 750
   InterestPayment <IntrstPmt> [0..1] Indicator 751
   VariableRateSupport <VarblRateSpprt> [0..1] ± 751
   RepurchaseRate <RpRate> [0..1] ± C45 751
   TransactionCallDelay <TxCallDely> [0..1] Text 751
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 751
   TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 752
   SecondLegNarrative <ScndLegNrrtv> [0..1] Text 752
22.4.9.1  SecuritiesFinancingTradeIdentification <SctiesFincgTradId>
Presence: [0..1]
Definition: Unambiguous identification of the underlying securities financing trade as assigned by the
instructing party. The identification is common to all collateral pieces (one or many).
Datatype: "Max35Text" on page 2192
22.4.9.2  SecuritiesFinancingUniqueTransactionIdentifier <SctiesFincgUnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
22.4.9.3  ClosingLegIdentification <ClsgLegId>
Presence: [0..1]
Definition: Unambiguous identification of the second leg of the transaction as known by the account
owner (or the instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 749 March 2026
```

