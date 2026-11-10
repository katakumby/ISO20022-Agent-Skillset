---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.4 Message Building Blocks", "5.4.3.1 Rejected <Rjctd>"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.4.3.1 Rejected <Rjctd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
5.4.3 ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following IntraPositionProcessingStatus11Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rejected <Rjctd> [1..1] ± 154
Or   Repair <Rpr> [1..1] ± 154
Or   Cancelled <Canc> [1..1] ± 155
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 155
Or}   Proprietary <Prtry> [1..1] ± 155
5.4.3.1  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/Request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus41Choice" on
page 1920 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1920
Or}   Reason <Rsn> [1..*]  1920
     Code <Cd> [0..*] ± 1921
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1921
5.4.3.2  Repair <Rpr>
Presence: [1..1]
Definition: Instruction/Request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus41Choice" on
page 1920 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1920
Or}   Reason <Rsn> [1..*]  1920
     Code <Cd> [0..*] ± 1921
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1921
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 154 March 2026
```

