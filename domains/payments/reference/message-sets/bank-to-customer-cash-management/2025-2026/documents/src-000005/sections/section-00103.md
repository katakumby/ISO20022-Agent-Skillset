---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [174, 175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 174 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 174

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 203
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 204
     ReferenceNumber <RefNb> [0..1] Text 205
     Date <Dt> [0..1] Date 206
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 206
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 206
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 206
   SecuritiesData <SctiesData> [0..*]  206
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 207
     Amount <Amt> [0..1] Amount C1, C7 207
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 207
2.4.2.15.18.2.15.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
174 March 2026
```

## File page 175

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  176
     CodeOrProprietary <CdOrPrtry> [1..1]  176
{Or       Code <Cd> [1..1] CodeSet 176
Or}       Proprietary <Prtry> [1..1] Text 176
     Issuer <Issr> [0..1] Text 176
   Number <Nb> [0..1] Text 177
   RelatedDate <RltdDt> [0..1]  177
     Type <Tp> [1..1]  177
{Or       Code <Cd> [1..1] CodeSet 177
Or}       Proprietary <Prtry> [1..1] Text 177
     Date <Dt> [1..1] Date 177
   LineDetails <LineDtls> [0..*]  178
     Identification <Id> [1..*]  178
       Type <Tp> [0..1]  179
         CodeOrProprietary <CdOrPrtry> [1..1]  179
{Or           Code <Cd> [1..1] CodeSet 179
Or}           Proprietary <Prtry> [1..1] Text 179
         Issuer <Issr> [0..1] Text 180
       Number <Nb> [0..1] Text 180
       RelatedDate <RltdDt> [0..1] Date 180
     Description <Desc> [0..1] Text 180
     Amount <Amt> [0..1]  C27 180
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  181
         Type <Tp> [1..1]  181
{Or           Code <Cd> [1..1] CodeSet 182
Or}           Proprietary <Prtry> [1..1] Text 182
         Amount <Amt> [1..1] Amount C2, C6 182
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  182
         Amount <Amt> [1..1] Amount C2, C6 182
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 183
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
175 March 2026
```

