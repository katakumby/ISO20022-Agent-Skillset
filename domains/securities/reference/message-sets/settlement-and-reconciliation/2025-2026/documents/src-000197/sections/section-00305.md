---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.8 ModificationProcessingStatus <ModPrcgSts>", "13.4.7.8.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.8.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
ModificationProcessingStatus <ModPrcgSts> contains one of the following
ModificationProcessingStatus13Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 450
Or   PendingProcessing <PdgPrcg> [1..1] ± 450
Or   Denied <Dnd> [1..1] ± 451
Or   Rejected <Rjctd> [1..1] ± 451
Or   Repaired <Rprd> [1..1] ± 451
Or   Modified <Modfd> [1..1]  452
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 452
Or}     Reason <Rsn> [1..*]  452
       Code <Cd> [1..1]  453
{Or         Code <Cd> [1..1] CodeSet 453
Or}         Proprietary <Prtry> [1..1] ± 453
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 454
Or}   Proprietary <Prtry> [1..1] ± 454
13.4.7.8.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus23Choice" on page 1926 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1926
Or}   Reason <Rsn> [1..*]  1926
     Code <Cd> [1..1] ± 1926
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1927
13.4.7.8.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Modification is pending processing.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 450 March 2026
```

