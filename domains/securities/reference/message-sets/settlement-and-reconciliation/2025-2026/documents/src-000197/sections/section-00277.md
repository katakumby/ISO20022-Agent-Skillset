---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.2 Structure"]
file_pages: [414]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 414 to 414.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 414

```text
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesStmtQry> [1..1]  C8, C9,
C10
   StatementRequested <StmtReqd> [1..1] ± 416
   StatementGeneralDetails <StmtGnlDtls> [0..1] ± C12,
C13
0
   AccountOwner <AcctOwnr> [0..1] ± 0
   SafekeepingAccount <SfkpgAcct> [0..1] ± 0
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 418
   AdditionalQueryParameters <AddtlQryParams> [0..*]  418
     Status <Sts> [0..1] ± C14 419
     Reason <Rsn> [0..*]  C7 421
{Or       RepoCallAcknowledgementReason <RepoCallAckRsn> [0..1] ± 422
Or       CancellationReason <CxlRsn> [0..1] ± 422
Or       PendingCancellationReason <PdgCxlRsn> [0..1] ± 422
Or       GeneratedReason <GnrtdRsn> [0..1] ± 422
Or       DeniedReason <DndRsn> [0..1] ± 423
Or       AcknowledgedAcceptedReason <AckdAccptdRsn> [0..1] ± 423
Or       PendingReason <PdgRsn> [0..1]  423
{Or         Code <Cd> [1..1] CodeSet 423
Or}         Proprietary <Prtry> [1..1] ± 427
Or       FailingReason <FlngRsn> [0..1] ± 427
Or       PendingProcessingReason <PdgPrcgRsn> [0..1]  427
{Or         Code <Cd> [1..1] CodeSet 428
Or}         Proprietary <Prtry> [1..1] ± 429
Or       RejectionReason <RjctnRsn> [0..1] ± 429
Or       RepairReason <RprRsn> [0..1] ± 429
Or       PendingModificationReason <PdgModRsn> [0..1] ± 430
Or}       UnmatchedReason <UmtchdRsn> [0..1] ± 430
     FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C2, C3,
C4, C5,
C6
430
   SupplementaryData <SplmtryData> [0..*] ± C15 0
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 414 March 2026
```

