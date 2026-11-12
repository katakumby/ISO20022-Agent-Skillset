---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.80 CancellationReason23", "35.1.29.80.1 Code <Cd>", "35.1.29.80.1.1 Code <Cd>"]
file_pages: [2000]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.80.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2000 to 2000.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2000

```text
Code <Cd> contains one of the following CancellationReason36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2000
Or}   Proprietary <Prtry> [1..1] ± 2000
35.1.29.80.1.1  Code <Cd>
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
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CANS CancelledBySystem Transaction is cancelled by the system.
CANI CancelledByYourself Transaction is cancelled by yourself.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
35.1.29.80.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2000 March 2026
```

