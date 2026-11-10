---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.1 Status <Sts>"]
file_pages: [419, 420]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.1 Status <Sts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 419 to 420.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 419

```text
AdditionalQueryParameters <AddtlQryParams> contains the following
AdditionalQueryParameters15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [0..1] ± C14 419
   Reason <Rsn> [0..*]  C7 421
{Or     RepoCallAcknowledgementReason
<RepoCallAckRsn>
[0..1] ± 422
Or     CancellationReason <CxlRsn> [0..1] ± 422
Or     PendingCancellationReason <PdgCxlRsn> [0..1] ± 422
Or     GeneratedReason <GnrtdRsn> [0..1] ± 422
Or     DeniedReason <DndRsn> [0..1] ± 423
Or     AcknowledgedAcceptedReason <AckdAccptdRsn> [0..1] ± 423
Or     PendingReason <PdgRsn> [0..1]  423
{Or       Code <Cd> [1..1] CodeSet 423
Or}       Proprietary <Prtry> [1..1] ± 427
Or     FailingReason <FlngRsn> [0..1] ± 427
Or     PendingProcessingReason <PdgPrcgRsn> [0..1]  427
{Or       Code <Cd> [1..1] CodeSet 428
Or}       Proprietary <Prtry> [1..1] ± 429
Or     RejectionReason <RjctnRsn> [0..1] ± 429
Or     RepairReason <RprRsn> [0..1] ± 429
Or     PendingModificationReason <PdgModRsn> [0..1] ± 430
Or}     UnmatchedReason <UmtchdRsn> [0..1] ± 430
   FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C2, C3,
C4, C5,
C6
430
12.4.6.1  Status <Sts>
Presence: [0..1]
Definition: Request to obtain a Securities Transaction Pending Report for transactions with the specified
status.
Impacted by: C14 "StatusRule"
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 419 March 2026
```

## File page 420

```text
Status <Sts> contains one of the following elements (see "Status19Choice" on page 1905 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AffirmationStatus <AffirmSts> [1..1] ± 1907
Or   AllocationStatus <AllcnSts> [1..1]  1907
{Or     Code <Cd> [1..1] CodeSet 1907
Or}     Proprietary <Prtry> [1..1] ± 1907
Or   RepoCallRequestStatus <RepoCallReqSts> [1..1] ± 1908
Or   CorporateActionEventProcessingStatus
<CorpActnEvtPrcgSts>
[1..1]  1908
{Or     Code <Cd> [1..1] CodeSet 1908
Or}     Proprietary <Prtry> [1..1] ± 1909
Or   CorporateActionEventStage <CorpActnEvtStag> [1..1]  1909
{Or     Code <Cd> [1..1] CodeSet 1909
Or}     Proprietary <Prtry> [1..1] ± 1910
Or   InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 1910
Or   InstructionProcessingStatus <InstrPrcgSts> [1..1]  1910
{Or     Code <Cd> [1..1] CodeSet 1910
Or}     Proprietary <Prtry> [1..1] ± 1912
Or   MatchingStatus <MtchgSts> [1..1] ± 1912
Or   RegistrationProcessingStatus <RegnPrcgSts> [1..1]  1913
{Or     Code <Cd> [1..1] CodeSet 1913
Or}     Proprietary <Prtry> [1..1] ± 1913
Or   ResponseStatus <RspnSts> [1..1]  1913
{Or     Code <Cd> [1..1] CodeSet 1914
Or}     Proprietary <Prtry> [1..1] ± 1914
Or   ReplacementProcessingStatus <RplcmntPrcgSts> [1..1]  1914
{Or     Code <Cd> [1..1] CodeSet 1915
Or}     Proprietary <Prtry> [1..1] ± 1915
Or   CancellationProcessingStatus <CxlPrcgSts> [1..1]  1916
{Or     Code <Cd> [1..1] CodeSet 1916
Or}     Proprietary <Prtry> [1..1] ± 1916
Or   SettlementStatus <SttlmSts> [1..1] ± 1917
Or}   SettlementConditionModificationStatus
<SttlmCondModSts>
[1..1]  1917
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 420 March 2026
```

