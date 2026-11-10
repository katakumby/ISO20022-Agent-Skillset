---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.6 ModificationProcessingStatus <ModPrcgSts>", "33.4.6.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [1308]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.6.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1308 to 1308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1308

```text
ModificationProcessingStatus <ModPrcgSts> contains one of the following
ModificationProcessingStatus12Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 1308
Or   PendingProcessing <PdgPrcg> [1..1] ± 1308
Or   Denied <Dnd> [1..1] ± 1309
Or   Rejected <Rjctd> [1..1] ± 1309
Or   Repaired <Rprd> [1..1] ± 1309
Or   Modified <Modfd> [1..1]  1310
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1310
Or}     Reason <Rsn> [1..*]  1310
       Code <Cd> [1..1]  1311
{Or         Code <Cd> [1..1] CodeSet 1311
Or}         Proprietary <Prtry> [1..1] ± 1311
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1312
Or}   Proprietary <Prtry> [1..1] ± 1312
33.4.6.1  AcknowledgedAccepted <AckdAccptd>
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
33.4.6.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Modification is pending processing.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1308 March 2026
```

