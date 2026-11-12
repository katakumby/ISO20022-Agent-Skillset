---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.3 Constraints"]
file_pages: [435]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 435 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SettlementStatus <SttlmSts> [0..1] ± C4 448
     ModificationProcessingStatus <ModPrcgSts> [0..1]  449
{Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 450
Or       PendingProcessing <PdgPrcg> [1..1] ± 450
Or       Denied <Dnd> [1..1] ± 451
Or       Rejected <Rjctd> [1..1] ± 451
Or       Repaired <Rprd> [1..1] ± 451
Or       Modified <Modfd> [1..1]  452
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 452
Or}         Reason <Rsn> [1..*]  452
           Code <Cd> [1..1]  453
{Or             Code <Cd> [1..1] CodeSet 453
Or}             Proprietary <Prtry> [1..1] ± 453
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 454
Or}       Proprietary <Prtry> [1..1] ± 454
     CancellationStatus <CxlSts> [0..1]  454
{Or       PendingCancellation <PdgCxl> [1..1] ± 454
Or       Rejected <Rjctd> [1..1] ± 455
Or       Repair <Rpr> [1..1] ± 455
Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 455
Or       Proprietary <Prtry> [1..1] ± 456
Or       Denied <Dnd> [1..1] ± 456
Or}       Cancelled <Canc> [1..1] ± 456
     Settled <Sttld> [0..1] ± C1 457
     SupplementaryData <SplmtryData> [0..*] ± C8 457
13.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 435 March 2026
```

