---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.3 ReportGeneralDetails <RptGnlDtls>", "10.4.3.1 QueryReference <QryRef>"]
file_pages: [199, 200, 201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.3.1 QueryReference <QryRef>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 199 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 199

```text
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different report identifications. For example, a daily report sent on
day 1 would have ReportIdentification 001, on day 2, 002, etc.
10.4.3.1  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the Query message sent to request this statement.
Datatype: "Max35Text" on page 497
10.4.3.2  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 497
10.4.3.3  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 485
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
10.4.3.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 495):
• Meaning When True: Yes
• Meaning When False: No
10.4.4 ReportOrError <RptOrErr>
Presence: [0..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
199 March 2024
```

## File page 200

```text
ReportOrError <RptOrErr> contains one of the following IntraBalanceOrOperationalError11Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Movements <Mvmnts> [1..*]  C8, C9,
C10,
C22
202
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
       CorporateActionEventIdentification
<CorpActnEvtId>
[0..1] Text 215
       MovementDetails <MvmntDtls> [0..1]  216
         BalanceFrom <BalFr> [1..1]  218
           Type <Tp> [1..1]  218
{Or             Code <Cd> [1..1] CodeSet 219
Or}             Proprietary <Prtry> [1..1] ± 219
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
200 March 2024
```

## File page 201

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           QuantityBreakdown <QtyBrkdwn> [0..*]  219
             LotNumber <LotNb> [0..1] ± 219
             LotAmount <LotAmt> [0..1] ± 220
             LotQuantity <LotQty> [0..1] ± 220
             CashSubBalanceType <CshSubBalTp> [0..1] ± 220
         BalanceTo <BalTo> [1..1]  221
           Type <Tp> [1..1]  221
{Or             Code <Cd> [1..1] CodeSet 221
Or}             Proprietary <Prtry> [1..1] ± 221
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
{Or             SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 227
Or             IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 227
Or             IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 228
Or             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 228
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
201 March 2024
```

