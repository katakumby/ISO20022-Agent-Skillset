---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.3 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [277, 278, 279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.3 CreditDebitIndicator <CdtDbtInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 277 to 279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 277

```text
5.4.2.1.3.2.1.3  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the payment transaction is a debit or credit transaction.
.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
5.4.2.1.3.2.1.4  Payment <Pmt>
Presence: [0..1]
Definition: Instruction to pay an amount of money to an ultimate beneficiary, on behalf of an originator.
This instruction may have to be forwarded several times to complete the settlement chain.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 277 February 2025
```

## File page 278

```text
Payment <Pmt> contains the following PaymentInstruction47 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [0..1] Text 280
   RequestedExecutionDate <ReqdExctnDt> [0..1] ± 280
   Status <Sts> [0..*]  280
     Code <Cd> [0..1]  281
{Or       Pending <Pdg> [1..1] CodeSet 281
Or       Final <Fnl> [1..1] CodeSet 283
Or       RTGS <RTGS> [1..1] Text 283
Or       Settlement <Sttlm> [1..1] Text 283
Or}       Proprietary <Prtry> [1..1] Text 283
     DateTime <DtTm> [0..1] ± 283
     Reason <Rsn> [0..*]  283
{Or       Unmatched <Umtchd> [1..1] CodeSet 284
Or       Cancelled <Canc> [1..1] CodeSet 286
Or       Suspended <Sspd> [1..1] CodeSet 286
Or       PendingFailingSettlement <PdgFlngSttlm> [1..1] CodeSet 286
Or       PendingSettlement <PdgSttlm> [1..1] CodeSet 289
Or       ProprietaryRejection <PrtryRjctn> [1..1]  291
         ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 291
         Reason <Rsn> [1..1] Text 291
Or}       Proprietary <Prtry> [1..1] Text 291
   InstructedAmount <InstdAmt> [0..1]  291
{Or     AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C8 292
Or}     AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 292
   InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] ± 292
   Purpose <Purp> [0..1] Text 292
   PaymentMethod <PmtMtd> [0..1]  292
{Or     FINMessageType <FINMT> [1..1] Text 293
Or     XMLMessageName <XMLMsgNm> [1..1] Text 293
Or     Proprietary <Prtry> [1..1] Text 293
Or}     Instrument <Instrm> [1..1] CodeSet 293
   Priority <Prty> [0..1]  294
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 278 February 2025
```

## File page 279

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Code <Cd> [1..1] CodeSet 294
Or}     Proprietary <Prtry> [1..1] Text 294
   ProcessingValidityTime <PrcgVldtyTm> [0..1]  295
{Or     FromDateTime <FrDtTm> [1..1] DateTime 295
Or     ToDateTime <ToDtTm> [1..1] DateTime 295
Or}     DateTimeRange <DtTmRg> [1..1] ± 295
   InstructionCopy <InstrCpy> [0..1] Text 295
   Type <Tp> [0..1]  295
{Or     Code <Cd> [1..1] CodeSet 296
Or}     Proprietary <Prtry> [1..1] Text 297
   GeneratedOrder <GnrtdOrdr> [0..1] Indicator 298
   TransactionIdentification <TxId> [0..1] Text 298
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 298
   EndToEndIdentification <EndToEndId> [0..1] Text 298
   Parties <Pties> [0..1]  298
     InstructingAgent <InstgAgt> [0..1] ± 299
     InstructedAgent <InstdAgt> [0..1] ± 300
     UltimateDebtor <UltmtDbtr> [0..1]  301
{Or       Party <Pty> [1..1] ± 301
Or}       Agent <Agt> [1..1] ± 302
     Debtor <Dbtr> [0..1]  303
{Or       Party <Pty> [1..1] ± 303
Or}       Agent <Agt> [1..1] ± 304
     DebtorAgent <DbtrAgt> [0..1] ± 305
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 306
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 307
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 307
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 308
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 309
     CreditorAgent <CdtrAgt> [0..1] ± 310
     Creditor <Cdtr> [0..1]  311
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 279 February 2025
```

