---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.77 RejectionStatus30Choice"]
file_pages: [1993]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.77 RejectionStatus30Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1993 to 1993.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1993

```text
Definition: Pending status of an instruction, advice or request.
Pending <Pdg> contains one of the following elements (see "PendingStatus20Choice" on page 1899
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Forwarded <Fwdd> [1..1] ± 1900
Or}   UnderInvestigation <UdrInvstgtn> [1..1] ± 1900
35.1.29.77  RejectionStatus30Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1993
Or}   Reason <Rsn> [1..*]  1993
     Code <Cd> [1..1]  1994
{Or       Code <Cd> [1..1] CodeSet 1994
Or}       Proprietary <Prtry> [1..1] ± 1994
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1995
35.1.29.77.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.77.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection status.
Reason <Rsn> contains the following RejectionReason49 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1994
{Or     Code <Cd> [1..1] CodeSet 1994
Or}     Proprietary <Prtry> [1..1] ± 1994
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1995
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1993 March 2026
```

