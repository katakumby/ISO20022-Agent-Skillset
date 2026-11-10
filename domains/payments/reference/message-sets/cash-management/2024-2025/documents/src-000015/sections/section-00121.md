---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.3 StatementReport <StmtRpt>"]
file_pages: [192, 193]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.3 StatementReport <StmtRpt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 192 to 193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 192

```text
AccountServicer <AcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
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
4.4.2.2.2.3  StatementReport <StmtRpt>
Presence: [0..1]
Definition: Indicates the format of the requested report.
Datatype: "ReportIndicator1Code" on page 872
CodeName Name Definition
STND Standard Requested report must contain
information in the format of a statement.
PRPR Proprietary Requested report must contain
information in a bilaterally agreed format.
4.4.2.2.2.4  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected payment transaction report.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 192 February 2025
```

## File page 193

```text
ReturnCriteria <RtrCrit> contains the following TransactionReturnCriteria5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 193 February 2025
```

