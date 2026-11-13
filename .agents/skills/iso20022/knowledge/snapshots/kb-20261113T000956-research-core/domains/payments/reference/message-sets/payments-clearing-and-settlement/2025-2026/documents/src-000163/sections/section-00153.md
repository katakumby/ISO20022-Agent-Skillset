---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.1 Unstructured <Ustrd>"]
file_pages: [207, 208, 209, 210]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.1 Unstructured <Ustrd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 207 to 210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 207

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 240
         Issuer <Issr> [0..1] Text 240
       Garnishee <Grnshee> [0..1] ± 240
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 241
       ReferenceNumber <RefNb> [0..1] Text 242
       Date <Dt> [0..1] Date 243
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 243
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 243
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 243
     SecuritiesData <SctiesData> [0..*]  243
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 244
       Amount <Amt> [0..1] Amount C1, C10 244
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 244
3.4.2.35.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 1244
3.4.2.35.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
207 March 2026
```

## File page 208

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  211
     Type <Tp> [0..1]  213
       CodeOrProprietary <CdOrPrtry> [1..1]  213
{Or         Code <Cd> [1..1] CodeSet 213
Or}         Proprietary <Prtry> [1..1] Text 213
       Issuer <Issr> [0..1] Text 213
     Number <Nb> [0..1] Text 214
     RelatedDate <RltdDt> [0..1]  214
       Type <Tp> [1..1]  214
{Or         Code <Cd> [1..1] CodeSet 214
Or}         Proprietary <Prtry> [1..1] Text 214
       Date <Dt> [1..1] Date 214
     LineDetails <LineDtls> [0..*]  215
       Identification <Id> [1..*]  215
         Type <Tp> [0..1]  216
           CodeOrProprietary <CdOrPrtry> [1..1]  216
{Or             Code <Cd> [1..1] CodeSet 216
Or}             Proprietary <Prtry> [1..1] Text 216
           Issuer <Issr> [0..1] Text 217
         Number <Nb> [0..1] Text 217
         RelatedDate <RltdDt> [0..1] Date 217
       Description <Desc> [0..1] Text 217
       Amount <Amt> [0..1]  C27 217
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  218
           Type <Tp> [1..1]  218
{Or             Code <Cd> [1..1] CodeSet 219
Or}             Proprietary <Prtry> [1..1] Text 219
           Amount <Amt> [1..1] Amount C2, C11 219
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  219
           Amount <Amt> [1..1] Amount C2, C11 219
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
208 March 2026
```

## File page 209

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 220
           Reason <Rsn> [0..1] Text 220
           AdditionalInformation <AddtlInf> [0..1] Text 220
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 220
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  221
       Type <Tp> [1..1]  221
{Or         Code <Cd> [1..1] CodeSet 222
Or}         Proprietary <Prtry> [1..1] Text 222
       Amount <Amt> [1..1] Amount C2, C11 222
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  222
       Amount <Amt> [1..1] Amount C2, C11 222
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 223
       Reason <Rsn> [0..1] Text 223
       AdditionalInformation <AddtlInf> [0..1] Text 223
   CreditorReferenceInformation <CdtrRefInf> [0..1]  223
     Type <Tp> [0..1]  224
       CodeOrProprietary <CdOrPrtry> [1..1]  224
{Or         Code <Cd> [1..1] CodeSet 224
Or}         Proprietary <Prtry> [1..1] Text 224
       Issuer <Issr> [0..1] Text 225
     Reference <Ref> [0..1] Text 225
   Invoicer <Invcr> [0..1] ± 225
   Invoicee <Invcee> [0..1] ± 226
   TaxRemittance <TaxRmt> [0..1]  227
     Creditor <Cdtr> [0..1] ± 229
     Debtor <Dbtr> [0..1] ± 229
     UltimateDebtor <UltmtDbtr> [0..1] ± 229
     AdministrationZone <AdmstnZone> [0..1] Text 230
     ReferenceNumber <RefNb> [0..1] Text 230
     Method <Mtd> [0..1] Text 230
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C11 230
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
209 March 2026
```

## File page 210

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C11 231
     Date <Dt> [0..1] Date 231
     SequenceNumber <SeqNb> [0..1] Quantity 231
     Record <Rcrd> [0..*]  231
       Type <Tp> [0..1] Text 232
       Category <Ctgy> [0..1] Text 232
       CategoryDetails <CtgyDtls> [0..1] Text 232
       DebtorStatus <DbtrSts> [0..1] Text 233
       CertificateIdentification <CertId> [0..1] Text 233
       FormsCode <FrmsCd> [0..1] Text 233
       Period <Prd> [0..1]  233
         Year <Yr> [0..1] Year 233
         Type <Tp> [0..1] CodeSet 233
         FromToDate <FrToDt> [0..1] ± 234
       TaxAmount <TaxAmt> [0..1]  235
         Rate <Rate> [0..1] Rate 235
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C11 235
         TotalAmount <TtlAmt> [0..1] Amount C2, C11 235
         Details <Dtls> [0..*]  236
           Period <Prd> [0..1]  236
             Year <Yr> [0..1] Year 236
             Type <Tp> [0..1] CodeSet 237
             FromToDate <FrToDt> [0..1] ± 237
           Amount <Amt> [1..1] Amount C2, C11 238
       AdditionalInformation <AddtlInf> [0..1] Text 238
   GarnishmentRemittance <GrnshmtRmt> [0..1]  238
     Type <Tp> [1..1]  239
       CodeOrProprietary <CdOrPrtry> [1..1]  239
{Or         Code <Cd> [1..1] CodeSet 240
Or}         Proprietary <Prtry> [1..1] Text 240
       Issuer <Issr> [0..1] Text 240
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
210 March 2026
```

