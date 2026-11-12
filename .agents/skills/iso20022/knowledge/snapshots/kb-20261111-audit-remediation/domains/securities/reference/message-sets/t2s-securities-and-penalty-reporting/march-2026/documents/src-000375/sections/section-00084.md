---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.3 StatusAndReason <StsAndRsn>"]
file_pages: [119, 120]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.3 StatusAndReason <StsAndRsn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 119 to 120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 119

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
4.4.3.4.3  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
Impacted by: C25 "PendingToFailingRule", C34 "SettlementStatusAndMatchedRule"
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 119 March 2026
```

## File page 120

```text
StatusAndReason <StsAndRsn> contains the following StatusAndReason52 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 121
   MatchingStatus <MtchgSts> [0..1] ± 121
   SettlementStatus <SttlmSts> [0..1] ± C26 122
   InstructionProcessingStatus <InstrPrcgSts> [0..1]  123
{Or     PendingProcessing <PdgPrcg> [1..1]  124
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 125
Or}       Reason <Rsn> [1..*]  125
         Code <Cd> [1..1]  125
{Or           Code <Cd> [1..1] CodeSet 126
Or}           Proprietary <Prtry> [1..1] ± 127
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 127
Or     CancellationRequested <CxlReqd> [1..1] ± C6 127
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 128
Or     Cancelled <Canc> [1..1] ± 128
Or     Generated <Gnrtd> [1..1]  128
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 129
Or}       Reason <Rsn> [1..*] ± 129
Or     Repair <Rpr> [1..1] ± 129
Or     PendingCancellation <PdgCxl> [1..1]  129
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 130
Or}       Reason <Rsn> [1..*]  130
         Code <Cd> [1..1]  130
{Or           Code <Cd> [1..1] CodeSet 131
Or}           Proprietary <Prtry> [1..1] ± 131
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 131
Or}     ModificationRequested <ModReqd> [1..1] ± C6 132
   Settled <Sttld> [0..1] ± C6 132
   Proprietary <Prtry> [0..1] ± 132
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 120 March 2026
```

