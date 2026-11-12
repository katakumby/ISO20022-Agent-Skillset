---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.1 Unstructured <Ustrd>"]
file_pages: [395, 396, 397, 398]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.1 Unstructured <Ustrd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 395 to 398.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 395

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 428
         Issuer <Issr> [0..1] Text 428
       Garnishee <Grnshee> [0..1] ± 428
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 429
       ReferenceNumber <RefNb> [0..1] Text 430
       Date <Dt> [0..1] Date 431
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 431
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 431
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 431
     SecuritiesData <SctiesData> [0..*]  431
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 432
       Amount <Amt> [0..1] Amount C1, C11 432
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 432
4.4.3.27.11.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 1244
4.4.3.27.11.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
395 March 2026
```

## File page 396

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  399
     Type <Tp> [0..1]  401
       CodeOrProprietary <CdOrPrtry> [1..1]  401
{Or         Code <Cd> [1..1] CodeSet 401
Or}         Proprietary <Prtry> [1..1] Text 401
       Issuer <Issr> [0..1] Text 401
     Number <Nb> [0..1] Text 402
     RelatedDate <RltdDt> [0..1]  402
       Type <Tp> [1..1]  402
{Or         Code <Cd> [1..1] CodeSet 402
Or}         Proprietary <Prtry> [1..1] Text 402
       Date <Dt> [1..1] Date 402
     LineDetails <LineDtls> [0..*]  403
       Identification <Id> [1..*]  403
         Type <Tp> [0..1]  404
           CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or             Code <Cd> [1..1] CodeSet 404
Or}             Proprietary <Prtry> [1..1] Text 404
           Issuer <Issr> [0..1] Text 405
         Number <Nb> [0..1] Text 405
         RelatedDate <RltdDt> [0..1] Date 405
       Description <Desc> [0..1] Text 405
       Amount <Amt> [0..1]  C59 405
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
           Type <Tp> [1..1]  406
{Or             Code <Cd> [1..1] CodeSet 407
Or}             Proprietary <Prtry> [1..1] Text 407
           Amount <Amt> [1..1] Amount C2, C12 407
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  407
           Amount <Amt> [1..1] Amount C2, C12 407
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
396 March 2026
```

## File page 397

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
           Reason <Rsn> [0..1] Text 408
           AdditionalInformation <AddtlInf> [0..1] Text 408
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C59 408
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  409
       Type <Tp> [1..1]  409
{Or         Code <Cd> [1..1] CodeSet 410
Or}         Proprietary <Prtry> [1..1] Text 410
       Amount <Amt> [1..1] Amount C2, C12 410
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  410
       Amount <Amt> [1..1] Amount C2, C12 410
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 411
       Reason <Rsn> [0..1] Text 411
       AdditionalInformation <AddtlInf> [0..1] Text 411
   CreditorReferenceInformation <CdtrRefInf> [0..1]  411
     Type <Tp> [0..1]  412
       CodeOrProprietary <CdOrPrtry> [1..1]  412
{Or         Code <Cd> [1..1] CodeSet 412
Or}         Proprietary <Prtry> [1..1] Text 412
       Issuer <Issr> [0..1] Text 413
     Reference <Ref> [0..1] Text 413
   Invoicer <Invcr> [0..1] ± 413
   Invoicee <Invcee> [0..1] ± 414
   TaxRemittance <TaxRmt> [0..1]  415
     Creditor <Cdtr> [0..1] ± 417
     Debtor <Dbtr> [0..1] ± 417
     UltimateDebtor <UltmtDbtr> [0..1] ± 417
     AdministrationZone <AdmstnZone> [0..1] Text 418
     ReferenceNumber <RefNb> [0..1] Text 418
     Method <Mtd> [0..1] Text 418
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 418
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
397 March 2026
```

## File page 398

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 419
     Date <Dt> [0..1] Date 419
     SequenceNumber <SeqNb> [0..1] Quantity 419
     Record <Rcrd> [0..*]  419
       Type <Tp> [0..1] Text 420
       Category <Ctgy> [0..1] Text 420
       CategoryDetails <CtgyDtls> [0..1] Text 420
       DebtorStatus <DbtrSts> [0..1] Text 421
       CertificateIdentification <CertId> [0..1] Text 421
       FormsCode <FrmsCd> [0..1] Text 421
       Period <Prd> [0..1]  421
         Year <Yr> [0..1] Year 421
         Type <Tp> [0..1] CodeSet 421
         FromToDate <FrToDt> [0..1] ± 422
       TaxAmount <TaxAmt> [0..1]  423
         Rate <Rate> [0..1] Rate 423
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 423
         TotalAmount <TtlAmt> [0..1] Amount C2, C12 423
         Details <Dtls> [0..*]  424
           Period <Prd> [0..1]  424
             Year <Yr> [0..1] Year 424
             Type <Tp> [0..1] CodeSet 425
             FromToDate <FrToDt> [0..1] ± 425
           Amount <Amt> [1..1] Amount C2, C12 426
       AdditionalInformation <AddtlInf> [0..1] Text 426
   GarnishmentRemittance <GrnshmtRmt> [0..1]  426
     Type <Tp> [1..1]  427
       CodeOrProprietary <CdOrPrtry> [1..1]  427
{Or         Code <Cd> [1..1] CodeSet 428
Or}         Proprietary <Prtry> [1..1] Text 428
       Issuer <Issr> [0..1] Text 428
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
398 March 2026
```

