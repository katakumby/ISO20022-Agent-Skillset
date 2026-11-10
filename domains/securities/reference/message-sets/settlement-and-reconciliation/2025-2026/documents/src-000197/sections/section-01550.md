---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.18 CancelledStatusReason5Code"]
file_pages: [2049]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.18 CancelledStatusReason5Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2049 to 2049.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2049

```text
35.2.2.18  CancelledStatusReason5Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
OTHR Other Other. See Narrative.
35.2.2.19  CancelledStatusReason9Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
SCEX SecuritiesNoLongerEligible Transaction has been cancelled; the
security no longer exists or is no longer
eligible on the market instructed. For
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
35.2.2.20  CashSettlementSystem3Code
Definition: Specifies the cash settlement system used.
Type: CodeSet
CodeName Name Definition
DCSS DigitalCashSettlementSystem Digital cash settlement system used for
the payment.
GROS GrossSettlementSystem Settle money through gross settlement
system.
NETS NetSettlementSystem Settle money through net settlement
system.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2049 March 2026
```

