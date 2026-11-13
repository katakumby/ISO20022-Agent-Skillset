---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.1 Unstructured <Ustrd>"]
file_pages: [170, 171, 172, 173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.1 Unstructured <Ustrd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 170 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 170

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 203
         Issuer <Issr> [0..1] Text 203
       Garnishee <Grnshee> [0..1] ± 203
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 204
       ReferenceNumber <RefNb> [0..1] Text 205
       Date <Dt> [0..1] Date 206
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 206
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 206
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 206
     SecuritiesData <SctiesData> [0..*]  206
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 207
       Amount <Amt> [0..1] Amount C1, C7 207
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 207
2.4.2.15.18.2.15.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 914
2.4.2.15.18.2.15.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
170 March 2026
```

## File page 171

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  174
     Type <Tp> [0..1]  176
       CodeOrProprietary <CdOrPrtry> [1..1]  176
{Or         Code <Cd> [1..1] CodeSet 176
Or}         Proprietary <Prtry> [1..1] Text 176
       Issuer <Issr> [0..1] Text 176
     Number <Nb> [0..1] Text 177
     RelatedDate <RltdDt> [0..1]  177
       Type <Tp> [1..1]  177
{Or         Code <Cd> [1..1] CodeSet 177
Or}         Proprietary <Prtry> [1..1] Text 177
       Date <Dt> [1..1] Date 177
     LineDetails <LineDtls> [0..*]  178
       Identification <Id> [1..*]  178
         Type <Tp> [0..1]  179
           CodeOrProprietary <CdOrPrtry> [1..1]  179
{Or             Code <Cd> [1..1] CodeSet 179
Or}             Proprietary <Prtry> [1..1] Text 179
           Issuer <Issr> [0..1] Text 180
         Number <Nb> [0..1] Text 180
         RelatedDate <RltdDt> [0..1] Date 180
       Description <Desc> [0..1] Text 180
       Amount <Amt> [0..1]  C27 180
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  181
           Type <Tp> [1..1]  181
{Or             Code <Cd> [1..1] CodeSet 182
Or}             Proprietary <Prtry> [1..1] Text 182
           Amount <Amt> [1..1] Amount C2, C6 182
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  182
           Amount <Amt> [1..1] Amount C2, C6 182
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
171 March 2026
```

## File page 172

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 183
           Reason <Rsn> [0..1] Text 183
           AdditionalInformation <AddtlInf> [0..1] Text 183
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 183
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  184
       Type <Tp> [1..1]  184
{Or         Code <Cd> [1..1] CodeSet 185
Or}         Proprietary <Prtry> [1..1] Text 185
       Amount <Amt> [1..1] Amount C2, C6 185
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  185
       Amount <Amt> [1..1] Amount C2, C6 185
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 186
       Reason <Rsn> [0..1] Text 186
       AdditionalInformation <AddtlInf> [0..1] Text 186
   CreditorReferenceInformation <CdtrRefInf> [0..1]  186
     Type <Tp> [0..1]  187
       CodeOrProprietary <CdOrPrtry> [1..1]  187
{Or         Code <Cd> [1..1] CodeSet 187
Or}         Proprietary <Prtry> [1..1] Text 187
       Issuer <Issr> [0..1] Text 188
     Reference <Ref> [0..1] Text 188
   Invoicer <Invcr> [0..1] ± 188
   Invoicee <Invcee> [0..1] ± 189
   TaxRemittance <TaxRmt> [0..1]  190
     Creditor <Cdtr> [0..1] ± 192
     Debtor <Dbtr> [0..1] ± 192
     UltimateDebtor <UltmtDbtr> [0..1] ± 192
     AdministrationZone <AdmstnZone> [0..1] Text 193
     ReferenceNumber <RefNb> [0..1] Text 193
     Method <Mtd> [0..1] Text 193
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 193
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
172 March 2026
```

## File page 173

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 194
     Date <Dt> [0..1] Date 194
     SequenceNumber <SeqNb> [0..1] Quantity 194
     Record <Rcrd> [0..*]  194
       Type <Tp> [0..1] Text 195
       Category <Ctgy> [0..1] Text 195
       CategoryDetails <CtgyDtls> [0..1] Text 195
       DebtorStatus <DbtrSts> [0..1] Text 196
       CertificateIdentification <CertId> [0..1] Text 196
       FormsCode <FrmsCd> [0..1] Text 196
       Period <Prd> [0..1]  196
         Year <Yr> [0..1] Year 196
         Type <Tp> [0..1] CodeSet 196
         FromToDate <FrToDt> [0..1] ± 197
       TaxAmount <TaxAmt> [0..1]  198
         Rate <Rate> [0..1] Rate 198
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 198
         TotalAmount <TtlAmt> [0..1] Amount C2, C6 198
         Details <Dtls> [0..*]  199
           Period <Prd> [0..1]  199
             Year <Yr> [0..1] Year 199
             Type <Tp> [0..1] CodeSet 200
             FromToDate <FrToDt> [0..1] ± 200
           Amount <Amt> [1..1] Amount C2, C6 201
       AdditionalInformation <AddtlInf> [0..1] Text 201
   GarnishmentRemittance <GrnshmtRmt> [0..1]  201
     Type <Tp> [1..1]  202
       CodeOrProprietary <CdOrPrtry> [1..1]  202
{Or         Code <Cd> [1..1] CodeSet 203
Or}         Proprietary <Prtry> [1..1] Text 203
       Issuer <Issr> [0..1] Text 203
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
173 March 2026
```

