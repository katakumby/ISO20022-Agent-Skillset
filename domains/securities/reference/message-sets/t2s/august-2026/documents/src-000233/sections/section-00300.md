---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.3 ReportGeneralDetails <RptGnlDtls>", "17.4.3.1 QueryReference <QryRef>"]
file_pages: [390, 391, 392]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.3.1 QueryReference <QryRef>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 390 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different report identifications. For example, a daily report sent on
day 1 would have ReportIdentification 001, on day 2, 002, etc.
17.4.3.1  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the Query message sent to request this statement.
Datatype: "Max35Text" on page 3328
17.4.3.2  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 3328
17.4.3.3  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 3264
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
17.4.3.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
17.4.4 ReportOrError <RptOrErr>
Presence: [0..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 390 August 2026
```

## File page 391

```text
ReportOrError <RptOrErr> contains one of the following IntraBalanceOrOperationalError11Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Movements <Mvmnts> [1..*]  C8, C9,
C10,
C22
393
     CashAccount <CshAcct> [0..1] ± C15,
C14
396
     CashAccountOwner <CshAcctOwnr> [0..1] ± 397
     CashAccountServicer <CshAcctSvcr> [0..1] ± 397
     StatusAndReason <StsAndRsn> [0..1]  398
       ProcessingStatus <PrcgSts> [0..*] ± 398
       SettlementStatus <SttlmSts> [0..*] ± C17 399
       Settled <Sttld> [0..1] ± C5 399
     Movement <Mvmnt> [1..*]  C16 400
       CashAccount <CshAcct> [0..1] ± C15,
C14
403
       CashAccountOwner <CshAcctOwnr> [0..1] ± 403
       CashAccountServicer <CshAcctSvcr> [0..1] ± 404
       StatusAndReason <StsAndRsn> [0..1]  404
         ProcessingStatus <PrcgSts> [0..*] ± 404
         SettlementStatus <SttlmSts> [0..*] ± C17 405
         Settled <Sttld> [0..1] ± C5 405
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 406
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 406
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 406
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 406
       PoolIdentification <PoolId> [0..1] Text 406
       CorporateActionEventIdentification
<CorpActnEvtId>
[0..1] Text 406
       MovementDetails <MvmntDtls> [0..1]  407
         BalanceFrom <BalFr> [1..1]  409
           Type <Tp> [1..1]  409
{Or             Code <Cd> [1..1] CodeSet 410
Or}             Proprietary <Prtry> [1..1] ± 410
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 391 August 2026
```

## File page 392

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           QuantityBreakdown <QtyBrkdwn> [0..*]  410
             LotNumber <LotNb> [0..1] ± 410
             LotAmount <LotAmt> [0..1] ± 411
             LotQuantity <LotQty> [0..1] ± 411
             CashSubBalanceType <CshSubBalTp> [0..1] ± 411
         BalanceTo <BalTo> [1..1]  412
           Type <Tp> [1..1]  412
{Or             Code <Cd> [1..1] CodeSet 412
Or}             Proprietary <Prtry> [1..1] ± 412
           QuantityBreakdown <QtyBrkdwn> [0..*]  413
             LotNumber <LotNb> [0..1] ± 413
             LotAmount <LotAmt> [0..1] ± 413
             LotQuantity <LotQty> [0..1] ± 414
             CashSubBalanceType <CshSubBalTp> [0..1] ± 414
         SettlementAmount <SttlmAmt> [1..1] ± 414
         SettledAmount <SttldAmt> [0..1] ± 414
         PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 415
         RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 415
         IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 415
         EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 415
         StatusDate <StsDt> [0..1] DateTime 416
         CashSubBalanceIdentification <CshSubBalId> [0..1] ± 416
         Linkages <Lnkgs> [0..*]  416
           ProcessingPosition <PrcgPos> [0..1] ± C24 417
           MessageNumber <MsgNb> [0..1] ± C21 417
           Reference <Ref> [1..1]  418
{Or             SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 418
Or             IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 418
Or             IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 419
Or             AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 419
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 392 August 2026
```

