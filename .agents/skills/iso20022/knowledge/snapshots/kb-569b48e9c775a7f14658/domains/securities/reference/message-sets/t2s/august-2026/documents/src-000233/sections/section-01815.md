---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.3 StatusAndReason <StsAndRsn>"]
file_pages: [2495, 2496]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.3 StatusAndReason <StsAndRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2495 to 2496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2495

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
72.4.3.3  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
Impacted by: C25 "PendingToFailingRule", C34 "SettlementStatusAndMatchedRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2495 August 2026
```

## File page 2496

```text
StatusAndReason <StsAndRsn> contains the following StatusAndReason52 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 2497
   MatchingStatus <MtchgSts> [0..1] ± 2497
   SettlementStatus <SttlmSts> [0..1] ± C26 2498
   InstructionProcessingStatus <InstrPrcgSts> [0..1]  2499
{Or     PendingProcessing <PdgPrcg> [1..1]  2500
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2501
Or}       Reason <Rsn> [1..*]  2501
         Code <Cd> [1..1]  2501
{Or           Code <Cd> [1..1] CodeSet 2502
Or}           Proprietary <Prtry> [1..1] ± 2503
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2503
Or     CancellationRequested <CxlReqd> [1..1] ± C6 2503
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 2504
Or     Cancelled <Canc> [1..1] ± 2504
Or     Generated <Gnrtd> [1..1]  2504
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2505
Or}       Reason <Rsn> [1..*] ± 2505
Or     Repair <Rpr> [1..1] ± 2505
Or     PendingCancellation <PdgCxl> [1..1]  2505
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2506
Or}       Reason <Rsn> [1..*]  2506
         Code <Cd> [1..1]  2506
{Or           Code <Cd> [1..1] CodeSet 2507
Or}           Proprietary <Prtry> [1..1] ± 2507
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2507
Or}     ModificationRequested <ModReqd> [1..1] ± C6 2508
   Settled <Sttld> [0..1] ± C6 2508
   Proprietary <Prtry> [0..1] ± 2508
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2496 August 2026
```

