---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.4 ProcessingStatus <PrcgSts>", "13.4.7.4.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [442]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.4.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 442 to 442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 442

```text
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus103Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 442
Or   PendingProcessing <PdgPrcg> [1..1] ± 442
Or   Rejected <Rjctd> [1..1] ± 443
Or   Repair <Rpr> [1..1] ± 443
Or   Cancelled <Canc> [1..1] ± 444
Or   PendingCancellation <PdgCxl> [1..1]  444
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 445
Or}     Reason <Rsn> [1..*]  445
       Code <Cd> [1..1]  445
{Or         Code <Cd> [1..1] CodeSet 446
Or}         Proprietary <Prtry> [1..1] ± 446
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
Or   Proprietary <Prtry> [1..1] ± 446
Or   CancellationRequested <CxlReqd> [1..1] ± C1 447
Or}   ModificationRequested <ModReqd> [1..1] ± C1 447
13.4.7.4.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 1968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
13.4.7.4.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer, but processing of the instruction
is pending.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 442 March 2026
```

