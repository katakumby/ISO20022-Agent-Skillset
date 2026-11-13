---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.2 ProcessingStatus <PrcgSts>", "28.4.2.3 PendingProcessing <PdgPrcg>"]
file_pages: [964]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.2.3 PendingProcessing <PdgPrcg>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 964 to 964.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 964

```text
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 1968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
28.4.2.3  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer, but processing of the instruction
is pending.
PendingProcessing <PdgPrcg> contains one of the following PendingProcessingStatus21Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 964
Or}   Reason <Rsn> [1..*]  964
     Code <Cd> [1..1]  965
{Or       Code <Cd> [1..1] CodeSet 965
Or}       Proprietary <Prtry> [1..1] ± 966
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 966
28.4.2.3.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
28.4.2.3.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 964 March 2026
```

