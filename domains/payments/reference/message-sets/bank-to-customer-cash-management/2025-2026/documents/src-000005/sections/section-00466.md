---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [692, 693]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 692 to 693.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 692

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 721
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 722
     ReferenceNumber <RefNb> [0..1] Text 723
     Date <Dt> [0..1] Date 724
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 724
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 724
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 724
   SecuritiesData <SctiesData> [0..*]  724
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 725
     Amount <Amt> [0..1] Amount C1, C7 725
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 725
4.4.2.14.18.2.15.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
692 March 2026
```

## File page 693

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  694
     CodeOrProprietary <CdOrPrtry> [1..1]  694
{Or       Code <Cd> [1..1] CodeSet 694
Or}       Proprietary <Prtry> [1..1] Text 694
     Issuer <Issr> [0..1] Text 694
   Number <Nb> [0..1] Text 695
   RelatedDate <RltdDt> [0..1]  695
     Type <Tp> [1..1]  695
{Or       Code <Cd> [1..1] CodeSet 695
Or}       Proprietary <Prtry> [1..1] Text 695
     Date <Dt> [1..1] Date 695
   LineDetails <LineDtls> [0..*]  696
     Identification <Id> [1..*]  696
       Type <Tp> [0..1]  697
         CodeOrProprietary <CdOrPrtry> [1..1]  697
{Or           Code <Cd> [1..1] CodeSet 697
Or}           Proprietary <Prtry> [1..1] Text 697
         Issuer <Issr> [0..1] Text 698
       Number <Nb> [0..1] Text 698
       RelatedDate <RltdDt> [0..1] Date 698
     Description <Desc> [0..1] Text 698
     Amount <Amt> [0..1]  C26 698
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  699
         Type <Tp> [1..1]  699
{Or           Code <Cd> [1..1] CodeSet 700
Or}           Proprietary <Prtry> [1..1] Text 700
         Amount <Amt> [1..1] Amount C2, C6 700
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  700
         Amount <Amt> [1..1] Amount C2, C6 700
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 701
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
693 March 2026
```

