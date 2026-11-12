---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.3.2 PendingProcessing <PdgPrcg>"]
file_pages: [569]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.3.2 PendingProcessing <PdgPrcg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 569 to 569.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 569

```text
18.4.3.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer, but processing of the instruction
is pending.
PendingProcessing <PdgPrcg> contains one of the following PendingProcessingStatus20Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 569
Or}   Reason <Rsn> [1..*]  569
     Code <Cd> [1..1]  569
{Or       Code <Cd> [1..1] CodeSet 570
Or}       Proprietary <Prtry> [1..1] ± 571
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 571
18.4.3.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
18.4.3.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Reason <Rsn> contains the following PendingProcessingReason17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  569
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] ± 571
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 571
18.4.3.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 569 March 2026
```

