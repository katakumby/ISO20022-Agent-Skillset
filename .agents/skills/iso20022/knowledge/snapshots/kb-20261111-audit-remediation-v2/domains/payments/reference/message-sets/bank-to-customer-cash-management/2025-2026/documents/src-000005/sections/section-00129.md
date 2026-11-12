---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.7 GarnishmentRemittance <GrnshmtRmt>", "2.4.2.15.18.2.15.2.7.1 Type <Tp>"]
file_pages: [202]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.7.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 202 to 202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 202

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  202
     CodeOrProprietary <CdOrPrtry> [1..1]  202
{Or       Code <Cd> [1..1] CodeSet 203
Or}       Proprietary <Prtry> [1..1] Text 203
     Issuer <Issr> [0..1] Text 203
   Garnishee <Grnshee> [0..1] ± 203
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 204
   ReferenceNumber <RefNb> [0..1] Text 205
   Date <Dt> [0..1] Date 206
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 206
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 206
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 206
2.4.2.15.18.2.15.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  202
{Or     Code <Cd> [1..1] CodeSet 203
Or}     Proprietary <Prtry> [1..1] Text 203
   Issuer <Issr> [0..1] Text 203
2.4.2.15.18.2.15.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 203
Or}   Proprietary <Prtry> [1..1] Text 203
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
202 March 2026
```

