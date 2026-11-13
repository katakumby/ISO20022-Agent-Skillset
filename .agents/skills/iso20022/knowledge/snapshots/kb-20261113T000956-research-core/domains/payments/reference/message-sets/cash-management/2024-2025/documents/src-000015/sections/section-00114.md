---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.4 AccountEntrySearch <AcctNtrySch>"]
file_pages: [184, 185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.4 AccountEntrySearch <AcctNtrySch>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 184 to 185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
4.4.2.2.2.2.4  AccountEntrySearch <AcctNtrySch>
Presence: [0..1]
Definition: Defines the criteria which are used to search for a cash entry.
Impacted by: C6 "EntryAmountCreditDebitIndicator1Rule", C7 "EntryAmountCreditDebitIndicator2Rule"
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 184 February 2025
```

## File page 185

```text
AccountEntrySearch <AcctNtrySch> contains the following CashAccountEntrySearch8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..*]  186
{Or     Equal <EQ> [1..1] ± 186
Or     ContainText <CTTxt> [1..1] Text 186
Or}     NotContainText <NCTTxt> [1..1] Text 187
   EntryAmount <NtryAmt> [0..*] ± 187
   EntryAmountCurrency <NtryAmtCcy> [0..*] CodeSet C2 187
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 187
   EntryStatus <NtrySts> [0..*] CodeSet 187
   EntryDate <NtryDt> [0..*]  188
{Or     DateTimeSearch <DtTmSch> [1..1]  189
{Or       FromDateTime <FrDtTm> [1..1] DateTime 189
Or       ToDateTime <ToDtTm> [1..1] DateTime 189
Or}       DateTimeRange <DtTmRg> [1..1] ± 189
Or}     DateSearch <DtSch> [1..1]  189
{Or       FromDate <FrDt> [1..1] Date 190
Or       ToDate <ToDt> [1..1] Date 190
Or       FromToDate <FrToDt> [1..1] ± 190
Or       EqualDate <EQDt> [1..1] Date 190
Or}       NotEqualDate <NEQDt> [1..1] Date 190
   AccountOwner <AcctOwnr> [0..1] ± 190
   AccountServicer <AcctSvcr> [0..1] ± 191
Constraints
• EntryAmountCreditDebitIndicator1Rule
If at least one occurrence of EntryAmount/CurrencyAndAmountRange/CreditDebitIndicator is
present, then CreditDebitIndicator is not allowed.
If EntryAmount/CurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
If CreditDebitIndicator is present then
all occurrences of EntryAmount/CurrencyAndAmountRange/CreditDebitIndicator must be absent and
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 185 February 2025
```

