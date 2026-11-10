---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.2 TransactionsSummary <TxsSummry>", "5.4.2.1.2.3 TotalNetEntryAmount <TtlNetNtryAmt>"]
file_pages: [251, 252, 253, 254, 255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.2.3 TotalNetEntryAmount <TtlNetNtryAmt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 251 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 251

```text
5.4.2.1.2.3  TotalNetEntryAmount <TtlNetNtryAmt>
Presence: [0..1]
Definition: Resulting amount of the netted amounts for all debit and credit entries.
Datatype: "DecimalNumber" on page 886
5.4.2.1.2.4  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the total net entry amount is a credit or a debit amount.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
5.4.2.1.3  TransactionReport <TxRpt>
Presence: [1..*]
Definition: Reports either on the transaction information or on a business error.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 251 February 2025
```

## File page 252

```text
TransactionReport <TxRpt> contains the following TransactionReport8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [1..1]  256
{Or     TransactionIdentification <TxId> [1..1] Text 257
Or     UETR <UETR> [1..1] IdentifierSet 258
Or     QueueIdentification <QId> [1..1]  258
       QueueIdentification <QId> [1..1] Text 258
       PositionInQueue <PosInQ> [1..1] Text 258
Or     LongBusinessIdentification <LngBizId> [1..1]  C18 258
       TransactionIdentification <TxId> [0..1] Text 259
       UETR <UETR> [0..1] IdentifierSet 259
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 260
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 260
       PaymentMethod <PmtMtd> [0..1]  260
{Or         FINMessageType <FINMT> [1..1] Text 260
Or         XMLMessageName <XMLMsgNm> [1..1] Text 260
Or         Proprietary <Prtry> [1..1] Text 260
Or}         Instrument <Instrm> [1..1] CodeSet 260
       InstructingAgent <InstgAgt> [1..1] ± 261
       InstructedAgent <InstdAgt> [1..1] ± 262
       EntryType <NtryTp> [0..1] IdentifierSet 263
       EndToEndIdentification <EndToEndId> [0..1] Text 263
Or     ShortBusinessIdentification <ShrtBizId> [1..1]  C19 263
       TransactionIdentification <TxId> [0..1] Text 264
       UETR <UETR> [0..1] IdentifierSet 264
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 264
       InstructingAgent <InstgAgt> [1..1] ± 264
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 265
   TransactionOrError <TxOrErr> [1..1]  265
{Or     Transaction <Tx> [1..1]  C17, C7 269
       PaymentTo <PmtTo> [0..1]  273
         SystemIdentification <SysId> [0..1] ± 274
         MemberIdentification <MmbId> [0..1] ± 274
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 252 February 2025
```

## File page 253

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Country <Ctry> [0..1] CodeSet C5 274
         AccountIdentification <AcctId> [0..1] ± 275
       PaymentFrom <PmtFr> [0..1]  275
         SystemIdentification <SysId> [0..1] ± 275
         MemberIdentification <MmbId> [0..1] ± 275
         Country <Ctry> [0..1] CodeSet C5 276
         AccountIdentification <AcctId> [0..1] ± 276
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 277
       Payment <Pmt> [0..1]  277
         MessageIdentification <MsgId> [0..1] Text 280
         RequestedExecutionDate <ReqdExctnDt> [0..1] ± 280
         Status <Sts> [0..*]  280
           Code <Cd> [0..1]  281
{Or             Pending <Pdg> [1..1] CodeSet 281
Or             Final <Fnl> [1..1] CodeSet 283
Or             RTGS <RTGS> [1..1] Text 283
Or             Settlement <Sttlm> [1..1] Text 283
Or}             Proprietary <Prtry> [1..1] Text 283
           DateTime <DtTm> [0..1] ± 283
           Reason <Rsn> [0..*]  283
{Or             Unmatched <Umtchd> [1..1] CodeSet 284
Or             Cancelled <Canc> [1..1] CodeSet 286
Or             Suspended <Sspd> [1..1] CodeSet 286
Or             PendingFailingSettlement <PdgFlngSttlm> [1..1] CodeSet 286
Or             PendingSettlement <PdgSttlm> [1..1] CodeSet 289
Or             ProprietaryRejection <PrtryRjctn> [1..1]  291
               ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 291
               Reason <Rsn> [1..1] Text 291
Or}             Proprietary <Prtry> [1..1] Text 291
         InstructedAmount <InstdAmt> [0..1]  291
{Or           AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C8 292
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 253 February 2025
```

## File page 254

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 292
         InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] ± 292
         Purpose <Purp> [0..1] Text 292
         PaymentMethod <PmtMtd> [0..1]  292
{Or           FINMessageType <FINMT> [1..1] Text 293
Or           XMLMessageName <XMLMsgNm> [1..1] Text 293
Or           Proprietary <Prtry> [1..1] Text 293
Or}           Instrument <Instrm> [1..1] CodeSet 293
         Priority <Prty> [0..1]  294
{Or           Code <Cd> [1..1] CodeSet 294
Or}           Proprietary <Prtry> [1..1] Text 294
         ProcessingValidityTime <PrcgVldtyTm> [0..1]  295
{Or           FromDateTime <FrDtTm> [1..1] DateTime 295
Or           ToDateTime <ToDtTm> [1..1] DateTime 295
Or}           DateTimeRange <DtTmRg> [1..1] ± 295
         InstructionCopy <InstrCpy> [0..1] Text 295
         Type <Tp> [0..1]  295
{Or           Code <Cd> [1..1] CodeSet 296
Or}           Proprietary <Prtry> [1..1] Text 297
         GeneratedOrder <GnrtdOrdr> [0..1] Indicator 298
         TransactionIdentification <TxId> [0..1] Text 298
         InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 298
         EndToEndIdentification <EndToEndId> [0..1] Text 298
         Parties <Pties> [0..1]  298
           InstructingAgent <InstgAgt> [0..1] ± 299
           InstructedAgent <InstdAgt> [0..1] ± 300
           UltimateDebtor <UltmtDbtr> [0..1]  301
{Or             Party <Pty> [1..1] ± 301
Or}             Agent <Agt> [1..1] ± 302
           Debtor <Dbtr> [0..1]  303
{Or             Party <Pty> [1..1] ± 303
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 254 February 2025
```

## File page 255

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             Agent <Agt> [1..1] ± 304
           DebtorAgent <DbtrAgt> [0..1] ± 305
           InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 306
           InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 307
           IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 307
           IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 308
           IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 309
           CreditorAgent <CdtrAgt> [0..1] ± 310
           Creditor <Cdtr> [0..1]  311
{Or             Party <Pty> [1..1] ± 311
Or}             Agent <Agt> [1..1] ± 312
           UltimateCreditor <UltmtCdtr> [0..1]  313
{Or             Party <Pty> [1..1] ± 313
Or}             Agent <Agt> [1..1] ± 314
       AccountEntry <AcctNtry> [0..1]  315
         Account <Acct> [1..1]  C14,
C13
316
           Identification <Id> [0..1] ± 317
           Type <Tp> [0..1] ± 317
           Currency <Ccy> [0..1] CodeSet C2 317
           Name <Nm> [0..1] Text 318
           Proxy <Prxy> [0..1] ± 318
           Owner <Ownr> [0..1] ± 318
           Servicer <Svcr> [0..1] ± 319
         Entry <Ntry> [0..1]  320
           Amount <Amt> [0..1] Amount C1, C9 320
           Date <Dt> [0..1] ± 321
           Status <Sts> [0..1] CodeSet 321
           Identification <Id> [0..1] Text 322
           StatementIdentification <StmtId> [0..1] Text 322
           AccountServicerReference <AcctSvcrRef> [0..1] Quantity 322
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 255 February 2025
```

