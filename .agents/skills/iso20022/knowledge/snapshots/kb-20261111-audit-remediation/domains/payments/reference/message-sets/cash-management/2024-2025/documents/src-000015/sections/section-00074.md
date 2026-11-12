---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.2 PaymentFrom <PmtFr>", "4.4.2.2.2.2.2.4 AccountIdentification <AcctId>"]
file_pages: [139, 140, 141, 142, 143]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.2.4 AccountIdentification <AcctId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 139 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
4.4.2.2.2.2.2.4  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 787 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
4.4.2.2.2.2.3  PaymentSearch <PmtSch>
Presence: [0..1]
Definition: Defines the criteria which are used to search for a payment.
Impacted by: C9 "InstructedAmountCreditDebitIndicator1Rule", C10
"InstructedAmountCreditDebitIndicator2Rule", C11 "InstructedAmountCurrencyRule", C13
"SettlementAmountCreditDebitIndicator1Rule", C14 "SettlementAmountCreditDebitIndicator2Rule", C15
"SettlementAmountCurrencyRule"
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 139 February 2025
```

## File page 140

```text
PaymentSearch <PmtSch> contains the following PaymentSearch10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [0..*] Text 144
   RequestedExecutionDate <ReqdExctnDt> [0..*]  144
{Or     DateTimeSearch <DtTmSch> [1..1]  145
{Or       FromDateTime <FrDtTm> [1..1] DateTime 145
Or       ToDateTime <ToDtTm> [1..1] DateTime 145
Or}       DateTimeRange <DtTmRg> [1..1] ± 145
Or}     DateSearch <DtSch> [1..1]  146
{Or       FromDate <FrDt> [1..1] Date 146
Or       ToDate <ToDt> [1..1] Date 146
Or       FromToDate <FrToDt> [1..1] ± 146
Or       EqualDate <EQDt> [1..1] Date 146
Or}       NotEqualDate <NEQDt> [1..1] Date 147
   PaymentIdentification <PmtId> [0..*]  147
{Or     TransactionIdentification <TxId> [1..1] Text 148
Or     UETR <UETR> [1..1] IdentifierSet 149
Or     QueueIdentification <QId> [1..1]  149
       QueueIdentification <QId> [1..1] Text 149
       PositionInQueue <PosInQ> [1..1] Text 149
Or     LongBusinessIdentification <LngBizId> [1..1]  C17 149
       TransactionIdentification <TxId> [0..1] Text 150
       UETR <UETR> [0..1] IdentifierSet 150
       InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 151
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 151
       PaymentMethod <PmtMtd> [0..1]  151
{Or         FINMessageType <FINMT> [1..1] Text 151
Or         XMLMessageName <XMLMsgNm> [1..1] Text 151
Or         Proprietary <Prtry> [1..1] Text 151
Or}         Instrument <Instrm> [1..1] CodeSet 151
       InstructingAgent <InstgAgt> [1..1] ± 152
       InstructedAgent <InstdAgt> [1..1] ± 153
       EntryType <NtryTp> [0..1] IdentifierSet 154
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 140 February 2025
```

## File page 141

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       EndToEndIdentification <EndToEndId> [0..1] Text 154
Or     ShortBusinessIdentification <ShrtBizId> [1..1]  C18 154
       TransactionIdentification <TxId> [0..1] Text 155
       UETR <UETR> [0..1] IdentifierSet 155
       InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 155
       InstructingAgent <InstgAgt> [1..1] ± 155
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 156
   Status <Sts> [0..*]  156
     PaymentInstructionStatus <PmtInstrSts> [0..1]  157
{Or       PendingStatus <PdgSts> [1..1] CodeSet 157
Or       FinalStatus <FnlSts> [1..1] CodeSet 158
Or}       PendingAndFinalStatus <PdgAndFnlSts> [1..1] CodeSet 159
     PaymentInstructionStatusDateTime
<PmtInstrStsDtTm>
[0..1]  159
{Or       FromDateTime <FrDtTm> [1..1] DateTime 159
Or       ToDateTime <ToDtTm> [1..1] DateTime 159
Or}       DateTimeRange <DtTmRg> [1..1] ± 159
     ProprietaryStatusReason <PrtryStsRsn> [0..1] Text 160
   InstructedAmount <InstdAmt> [0..*] ± 160
   InstructedAmountCurrency <InstdAmtCcy> [0..*] CodeSet C2 160
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 160
   InterbankSettlementAmount <IntrBkSttlmAmt> [0..*] ± 161
   InterbankSettlementAmountCurrency
<IntrBkSttlmAmtCcy>
[0..*] CodeSet C1 161
   PaymentMethod <PmtMtd> [0..*]  161
{Or     FINMessageType <FINMT> [1..1] Text 161
Or     XMLMessageName <XMLMsgNm> [1..1] Text 162
Or     Proprietary <Prtry> [1..1] Text 162
Or}     Instrument <Instrm> [1..1] CodeSet 162
   PaymentType <PmtTp> [0..*]  163
{Or     Code <Cd> [1..1] CodeSet 163
Or}     Proprietary <Prtry> [1..1] Text 165
   Priority <Prty> [0..*]  165
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 141 February 2025
```

## File page 142

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Code <Cd> [1..1] CodeSet 165
Or}     Proprietary <Prtry> [1..1] Text 165
   ProcessingValidityTime <PrcgVldtyTm> [0..*]  165
{Or     FromDateTime <FrDtTm> [1..1] DateTime 166
Or     ToDateTime <ToDtTm> [1..1] DateTime 166
Or}     DateTimeRange <DtTmRg> [1..1] ± 166
   Instruction <Instr> [0..*] CodeSet 166
   TransactionIdentification <TxId> [0..*] Text 167
   UETR <UETR> [0..*] IdentifierSet 167
   InterbankSettlementDate <IntrBkSttlmDt> [0..*] Date 167
   EndToEndIdentification <EndToEndId> [0..*] Text 167
   Parties <Pties> [0..1]  167
     InstructingAgent <InstgAgt> [0..1] ± 168
     InstructedAgent <InstdAgt> [0..1] ± 169
     UltimateDebtor <UltmtDbtr> [0..1]  170
{Or       Party <Pty> [1..1] ± 170
Or}       Agent <Agt> [1..1] ± 171
     Debtor <Dbtr> [0..1]  172
{Or       Party <Pty> [1..1] ± 172
Or}       Agent <Agt> [1..1] ± 173
     DebtorAgent <DbtrAgt> [0..1] ± 174
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 175
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 176
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 176
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 177
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 178
     CreditorAgent <CdtrAgt> [0..1] ± 179
     Creditor <Cdtr> [0..1]  180
{Or       Party <Pty> [1..1] ± 180
Or}       Agent <Agt> [1..1] ± 181
     UltimateCreditor <UltmtCdtr> [0..1]  182
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 142 February 2025
```

## File page 143

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Party <Pty> [1..1] ± 182
Or}       Agent <Agt> [1..1] ± 183
Constraints
• InstructedAmountCreditDebitIndicator1Rule
If at least one occurrence of InstructedAmount/CurrencyAndAmountRange/CreditDebitIndicator is
present, then CreditDebitIndicator is not allowed.
If InstructedAmount/CurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
On Condition
    /InstructedAmount[*]/CurrencyAndAmountRange/CreditDebitIndicator is present
Following Must be True
    /CreditDebitIndicator Must be absent
• InstructedAmountCreditDebitIndicator2Rule
If at least one occurrence of InstructedAmount/ImpliedCurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If InstructedAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
On Condition
    /InstructedAmount[*]/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is 
present
Following Must be True
    /CreditDebitIndicator Must be absent
• InstructedAmountCurrencyRule
If at least one occurrence of InstructedAmount/CurrencyAndAmountRange is present, then no
occurrence of InstructedAmountCurrency is allowed.
If InstructedAmount/CurrencyAndAmountRange is not present, then any occurrence of
InstructedAmountCurrency is optional.
On Condition
    /InstructedAmount[*]/CurrencyAndAmountRange/Currency is present
Following Must be True
    /InstructedAmountCurrency[*] Must be absent
• SettlementAmountCreditDebitIndicator1Rule
If at least one occurrence of InterbankSettlementAmount/CurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If InterbankSettlementAmount/CurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
On Condition
    /InterbankSettlementAmount[*]/CurrencyAndAmountRange/CreditDebitIndicator is 
present
Following Must be True
    /CreditDebitIndicator Must be absent
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 143 February 2025
```

