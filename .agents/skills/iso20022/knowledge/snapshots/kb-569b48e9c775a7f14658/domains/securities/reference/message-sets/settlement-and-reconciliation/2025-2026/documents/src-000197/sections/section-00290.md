---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.2 Structure"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
13.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxAudtTrlRpt> [1..1]  C5, C6,
C7
   Pagination <Pgntn> [1..1] ± 0
   QueryReference <QryRef> [0..1] Text 437
   TransactionIdentification <TxId> [0..1] ± C3 0
   SafekeepingAccount <SfkpgAcct> [0..1] ± 0
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 438
   AccountOwner <AcctOwnr> [0..1] ± 438
   StatusTrail <StsTrl> [0..*]  0
     StatusDate <StsDt> [1..1] DateTime 440
     SendingOrganisationIdentification <SndgOrgId> [0..1] ± 440
     UserIdentification <UsrId> [0..1] Text 441
     ProcessingStatus <PrcgSts> [0..1]  441
{Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 442
Or       PendingProcessing <PdgPrcg> [1..1] ± 442
Or       Rejected <Rjctd> [1..1] ± 443
Or       Repair <Rpr> [1..1] ± 443
Or       Cancelled <Canc> [1..1] ± 444
Or       PendingCancellation <PdgCxl> [1..1]  444
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 445
Or}         Reason <Rsn> [1..*]  445
           Code <Cd> [1..1]  445
{Or             Code <Cd> [1..1] CodeSet 446
Or}             Proprietary <Prtry> [1..1] ± 446
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
Or       Proprietary <Prtry> [1..1] ± 446
Or       CancellationRequested <CxlReqd> [1..1] ± C1 447
Or}       ModificationRequested <ModReqd> [1..1] ± C1 447
     InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 448
     MatchingStatus <MtchgSts> [0..1] ± 448
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 434 March 2026
```

