---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.1 QueryType <QryTp>"]
file_pages: [116, 117, 118, 119, 120, 121, 122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.1 QueryType <QryTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 116 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           DebtorAgentIndicator <DbtrAgtInd> [0..1] Indicator 204
           InstructingReimbursementAgentIndicator
<InstgRmbrsmntAgtInd>
[0..1] Indicator 204
           InstructedReimbursementAgentIndicator
<InstdRmbrsmntAgtInd>
[0..1] Indicator 204
           IntermediaryIndicator <IntrmyInd> [0..1] Indicator 204
           CreditorAgentIndicator <CdtrAgtInd> [0..1] Indicator 204
           CreditorIndicator <CdtrInd> [0..1] Indicator 205
4.4.2.1  QueryType <QryTp>
Presence: [0..1]
Definition: Specifies the type of matching items to be returned in the response to the query.
Datatype: "QueryType2Code" on page 872
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
DELD Deleted Specifies that the query requests that
items that have been deleted since the
last query be returned.
4.4.2.2  TransactionCriteria <TxCrit>
Presence: [0..1]
Definition: Defines the payment transaction query criteria.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 116 February 2025
```

## File page 117

```text
TransactionCriteria <TxCrit> contains one of the following TransactionCriteria8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 123
Or}   NewCriteria <NewCrit> [1..1]  C12 123
     NewQueryName <NewQryNm> [0..1] Text 130
     SearchCriteria <SchCrit> [0..*]  130
       PaymentTo <PmtTo> [0..*]  135
         SystemIdentification <SysId> [0..*]  135
{Or           Code <Cd> [1..1] CodeSet 135
Or}           Proprietary <Prtry> [1..1] Text 136
         MemberIdentification <MmbId> [0..*] ± 136
         Country <Ctry> [0..1] CodeSet C5 136
         AccountIdentification <AcctId> [0..1] ± 137
       PaymentFrom <PmtFr> [0..*]  137
         SystemIdentification <SysId> [0..*]  137
{Or           Code <Cd> [1..1] CodeSet 138
Or}           Proprietary <Prtry> [1..1] Text 138
         MemberIdentification <MmbId> [0..*] ± 138
         Country <Ctry> [0..1] CodeSet C5 138
         AccountIdentification <AcctId> [0..1] ± 139
       PaymentSearch <PmtSch> [0..1]  C9, C10,
C11,
C13,
C14,
C15
139
         MessageIdentification <MsgId> [0..*] Text 144
         RequestedExecutionDate <ReqdExctnDt> [0..*]  144
{Or           DateTimeSearch <DtTmSch> [1..1]  145
{Or             FromDateTime <FrDtTm> [1..1] DateTime 145
Or             ToDateTime <ToDtTm> [1..1] DateTime 145
Or}             DateTimeRange <DtTmRg> [1..1] ± 145
Or}           DateSearch <DtSch> [1..1]  146
{Or             FromDate <FrDt> [1..1] Date 146
Or             ToDate <ToDt> [1..1] Date 146
Or             FromToDate <FrToDt> [1..1] ± 146
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 117 February 2025
```

## File page 118

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             EqualDate <EQDt> [1..1] Date 146
Or}             NotEqualDate <NEQDt> [1..1] Date 147
         PaymentIdentification <PmtId> [0..*]  147
{Or           TransactionIdentification <TxId> [1..1] Text 148
Or           UETR <UETR> [1..1] IdentifierSet 149
Or           QueueIdentification <QId> [1..1]  149
             QueueIdentification <QId> [1..1] Text 149
             PositionInQueue <PosInQ> [1..1] Text 149
Or           LongBusinessIdentification <LngBizId> [1..1]  C17 149
             TransactionIdentification <TxId> [0..1] Text 150
             UETR <UETR> [0..1] IdentifierSet 150
             InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 151
             InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 151
             PaymentMethod <PmtMtd> [0..1]  151
{Or               FINMessageType <FINMT> [1..1] Text 151
Or               XMLMessageName <XMLMsgNm> [1..1] Text 151
Or               Proprietary <Prtry> [1..1] Text 151
Or}               Instrument <Instrm> [1..1] CodeSet 151
             InstructingAgent <InstgAgt> [1..1] ± 152
             InstructedAgent <InstdAgt> [1..1] ± 153
             EntryType <NtryTp> [0..1] IdentifierSet 154
             EndToEndIdentification <EndToEndId> [0..1] Text 154
Or           ShortBusinessIdentification <ShrtBizId> [1..1]  C18 154
             TransactionIdentification <TxId> [0..1] Text 155
             UETR <UETR> [0..1] IdentifierSet 155
             InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 155
             InstructingAgent <InstgAgt> [1..1] ± 155
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 156
         Status <Sts> [0..*]  156
           PaymentInstructionStatus <PmtInstrSts> [0..1]  157
{Or             PendingStatus <PdgSts> [1..1] CodeSet 157
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 118 February 2025
```

## File page 119

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             FinalStatus <FnlSts> [1..1] CodeSet 158
Or}             PendingAndFinalStatus <PdgAndFnlSts> [1..1] CodeSet 159
           PaymentInstructionStatusDateTime
<PmtInstrStsDtTm>
[0..1]  159
{Or             FromDateTime <FrDtTm> [1..1] DateTime 159
Or             ToDateTime <ToDtTm> [1..1] DateTime 159
Or}             DateTimeRange <DtTmRg> [1..1] ± 159
           ProprietaryStatusReason <PrtryStsRsn> [0..1] Text 160
         InstructedAmount <InstdAmt> [0..*] ± 160
         InstructedAmountCurrency <InstdAmtCcy> [0..*] CodeSet C2 160
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 160
         InterbankSettlementAmount <IntrBkSttlmAmt> [0..*] ± 161
         InterbankSettlementAmountCurrency
<IntrBkSttlmAmtCcy>
[0..*] CodeSet C1 161
         PaymentMethod <PmtMtd> [0..*]  161
{Or           FINMessageType <FINMT> [1..1] Text 161
Or           XMLMessageName <XMLMsgNm> [1..1] Text 162
Or           Proprietary <Prtry> [1..1] Text 162
Or}           Instrument <Instrm> [1..1] CodeSet 162
         PaymentType <PmtTp> [0..*]  163
{Or           Code <Cd> [1..1] CodeSet 163
Or}           Proprietary <Prtry> [1..1] Text 165
         Priority <Prty> [0..*]  165
{Or           Code <Cd> [1..1] CodeSet 165
Or}           Proprietary <Prtry> [1..1] Text 165
         ProcessingValidityTime <PrcgVldtyTm> [0..*]  165
{Or           FromDateTime <FrDtTm> [1..1] DateTime 166
Or           ToDateTime <ToDtTm> [1..1] DateTime 166
Or}           DateTimeRange <DtTmRg> [1..1] ± 166
         Instruction <Instr> [0..*] CodeSet 166
         TransactionIdentification <TxId> [0..*] Text 167
         UETR <UETR> [0..*] IdentifierSet 167
         InterbankSettlementDate <IntrBkSttlmDt> [0..*] Date 167
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 119 February 2025
```

## File page 120

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         EndToEndIdentification <EndToEndId> [0..*] Text 167
         Parties <Pties> [0..1]  167
           InstructingAgent <InstgAgt> [0..1] ± 168
           InstructedAgent <InstdAgt> [0..1] ± 169
           UltimateDebtor <UltmtDbtr> [0..1]  170
{Or             Party <Pty> [1..1] ± 170
Or}             Agent <Agt> [1..1] ± 171
           Debtor <Dbtr> [0..1]  172
{Or             Party <Pty> [1..1] ± 172
Or}             Agent <Agt> [1..1] ± 173
           DebtorAgent <DbtrAgt> [0..1] ± 174
           InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 175
           InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 176
           IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 176
           IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 177
           IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 178
           CreditorAgent <CdtrAgt> [0..1] ± 179
           Creditor <Cdtr> [0..1]  180
{Or             Party <Pty> [1..1] ± 180
Or}             Agent <Agt> [1..1] ± 181
           UltimateCreditor <UltmtCdtr> [0..1]  182
{Or             Party <Pty> [1..1] ± 182
Or}             Agent <Agt> [1..1] ± 183
       AccountEntrySearch <AcctNtrySch> [0..1]  C6, C7 184
         AccountIdentification <AcctId> [0..*]  186
{Or           Equal <EQ> [1..1] ± 186
Or           ContainText <CTTxt> [1..1] Text 186
Or}           NotContainText <NCTTxt> [1..1] Text 187
         EntryAmount <NtryAmt> [0..*] ± 187
         EntryAmountCurrency <NtryAmtCcy> [0..*] CodeSet C2 187
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 187
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 120 February 2025
```

## File page 121

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         EntryStatus <NtrySts> [0..*] CodeSet 187
         EntryDate <NtryDt> [0..*]  188
{Or           DateTimeSearch <DtTmSch> [1..1]  189
{Or             FromDateTime <FrDtTm> [1..1] DateTime 189
Or             ToDateTime <ToDtTm> [1..1] DateTime 189
Or}             DateTimeRange <DtTmRg> [1..1] ± 189
Or}           DateSearch <DtSch> [1..1]  189
{Or             FromDate <FrDt> [1..1] Date 190
Or             ToDate <ToDt> [1..1] Date 190
Or             FromToDate <FrToDt> [1..1] ± 190
Or             EqualDate <EQDt> [1..1] Date 190
Or}             NotEqualDate <NEQDt> [1..1] Date 190
         AccountOwner <AcctOwnr> [0..1] ± 190
         AccountServicer <AcctSvcr> [0..1] ± 191
     StatementReport <StmtRpt> [0..1] CodeSet 192
     ReturnCriteria <RtrCrit> [0..1]  192
       PaymentToReturnCriteria <PmtToRtrCrit> [0..1]  194
         SystemIdentificationIndicator <SysIdInd> [0..1] Indicator 194
         MemberIdentificationIndicator <MmbIdInd> [0..1] Indicator 195
         CountryIdentificationIndicator <CtryIdInd> [0..1] Indicator 195
         AccountIdentificationIndicator <AcctIdInd> [0..1] Indicator 195
       PaymentFromReturnCriteria <PmtFrRtrCrit> [0..1]  195
         SystemIdentificationIndicator <SysIdInd> [0..1] Indicator 195
         MemberIdentificationIndicator <MmbIdInd> [0..1] Indicator 196
         CountryIdentificationIndicator <CtryIdInd> [0..1] Indicator 196
         AccountIdentificationIndicator <AcctIdInd> [0..1] Indicator 196
       AccountCashEntryReturnCriteria
<AcctCshNtryRtrCrit>
[0..1]  196
         EntryReferenceIndicator <NtryRefInd> [0..1] Indicator 197
         AccountTypeIndicator <AcctTpInd> [0..1] Indicator 197
         EntryAmountIndicator <NtryAmtInd> [0..1] Indicator 197
         AccountCurrencyIndicator <AcctCcyInd> [0..1] Indicator 197
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 121 February 2025
```

## File page 122

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         EntryStatusIndicator <NtryStsInd> [0..1] Indicator 198
         EntryDateIndicator <NtryDtInd> [0..1] Indicator 198
         AccountServicerIndicator <AcctSvcrInd> [0..1] Indicator 198
         AccountOwnerIndicator <AcctOwnrInd> [0..1] Indicator 198
       PaymentReturnCriteria <PmtRtrCrit> [0..1]  198
         MessageIdentificationIndicator <MsgIdInd> [0..1] Indicator 200
         RequestedExecutionDateIndicator
<ReqdExctnDtInd>
[0..1] Indicator 200
         InstructionIndicator <InstrInd> [0..1] Indicator 200
         InstructionStatusReturnCriteria <InstrStsRtrCrit> [0..1]  200
           PaymentInstructionStatusIndicator
<PmtInstrStsInd>
[1..1] Indicator 200
           PaymentInstructionStatusDateTimeIndicator
<PmtInstrStsDtTmInd>
[0..1] Indicator 201
           PaymentInstructionStatusReasonIndicator
<PmtInstrStsRsnInd>
[0..1] Indicator 201
         InstructedAmountIndicator <InstdAmtInd> [0..1] Indicator 201
         CreditDebitIndicator <CdtDbtInd> [0..1] Indicator 201
         InterbankSettlementAmountIndicator
<IntrBkSttlmAmtInd>
[0..1] Indicator 201
         PriorityIndicator <PrtyInd> [0..1] Indicator 202
         ProcessingValidityTimeIndicator
<PrcgVldtyTmInd>
[0..1] Indicator 202
         PurposeIndicator <PurpInd> [0..1] Indicator 202
         InstructionCopyIndicator <InstrCpyInd> [0..1] Indicator 202
         PaymentMessageTypeIndicator <PmtMTInd> [0..1] Indicator 202
         PaymentTypeIndicator <PmtTpInd> [0..1] Indicator 202
         TransactionIdentificationIndicator <TxIdInd> [0..1] Indicator 203
         InterbankSettlementDateIndicator
<IntrBkSttlmDtInd>
[0..1] Indicator 203
         EndToEndIdentificationIndicator <EndToEndIdInd> [0..1] Indicator 203
         PaymentMethodIndicator <PmtMtdInd> [0..1] Indicator 203
         DebtorIndicator <DbtrInd> [0..1] Indicator 203
         DebtorAgentIndicator <DbtrAgtInd> [0..1] Indicator 204
         InstructingReimbursementAgentIndicator
<InstgRmbrsmntAgtInd>
[0..1] Indicator 204
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 122 February 2025
```

