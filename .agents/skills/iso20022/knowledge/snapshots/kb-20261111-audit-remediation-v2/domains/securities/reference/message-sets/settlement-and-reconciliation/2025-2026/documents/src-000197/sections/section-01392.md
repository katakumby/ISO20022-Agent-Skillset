---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.1 SettlementStatus32Choice", "35.1.29.1.1 Pending <Pdg>"]
file_pages: [1861]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.1.1 Pending <Pdg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1861 to 1861.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1861

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  1861
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1862
Or}     Reason <Rsn> [1..*]  1862
       Code <Cd> [1..1]  1862
{Or         Code <Cd> [1..1] CodeSet 1862
Or}         Proprietary <Prtry> [1..1] ± 1865
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1866
Or   Failing <Flng> [1..1]  1866
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1866
Or}     Reason <Rsn> [1..*]  1866
       Code <Cd> [1..1]  1867
{Or         Code <Cd> [1..1] CodeSet 1867
Or}         Proprietary <Prtry> [1..1] ± 1870
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1871
Or}   Proprietary <Prtry> [1..1] ± 1871
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
35.1.29.1.1  Pending <Pdg>
Presence: [1..1]
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following PendingStatus73Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1862
Or}   Reason <Rsn> [1..*]  1862
     Code <Cd> [1..1]  1862
{Or       Code <Cd> [1..1] CodeSet 1862
Or}       Proprietary <Prtry> [1..1] ± 1865
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1866
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1861 March 2026
```

