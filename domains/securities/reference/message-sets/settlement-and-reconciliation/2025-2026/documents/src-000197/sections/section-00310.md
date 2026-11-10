---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.9 CancellationStatus <CxlSts>", "13.4.7.9.2 Rejected <Rjctd>"]
file_pages: [455]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.9.2 Rejected <Rjctd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 455 to 455.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 455

```text
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingStatus39Choice" on page 1982 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1982
Or}   Reason <Rsn> [1..*]  1982
     Code <Cd> [1..1] ± 1982
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1983
13.4.7.9.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/Request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus43Choice" on
page 1951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1952
Or}   Reason <Rsn> [1..*]  1952
     Code <Cd> [1..1] ± 1952
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1952
13.4.7.9.3  Repair <Rpr>
Presence: [1..1]
Definition: Instruction/Request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus42Choice" on
page 1919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1919
Or}   Reason <Rsn> [1..*]  1919
     Code <Cd> [1..1] ± 1920
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1920
13.4.7.9.4  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 455 March 2026
```

