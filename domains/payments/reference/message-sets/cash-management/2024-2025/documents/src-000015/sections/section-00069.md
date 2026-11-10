---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.1 NewQueryName <NewQryNm>"]
file_pages: [130, 131, 132, 133, 134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.1 NewQueryName <NewQryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 130 to 134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 130

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       CreditorAgentIndicator <CdtrAgtInd> [0..1] Indicator 204
       CreditorIndicator <CdtrInd> [0..1] Indicator 205
Constraints
• SearchAndReturnCriteriaAndStatementReportRule
The following combinations are allowed: only Search Criteria, or only Return Criteria, or only a
Statement Report, or a combination of Search and Return criteria, or a combination of Search criteria
and a Statement Report.
Rule rationale:
- If ReturnCriteria are present, they define the expected report.
- If StatementReport is present, it indicates that a statement-type report needs to be returned. In this
case, the return message will contain information equivalent to that present in field 61 (Statement
Line) of FIN standards, for example, value date, entry date, debit/credit indicator, amount, transaction
type identification code, reference for the account owner, reference of the account servicing
institution and supplementary details.
- If the StatementReportIndicator equals "false" or "0" (No), this means that the report type is pre-
defined between the transaction administrator and the member.
Following Must be True
    /SearchCriteria[1] Must be present
 Or    /StatementReport Must be present
 Or    /ReturnCriteria Must be present
4.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria on which the information is extracted.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 130 February 2025
```

## File page 131

```text
SearchCriteria <SchCrit> contains the following TransactionSearchCriteria11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentTo <PmtTo> [0..*]  135
     SystemIdentification <SysId> [0..*]  135
{Or       Code <Cd> [1..1] CodeSet 135
Or}       Proprietary <Prtry> [1..1] Text 136
     MemberIdentification <MmbId> [0..*] ± 136
     Country <Ctry> [0..1] CodeSet C5 136
     AccountIdentification <AcctId> [0..1] ± 137
   PaymentFrom <PmtFr> [0..*]  137
     SystemIdentification <SysId> [0..*]  137
{Or       Code <Cd> [1..1] CodeSet 138
Or}       Proprietary <Prtry> [1..1] Text 138
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
{Or       DateTimeSearch <DtTmSch> [1..1]  145
{Or         FromDateTime <FrDtTm> [1..1] DateTime 145
Or         ToDateTime <ToDtTm> [1..1] DateTime 145
Or}         DateTimeRange <DtTmRg> [1..1] ± 145
Or}       DateSearch <DtSch> [1..1]  146
{Or         FromDate <FrDt> [1..1] Date 146
Or         ToDate <ToDt> [1..1] Date 146
Or         FromToDate <FrToDt> [1..1] ± 146
Or         EqualDate <EQDt> [1..1] Date 146
Or}         NotEqualDate <NEQDt> [1..1] Date 147
     PaymentIdentification <PmtId> [0..*]  147
{Or       TransactionIdentification <TxId> [1..1] Text 148
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 131 February 2025
```

## File page 132

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       UETR <UETR> [1..1] IdentifierSet 149
Or       QueueIdentification <QId> [1..1]  149
         QueueIdentification <QId> [1..1] Text 149
         PositionInQueue <PosInQ> [1..1] Text 149
Or       LongBusinessIdentification <LngBizId> [1..1]  C17 149
         TransactionIdentification <TxId> [0..1] Text 150
         UETR <UETR> [0..1] IdentifierSet 150
         InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 151
         InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 151
         PaymentMethod <PmtMtd> [0..1]  151
{Or           FINMessageType <FINMT> [1..1] Text 151
Or           XMLMessageName <XMLMsgNm> [1..1] Text 151
Or           Proprietary <Prtry> [1..1] Text 151
Or}           Instrument <Instrm> [1..1] CodeSet 151
         InstructingAgent <InstgAgt> [1..1] ± 152
         InstructedAgent <InstdAgt> [1..1] ± 153
         EntryType <NtryTp> [0..1] IdentifierSet 154
         EndToEndIdentification <EndToEndId> [0..1] Text 154
Or       ShortBusinessIdentification <ShrtBizId> [1..1]  C18 154
         TransactionIdentification <TxId> [0..1] Text 155
         UETR <UETR> [0..1] IdentifierSet 155
         InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 155
         InstructingAgent <InstgAgt> [1..1] ± 155
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 156
     Status <Sts> [0..*]  156
       PaymentInstructionStatus <PmtInstrSts> [0..1]  157
{Or         PendingStatus <PdgSts> [1..1] CodeSet 157
Or         FinalStatus <FnlSts> [1..1] CodeSet 158
Or}         PendingAndFinalStatus <PdgAndFnlSts> [1..1] CodeSet 159
       PaymentInstructionStatusDateTime
<PmtInstrStsDtTm>
[0..1]  159
{Or         FromDateTime <FrDtTm> [1..1] DateTime 159
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 132 February 2025
```

## File page 133

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         ToDateTime <ToDtTm> [1..1] DateTime 159
Or}         DateTimeRange <DtTmRg> [1..1] ± 159
       ProprietaryStatusReason <PrtryStsRsn> [0..1] Text 160
     InstructedAmount <InstdAmt> [0..*] ± 160
     InstructedAmountCurrency <InstdAmtCcy> [0..*] CodeSet C2 160
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 160
     InterbankSettlementAmount <IntrBkSttlmAmt> [0..*] ± 161
     InterbankSettlementAmountCurrency
<IntrBkSttlmAmtCcy>
[0..*] CodeSet C1 161
     PaymentMethod <PmtMtd> [0..*]  161
{Or       FINMessageType <FINMT> [1..1] Text 161
Or       XMLMessageName <XMLMsgNm> [1..1] Text 162
Or       Proprietary <Prtry> [1..1] Text 162
Or}       Instrument <Instrm> [1..1] CodeSet 162
     PaymentType <PmtTp> [0..*]  163
{Or       Code <Cd> [1..1] CodeSet 163
Or}       Proprietary <Prtry> [1..1] Text 165
     Priority <Prty> [0..*]  165
{Or       Code <Cd> [1..1] CodeSet 165
Or}       Proprietary <Prtry> [1..1] Text 165
     ProcessingValidityTime <PrcgVldtyTm> [0..*]  165
{Or       FromDateTime <FrDtTm> [1..1] DateTime 166
Or       ToDateTime <ToDtTm> [1..1] DateTime 166
Or}       DateTimeRange <DtTmRg> [1..1] ± 166
     Instruction <Instr> [0..*] CodeSet 166
     TransactionIdentification <TxId> [0..*] Text 167
     UETR <UETR> [0..*] IdentifierSet 167
     InterbankSettlementDate <IntrBkSttlmDt> [0..*] Date 167
     EndToEndIdentification <EndToEndId> [0..*] Text 167
     Parties <Pties> [0..1]  167
       InstructingAgent <InstgAgt> [0..1] ± 168
       InstructedAgent <InstdAgt> [0..1] ± 169
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 133 February 2025
```

## File page 134

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       UltimateDebtor <UltmtDbtr> [0..1]  170
{Or         Party <Pty> [1..1] ± 170
Or}         Agent <Agt> [1..1] ± 171
       Debtor <Dbtr> [0..1]  172
{Or         Party <Pty> [1..1] ± 172
Or}         Agent <Agt> [1..1] ± 173
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
{Or         Party <Pty> [1..1] ± 180
Or}         Agent <Agt> [1..1] ± 181
       UltimateCreditor <UltmtCdtr> [0..1]  182
{Or         Party <Pty> [1..1] ± 182
Or}         Agent <Agt> [1..1] ± 183
   AccountEntrySearch <AcctNtrySch> [0..1]  C6, C7 184
     AccountIdentification <AcctId> [0..*]  186
{Or       Equal <EQ> [1..1] ± 186
Or       ContainText <CTTxt> [1..1] Text 186
Or}       NotContainText <NCTTxt> [1..1] Text 187
     EntryAmount <NtryAmt> [0..*] ± 187
     EntryAmountCurrency <NtryAmtCcy> [0..*] CodeSet C2 187
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 187
     EntryStatus <NtrySts> [0..*] CodeSet 187
     EntryDate <NtryDt> [0..*]  188
{Or       DateTimeSearch <DtTmSch> [1..1]  189
{Or         FromDateTime <FrDtTm> [1..1] DateTime 189
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 134 February 2025
```

