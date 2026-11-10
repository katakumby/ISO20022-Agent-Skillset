---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.79 PendingProcessingStatus13Choice", "35.1.29.79.2 Reason <Rsn>"]
file_pages: [1999]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.79.2 Reason <Rsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1999 to 1999.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1999

```text
35.1.29.79.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Reason <Rsn> contains the following PendingProcessingReason10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1999
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1999
35.1.29.79.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Code <Cd> contains one of the following elements (see "PendingProcessingReason12Choice" on
page 1980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1980
Or}   Proprietary <Prtry> [1..1] ± 1981
35.1.29.79.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.80  CancellationReason23
Definition: Specifies the reason why the instruction or request is cancelled.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1999
{Or     Code <Cd> [1..1] CodeSet 2000
Or}     Proprietary <Prtry> [1..1] ± 2000
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2001
35.1.29.80.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction is cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1999 March 2026
```

