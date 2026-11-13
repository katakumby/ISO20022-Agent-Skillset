---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [434, 435]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 434 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 463
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 464
     ReferenceNumber <RefNb> [0..1] Text 465
     Date <Dt> [0..1] Date 466
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 466
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 466
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 466
   SecuritiesData <SctiesData> [0..*]  466
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 467
     Amount <Amt> [0..1] Amount C1, C7 467
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 467
3.4.2.15.18.2.15.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
434 March 2026
```

## File page 435

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  436
     CodeOrProprietary <CdOrPrtry> [1..1]  436
{Or       Code <Cd> [1..1] CodeSet 436
Or}       Proprietary <Prtry> [1..1] Text 436
     Issuer <Issr> [0..1] Text 436
   Number <Nb> [0..1] Text 437
   RelatedDate <RltdDt> [0..1]  437
     Type <Tp> [1..1]  437
{Or       Code <Cd> [1..1] CodeSet 437
Or}       Proprietary <Prtry> [1..1] Text 437
     Date <Dt> [1..1] Date 437
   LineDetails <LineDtls> [0..*]  438
     Identification <Id> [1..*]  438
       Type <Tp> [0..1]  439
         CodeOrProprietary <CdOrPrtry> [1..1]  439
{Or           Code <Cd> [1..1] CodeSet 439
Or}           Proprietary <Prtry> [1..1] Text 439
         Issuer <Issr> [0..1] Text 440
       Number <Nb> [0..1] Text 440
       RelatedDate <RltdDt> [0..1] Date 440
     Description <Desc> [0..1] Text 440
     Amount <Amt> [0..1]  C27 440
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  441
         Type <Tp> [1..1]  441
{Or           Code <Cd> [1..1] CodeSet 442
Or}           Proprietary <Prtry> [1..1] Text 442
         Amount <Amt> [1..1] Amount C2, C6 442
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  442
         Amount <Amt> [1..1] Amount C2, C6 442
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 443
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
435 March 2026
```

