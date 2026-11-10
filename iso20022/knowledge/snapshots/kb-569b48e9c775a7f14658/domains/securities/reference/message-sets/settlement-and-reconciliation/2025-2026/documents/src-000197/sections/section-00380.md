---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.3.6 PendingCancellation <PdgCxl>"]
file_pages: [573]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.3.6 PendingCancellation <PdgCxl>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 573 to 573.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 573

```text
Cancelled <Canc> contains one of the following elements (see "CancellationStatus24Choice" on
page 1922 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1922
Or}   Reason <Rsn> [1..*]  1923
     Code <Cd> [1..1]  1923
{Or       Code <Cd> [1..1] CodeSet 1923
Or}       Proprietary <Prtry> [1..1] ± 1924
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1924
18.4.3.6  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation request from yourself for this instruction is pending, waiting for further
processing.
PendingCancellation <PdgCxl> contains one of the following PendingStatus81Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 573
Or}   Reason <Rsn> [1..*]  573
     Code <Cd> [1..1]  574
{Or       Code <Cd> [1..1] CodeSet 574
Or}       Proprietary <Prtry> [1..1] ± 574
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 575
18.4.3.6.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
18.4.3.6.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 573 March 2026
```

