---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.84 CancellationReason23Choice", "35.1.29.84.2 Proprietary <Prtry>"]
file_pages: [2009]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.84.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2009 to 2009.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2009

```text
CodeName Name Definition
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
35.1.29.84.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.85  RejectionAndRepairReason36Choice
Definition: Choice of format for the rejection or repair reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2009
Or}   Proprietary <Prtry> [1..1] ± 2010
35.1.29.85.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2009 March 2026
```

