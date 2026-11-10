---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.2 ProcessingStatus <PrcgSts>", "28.4.2.1 PendingCancellation <PdgCxl>"]
file_pages: [961]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.2.1 PendingCancellation <PdgCxl>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 961 to 961.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 961

```text
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus102Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1]  961
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 962
Or}     Reason <Rsn> [1..*]  962
       Code <Cd> [1..1]  962
{Or         Code <Cd> [1..1] CodeSet 963
Or}         Proprietary <Prtry> [1..1] ± 963
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 963
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 963
Or   PendingProcessing <PdgPrcg> [1..1]  964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 964
Or}     Reason <Rsn> [1..*]  964
       Code <Cd> [1..1]  965
{Or         Code <Cd> [1..1] CodeSet 965
Or}         Proprietary <Prtry> [1..1] ± 966
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 966
Or   Rejected <Rjctd> [1..1] ± 966
Or   Repair <Rpr> [1..1] ± 967
Or   Cancelled <Canc> [1..1] ± 967
Or   Proprietary <Prtry> [1..1] ± 968
Or   CancellationRequested <CxlReqd> [1..1] ± C4 968
Or}   ModificationRequested <ModReqd> [1..1] ± C4 968
28.4.2.1  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation request from yourself for this instruction is pending waiting for further
processing.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 961 March 2026
```

