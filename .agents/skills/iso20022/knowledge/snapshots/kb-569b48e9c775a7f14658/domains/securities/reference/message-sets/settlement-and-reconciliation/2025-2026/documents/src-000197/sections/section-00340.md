---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "16.4 Message Building Blocks", "16.4.6 ProcessingStatus <PrcgSts>", "16.4.6.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [489]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16.4.6.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 489 to 489.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 489

```text
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus89Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 489
Or   Rejected <Rjctd> [1..1] ± 489
Or}   Proprietary <Prtry> [1..1] ± 489
16.4.6.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus24Choice" on page 1983 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1983
Or}   Reason <Rsn> [1..*]  1983
     Code <Cd> [1..1] ± 1983
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1984
16.4.6.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/Request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus44Choice" on
page 1892 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1892
Or}   Reason <Rsn> [1..*]  1892
     Code <Cd> [1..1] ± 1893
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1893
16.4.6.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 489 March 2026
```

