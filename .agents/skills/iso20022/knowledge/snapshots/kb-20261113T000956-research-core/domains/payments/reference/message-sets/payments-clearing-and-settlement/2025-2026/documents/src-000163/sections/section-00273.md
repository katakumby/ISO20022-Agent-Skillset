---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>"]
file_pages: [391, 392, 393, 394]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11 RemittanceInformation <RmtInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 391 to 394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 391

```text
CreditTransferMandate <CdtTrfMndt> contains the following elements (see
"CreditTransferMandateData1" on page 1169 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 1169
   Type <Tp> [0..1] ± 1169
   DateOfSignature <DtOfSgntr> [0..1] Date 1170
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 1170
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 1170
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1170
   FinalPaymentDate <FnlPmtDt> [0..1] Date 1170
   Frequency <Frqcy> [0..1] ± 1171
   Reason <Rsn> [0..1]  1171
{Or     Code <Cd> [1..1] CodeSet 1171
Or}     Proprietary <Prtry> [1..1] Text 1171
4.4.3.27.11  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
391 March 2026
```

## File page 392

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 395
   Structured <Strd> [0..*]  395
     ReferredDocumentInformation <RfrdDocInf> [0..*]  399
       Type <Tp> [0..1]  401
         CodeOrProprietary <CdOrPrtry> [1..1]  401
{Or           Code <Cd> [1..1] CodeSet 401
Or}           Proprietary <Prtry> [1..1] Text 401
         Issuer <Issr> [0..1] Text 401
       Number <Nb> [0..1] Text 402
       RelatedDate <RltdDt> [0..1]  402
         Type <Tp> [1..1]  402
{Or           Code <Cd> [1..1] CodeSet 402
Or}           Proprietary <Prtry> [1..1] Text 402
         Date <Dt> [1..1] Date 402
       LineDetails <LineDtls> [0..*]  403
         Identification <Id> [1..*]  403
           Type <Tp> [0..1]  404
             CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or               Code <Cd> [1..1] CodeSet 404
Or}               Proprietary <Prtry> [1..1] Text 404
             Issuer <Issr> [0..1] Text 405
           Number <Nb> [0..1] Text 405
           RelatedDate <RltdDt> [0..1] Date 405
         Description <Desc> [0..1] Text 405
         Amount <Amt> [0..1]  C59 405
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
             Type <Tp> [1..1]  406
{Or               Code <Cd> [1..1] CodeSet 407
Or}               Proprietary <Prtry> [1..1] Text 407
             Amount <Amt> [1..1] Amount C2, C12 407
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
392 March 2026
```

## File page 393

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  407
             Amount <Amt> [1..1] Amount C2, C12 407
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
             Reason <Rsn> [0..1] Text 408
             AdditionalInformation <AddtlInf> [0..1] Text 408
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C59 408
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  409
         Type <Tp> [1..1]  409
{Or           Code <Cd> [1..1] CodeSet 410
Or}           Proprietary <Prtry> [1..1] Text 410
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
{Or           Code <Cd> [1..1] CodeSet 412
Or}           Proprietary <Prtry> [1..1] Text 412
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
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
393 March 2026
```

## File page 394

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Method <Mtd> [0..1] Text 418
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 418
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
{Or           Code <Cd> [1..1] CodeSet 428
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
394 March 2026
```

