---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.2 ProcessingStatus <PrcgSts>", "28.4.2.1 PendingCancellation <PdgCxl>", "28.4.2.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [962]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.2.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 962 to 962.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 962

```text
PendingCancellation <PdgCxl> contains one of the following PendingStatus81Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 962
Or}   Reason <Rsn> [1..*]  962
     Code <Cd> [1..1]  962
{Or       Code <Cd> [1..1] CodeSet 963
Or}       Proprietary <Prtry> [1..1] ± 963
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 963
28.4.2.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
28.4.2.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  962
{Or     Code <Cd> [1..1] CodeSet 963
Or}     Proprietary <Prtry> [1..1] ± 963
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 963
28.4.2.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Code <Cd> contains one of the following PendingReason77Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 963
Or}   Proprietary <Prtry> [1..1] ± 963
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 962 March 2026
```

