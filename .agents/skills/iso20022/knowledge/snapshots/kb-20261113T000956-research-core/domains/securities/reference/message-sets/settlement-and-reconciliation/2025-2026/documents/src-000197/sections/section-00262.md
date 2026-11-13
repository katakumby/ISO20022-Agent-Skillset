---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.25 SecuritiesFinancingDetails <SctiesFincgDtls>", "10.4.6.25.13 TerminationTransactionAmount <TermntnTxAmt>"]
file_pages: [393]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.25.13 TerminationTransactionAmount <TermntnTxAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 393 to 393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 393

```text
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
10.4.6.25.13  TerminationTransactionAmount <TermntnTxAmt>
Presence: [0..1]
Definition: Total amount of money to be settled to terminate the transaction.
TerminationTransactionAmount <TermntnTxAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
10.4.6.25.14  SecondLegNarrative <ScndLegNrrtv>
Presence: [0..1]
Definition: Provides additional information about the second leg in narrative form.
Datatype: "Max140Text" on page 2191
10.4.6.26  SettlementParameters <SttlmParams>
Presence: [1..1]
Definition: Parameters applied to the settlement of a security transfer.
Impacted by: C10 "CashClearingSystemRule", C44 "SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 393 March 2026
```

