---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.99 SettlementStatus34Choice"]
file_pages: [2027]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.99 SettlementStatus34Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2027 to 2027.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2027

```text
35.1.29.99  SettlementStatus34Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  2027
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2027
Or}     Reason <Rsn> [1..*] ± 2027
Or   Failing <Flng> [1..1]  2028
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2028
Or}     Reason <Rsn> [1..*] ± 2028
Or}   Proprietary <Prtry> [1..1] ± 2028
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
35.1.29.99.1  Pending <Pdg>
Presence: [1..1]
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following PendingStatus79Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2027
Or}   Reason <Rsn> [1..*] ± 2027
35.1.29.99.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.99.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2027 March 2026
```

