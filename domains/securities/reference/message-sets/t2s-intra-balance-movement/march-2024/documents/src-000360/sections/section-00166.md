---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>"]
file_pages: [202, 203, 204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1 Movements <Mvmnts>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 202 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 202

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 228
Or             PoolIdentification <PoolId> [1..1] Text 228
Or}             OtherTransactionIdentification <OthrTxId> [1..1] Text 228
           ReferenceOwner <RefOwnr> [0..1] ± 228
         Priority <Prty> [0..1] ± 229
         MessageOriginator <MsgOrgtr> [0..1] ± 229
         CreationDateTime <CreDtTm> [1..1] DateTime 229
         InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 229
         SupplementaryData <SplmtryData> [0..*] ± C23 229
Or}   OperationalError <OprlErr> [1..*]  230
     Error <Err> [1..1]  230
{Or       Code <Cd> [1..1] CodeSet 230
Or}       Proprietary <Prtry> [1..1] Text 230
     Description <Desc> [0..1] Text 231
10.4.4.1  Movements <Mvmnts>
Presence: [1..*]
Definition: Identifies the transactions.
Impacted by: C8 "CashAccountOwnerRule", C9 "CashAccountRule", C10 "CashAccountServicerRule",
C22 "StatusAndReasonRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
202 March 2024
```

## File page 203

```text
Movements <Mvmnts> contains the following IntraBalanceMovements4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [0..1] ± C15,
C14
205
   CashAccountOwner <CshAcctOwnr> [0..1] ± 206
   CashAccountServicer <CshAcctSvcr> [0..1] ± 206
   StatusAndReason <StsAndRsn> [0..1]  207
     ProcessingStatus <PrcgSts> [0..*] ± 207
     SettlementStatus <SttlmSts> [0..*] ± C17 208
     Settled <Sttld> [0..1] ± C5 208
   Movement <Mvmnt> [1..*]  C16 209
     CashAccount <CshAcct> [0..1] ± C15,
C14
212
     CashAccountOwner <CshAcctOwnr> [0..1] ± 212
     CashAccountServicer <CshAcctSvcr> [0..1] ± 213
     StatusAndReason <StsAndRsn> [0..1]  213
       ProcessingStatus <PrcgSts> [0..*] ± 213
       SettlementStatus <SttlmSts> [0..*] ± C17 214
       Settled <Sttld> [0..1] ± C5 214
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 215
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 215
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 215
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 215
     PoolIdentification <PoolId> [0..1] Text 215
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 215
     MovementDetails <MvmntDtls> [0..1]  216
       BalanceFrom <BalFr> [1..1]  218
         Type <Tp> [1..1]  218
{Or           Code <Cd> [1..1] CodeSet 219
Or}           Proprietary <Prtry> [1..1] ± 219
         QuantityBreakdown <QtyBrkdwn> [0..*]  219
           LotNumber <LotNb> [0..1] ± 219
           LotAmount <LotAmt> [0..1] ± 220
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
203 March 2024
```

## File page 204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           LotQuantity <LotQty> [0..1] ± 220
           CashSubBalanceType <CshSubBalTp> [0..1] ± 220
       BalanceTo <BalTo> [1..1]  221
         Type <Tp> [1..1]  221
{Or           Code <Cd> [1..1] CodeSet 221
Or}           Proprietary <Prtry> [1..1] ± 221
         QuantityBreakdown <QtyBrkdwn> [0..*]  222
           LotNumber <LotNb> [0..1] ± 222
           LotAmount <LotAmt> [0..1] ± 222
           LotQuantity <LotQty> [0..1] ± 223
           CashSubBalanceType <CshSubBalTp> [0..1] ± 223
       SettlementAmount <SttlmAmt> [1..1] ± 223
       SettledAmount <SttldAmt> [0..1] ± 223
       PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 224
       RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 224
       IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 224
       EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 224
       StatusDate <StsDt> [0..1] DateTime 225
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 225
       Linkages <Lnkgs> [0..*]  225
         ProcessingPosition <PrcgPos> [0..1] ± C24 226
         MessageNumber <MsgNb> [0..1] ± C21 226
         Reference <Ref> [1..1]  227
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 227
Or           IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 227
Or           IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 228
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 228
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 228
Or           PoolIdentification <PoolId> [1..1] Text 228
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
204 March 2024
```

