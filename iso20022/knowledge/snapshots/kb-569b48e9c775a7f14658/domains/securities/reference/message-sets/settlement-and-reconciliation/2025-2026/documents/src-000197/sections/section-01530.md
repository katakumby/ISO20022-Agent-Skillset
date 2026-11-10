---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.99 SettlementStatus34Choice", "35.1.29.99.2 Failing <Flng>"]
file_pages: [2028]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.99.2 Failing <Flng>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2028 to 2028.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2028

```text
Reason <Rsn> contains the following elements (see "PendingReason34" on page 2025 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2025
{Or     Code <Cd> [1..1] CodeSet 2026
Or}     Proprietary <Prtry> [1..1] ± 2026
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2026
35.1.29.99.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following FailingStatus17Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2028
Or}   Reason <Rsn> [1..*] ± 2028
35.1.29.99.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.99.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following elements (see "FailingReason15" on page 2029 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2029
{Or     Code <Cd> [1..1] CodeSet 2029
Or}     Proprietary <Prtry> [1..1] ± 2030
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2030
35.1.29.99.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2028 March 2026
```

