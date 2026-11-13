---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.3.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [568]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.3.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 568 to 568.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 568

```text
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus101Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 568
Or   PendingProcessing <PdgPrcg> [1..1]  569
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 569
Or}     Reason <Rsn> [1..*]  569
       Code <Cd> [1..1]  569
{Or         Code <Cd> [1..1] CodeSet 570
Or}         Proprietary <Prtry> [1..1] ± 571
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 571
Or   Rejected <Rjctd> [1..1] ± 572
Or   Repair <Rpr> [1..1] ± 572
Or   Cancelled <Canc> [1..1] ± 572
Or   PendingCancellation <PdgCxl> [1..1]  573
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 573
Or}     Reason <Rsn> [1..*]  573
       Code <Cd> [1..1]  574
{Or         Code <Cd> [1..1] CodeSet 574
Or}         Proprietary <Prtry> [1..1] ± 574
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 575
Or   Proprietary <Prtry> [1..1] ± 575
Or   CancellationRequested <CxlReqd> [1..1] ± C3 575
Or}   ModificationRequested <ModReqd> [1..1] ± C3 576
18.4.3.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 1968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 568 March 2026
```

