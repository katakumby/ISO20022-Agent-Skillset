---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.11 SettlementDetails221", "35.1.26.11.1 Priority <Prty>"]
file_pages: [1852]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.11.1 Priority <Prty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1852 to 1852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1852

```text
35.1.26.11.1  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction was executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 1541 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 1541
Or}   Proprietary <Prtry> [1..1] ± 1541
35.1.26.11.2  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType43Choice" on page 1584 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1584
Or}   Proprietary <Prtry> [1..1] ± 1587
35.1.26.11.3  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade was to be settled.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition41Choice" on page 1641 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1641
Or}   Proprietary <Prtry> [1..1] ± 1642
35.1.26.11.4  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement was allowed.
Datatype: "SettlementTransactionCondition5Code" on page 2170
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1852 March 2026
```

