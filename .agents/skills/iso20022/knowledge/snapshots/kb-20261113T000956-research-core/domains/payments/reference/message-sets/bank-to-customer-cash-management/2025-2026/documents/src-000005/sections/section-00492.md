---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.7 GarnishmentRemittance <GrnshmtRmt>", "4.4.2.14.18.2.15.2.7.1 Type <Tp>"]
file_pages: [720]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.7.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 720 to 720.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 720

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  720
     CodeOrProprietary <CdOrPrtry> [1..1]  720
{Or       Code <Cd> [1..1] CodeSet 721
Or}       Proprietary <Prtry> [1..1] Text 721
     Issuer <Issr> [0..1] Text 721
   Garnishee <Grnshee> [0..1] ± 721
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 722
   ReferenceNumber <RefNb> [0..1] Text 723
   Date <Dt> [0..1] Date 724
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 724
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 724
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 724
4.4.2.14.18.2.15.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  720
{Or     Code <Cd> [1..1] CodeSet 721
Or}     Proprietary <Prtry> [1..1] Text 721
   Issuer <Issr> [0..1] Text 721
4.4.2.14.18.2.15.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 721
Or}   Proprietary <Prtry> [1..1] Text 721
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
720 March 2026
```

