---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.1 Unstructured <Ustrd>"]
file_pages: [350, 351, 352, 353]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.1 Unstructured <Ustrd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 350 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 350

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 383
         Issuer <Issr> [0..1] Text 383
       Garnishee <Grnshee> [0..1] ± 383
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 384
       ReferenceNumber <RefNb> [0..1] Text 385
       Date <Dt> [0..1] Date 386
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 386
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 386
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 386
     SecuritiesData <SctiesData> [0..*]  386
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 387
       Amount <Amt> [0..1] Amount C1, C10 387
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 387
4.4.3.8.9.11.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 608
4.4.3.8.9.11.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 350 March 2026
```

## File page 351

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  354
     Type <Tp> [0..1]  356
       CodeOrProprietary <CdOrPrtry> [1..1]  356
{Or         Code <Cd> [1..1] CodeSet 356
Or}         Proprietary <Prtry> [1..1] Text 356
       Issuer <Issr> [0..1] Text 356
     Number <Nb> [0..1] Text 357
     RelatedDate <RltdDt> [0..1]  357
       Type <Tp> [1..1]  357
{Or         Code <Cd> [1..1] CodeSet 357
Or}         Proprietary <Prtry> [1..1] Text 357
       Date <Dt> [1..1] Date 357
     LineDetails <LineDtls> [0..*]  358
       Identification <Id> [1..*]  358
         Type <Tp> [0..1]  359
           CodeOrProprietary <CdOrPrtry> [1..1]  359
{Or             Code <Cd> [1..1] CodeSet 359
Or}             Proprietary <Prtry> [1..1] Text 359
           Issuer <Issr> [0..1] Text 360
         Number <Nb> [0..1] Text 360
         RelatedDate <RltdDt> [0..1] Date 360
       Description <Desc> [0..1] Text 360
       Amount <Amt> [0..1]  C24 360
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  361
           Type <Tp> [1..1]  361
{Or             Code <Cd> [1..1] CodeSet 362
Or}             Proprietary <Prtry> [1..1] Text 362
           Amount <Amt> [1..1] Amount C2, C9 362
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  362
           Amount <Amt> [1..1] Amount C2, C9 362
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 351 March 2026
```

## File page 352

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 363
           Reason <Rsn> [0..1] Text 363
           AdditionalInformation <AddtlInf> [0..1] Text 363
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C24 363
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  364
       Type <Tp> [1..1]  364
{Or         Code <Cd> [1..1] CodeSet 365
Or}         Proprietary <Prtry> [1..1] Text 365
       Amount <Amt> [1..1] Amount C2, C9 365
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  365
       Amount <Amt> [1..1] Amount C2, C9 365
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 366
       Reason <Rsn> [0..1] Text 366
       AdditionalInformation <AddtlInf> [0..1] Text 366
   CreditorReferenceInformation <CdtrRefInf> [0..1]  366
     Type <Tp> [0..1]  367
       CodeOrProprietary <CdOrPrtry> [1..1]  367
{Or         Code <Cd> [1..1] CodeSet 367
Or}         Proprietary <Prtry> [1..1] Text 367
       Issuer <Issr> [0..1] Text 368
     Reference <Ref> [0..1] Text 368
   Invoicer <Invcr> [0..1] ± 368
   Invoicee <Invcee> [0..1] ± 369
   TaxRemittance <TaxRmt> [0..1]  370
     Creditor <Cdtr> [0..1] ± 372
     Debtor <Dbtr> [0..1] ± 372
     UltimateDebtor <UltmtDbtr> [0..1] ± 372
     AdministrationZone <AdmstnZone> [0..1] Text 373
     ReferenceNumber <RefNb> [0..1] Text 373
     Method <Mtd> [0..1] Text 373
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 373
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 352 March 2026
```

## File page 353

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 374
     Date <Dt> [0..1] Date 374
     SequenceNumber <SeqNb> [0..1] Quantity 374
     Record <Rcrd> [0..*]  374
       Type <Tp> [0..1] Text 375
       Category <Ctgy> [0..1] Text 375
       CategoryDetails <CtgyDtls> [0..1] Text 375
       DebtorStatus <DbtrSts> [0..1] Text 376
       CertificateIdentification <CertId> [0..1] Text 376
       FormsCode <FrmsCd> [0..1] Text 376
       Period <Prd> [0..1]  376
         Year <Yr> [0..1] Year 376
         Type <Tp> [0..1] CodeSet 376
         FromToDate <FrToDt> [0..1] ± 377
       TaxAmount <TaxAmt> [0..1]  378
         Rate <Rate> [0..1] Rate 378
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 378
         TotalAmount <TtlAmt> [0..1] Amount C2, C9 378
         Details <Dtls> [0..*]  379
           Period <Prd> [0..1]  379
             Year <Yr> [0..1] Year 379
             Type <Tp> [0..1] CodeSet 380
             FromToDate <FrToDt> [0..1] ± 380
           Amount <Amt> [1..1] Amount C2, C9 381
       AdditionalInformation <AddtlInf> [0..1] Text 381
   GarnishmentRemittance <GrnshmtRmt> [0..1]  381
     Type <Tp> [1..1]  382
       CodeOrProprietary <CdOrPrtry> [1..1]  382
{Or         Code <Cd> [1..1] CodeSet 383
Or}         Proprietary <Prtry> [1..1] Text 383
       Issuer <Issr> [0..1] Text 383
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 353 March 2026
```

