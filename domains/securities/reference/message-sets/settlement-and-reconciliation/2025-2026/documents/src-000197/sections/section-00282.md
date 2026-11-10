---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>"]
file_pages: [421]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2 Reason <Rsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 421 to 421.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 421

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Code <Cd> [1..1] CodeSet 1917
Or}     Proprietary <Prtry> [1..1] ± 1918
Constraints
• StatusRule
If a specific Status is requested, then it must be in line with the statuses available for the message
type requested.
12.4.6.2  Reason <Rsn>
Presence: [0..*]
Definition: Request to obtain a Securities Transaction Pending Report for transactions with the specified
status reason.
Impacted by: C7 "ReasonRule"
Reason <Rsn> contains one of the following Reason21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RepoCallAcknowledgementReason
<RepoCallAckRsn>
[0..1] ± 422
Or   CancellationReason <CxlRsn> [0..1] ± 422
Or   PendingCancellationReason <PdgCxlRsn> [0..1] ± 422
Or   GeneratedReason <GnrtdRsn> [0..1] ± 422
Or   DeniedReason <DndRsn> [0..1] ± 423
Or   AcknowledgedAcceptedReason <AckdAccptdRsn> [0..1] ± 423
Or   PendingReason <PdgRsn> [0..1]  423
{Or     Code <Cd> [1..1] CodeSet 423
Or}     Proprietary <Prtry> [1..1] ± 427
Or   FailingReason <FlngRsn> [0..1] ± 427
Or   PendingProcessingReason <PdgPrcgRsn> [0..1]  427
{Or     Code <Cd> [1..1] CodeSet 428
Or}     Proprietary <Prtry> [1..1] ± 429
Or   RejectionReason <RjctnRsn> [0..1] ± 429
Or   RepairReason <RprRsn> [0..1] ± 429
Or   PendingModificationReason <PdgModRsn> [0..1] ± 430
Or}   UnmatchedReason <UmtchdRsn> [0..1] ± 430
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 421 March 2026
```

