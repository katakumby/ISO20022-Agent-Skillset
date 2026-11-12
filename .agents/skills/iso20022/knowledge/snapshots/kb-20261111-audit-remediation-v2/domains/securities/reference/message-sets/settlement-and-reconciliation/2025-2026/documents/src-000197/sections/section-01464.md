---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.47 RejectionOrRepairStatus43Choice", "35.1.29.47.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [1952]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.47.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1952 to 1952.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1952

```text
35.1.29.47.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.47.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason for the status.
Reason <Rsn> contains the following RejectionOrRepairReason38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1952
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1952
35.1.29.47.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following elements (see "RejectionAndRepairReason38Choice" on
page 1933 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1934
Or}   Proprietary <Prtry> [1..1] ± 1934
35.1.29.47.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.48  SettlementStatus30Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1] ± 1953
Or   Failing <Flng> [1..1] ± 1953
Or}   Proprietary <Prtry> [1..1] ± 1953
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1952 March 2026
```

