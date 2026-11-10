---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.27 CancellationStatus24Choice", "35.1.29.27.2 Reason <Rsn>"]
file_pages: [1923]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.27.2 Reason <Rsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1923 to 1923.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1923

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.27.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the cancellation status.
Reason <Rsn> contains the following CancellationReason22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1923
{Or     Code <Cd> [1..1] CodeSet 1923
Or}     Proprietary <Prtry> [1..1] ± 1924
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1924
35.1.29.27.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction is cancelled.
Code <Cd> contains one of the following CancellationReason36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1923
Or}   Proprietary <Prtry> [1..1] ± 1924
35.1.29.27.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Datatype: "CancelledStatusReason16Code" on page 2048
CodeName Name Definition
SCEX SecuritiesNoLongerEligible Transaction has been cancelled; the
security no longer exists or is no longer
eligible on the market instructed. For
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
BYIY CancelledDueToBuyIn Instruction has been cancelled because
a buy-in has been initiated.
CTHP CancelledByThirdParty Instruction is cancelled by a Third party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1923 March 2026
```

