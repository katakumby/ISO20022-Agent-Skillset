---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.9 SettlementStatus18Choice", "35.1.29.9.1 Pending <Pdg>"]
file_pages: [1883]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.9.1 Pending <Pdg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1883 to 1883.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1883

```text
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
35.1.29.9.1  Pending <Pdg>
Presence: [1..1]
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following elements (see "PendingStatus40Choice" on page 1984
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1984
Or}   Reason <Rsn> [1..*]  1984
     Code <Cd> [1..1] ± 1985
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1985
35.1.29.9.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following FailingStatus10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1883
Or}   Reason <Rsn> [1..*]  1884
     Code <Cd> [1..1]  1884
{Or       Code <Cd> [1..1] CodeSet 1884
Or}       Proprietary <Prtry> [1..1] ± 1887
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1888
35.1.29.9.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1883 March 2026
```

