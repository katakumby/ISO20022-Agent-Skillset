---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>"]
file_pages: [215, 216, 217, 218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11 RemittanceInformation <RmtInf>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 215 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 215

```text
CreditTransferMandate <CdtTrfMndt> contains the following elements (see
"CreditTransferMandateData1" on page 535 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 535
   Type <Tp> [0..1] ± 535
   DateOfSignature <DtOfSgntr> [0..1] Date 536
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 536
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 536
   FirstPaymentDate <FrstPmtDt> [0..1] Date 536
   FinalPaymentDate <FnlPmtDt> [0..1] Date 536
   Frequency <Frqcy> [0..1] ± 537
   Reason <Rsn> [0..1]  537
{Or     Code <Cd> [1..1] CodeSet 537
Or}     Proprietary <Prtry> [1..1] Text 537
3.4.3.7.12.11  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 215 March 2026
```

## File page 216

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 219
   Structured <Strd> [0..*]  219
     ReferredDocumentInformation <RfrdDocInf> [0..*]  223
       Type <Tp> [0..1]  225
         CodeOrProprietary <CdOrPrtry> [1..1]  225
{Or           Code <Cd> [1..1] CodeSet 225
Or}           Proprietary <Prtry> [1..1] Text 225
         Issuer <Issr> [0..1] Text 225
       Number <Nb> [0..1] Text 226
       RelatedDate <RltdDt> [0..1]  226
         Type <Tp> [1..1]  226
{Or           Code <Cd> [1..1] CodeSet 226
Or}           Proprietary <Prtry> [1..1] Text 226
         Date <Dt> [1..1] Date 226
       LineDetails <LineDtls> [0..*]  227
         Identification <Id> [1..*]  227
           Type <Tp> [0..1]  228
             CodeOrProprietary <CdOrPrtry> [1..1]  228
{Or               Code <Cd> [1..1] CodeSet 228
Or}               Proprietary <Prtry> [1..1] Text 228
             Issuer <Issr> [0..1] Text 229
           Number <Nb> [0..1] Text 229
           RelatedDate <RltdDt> [0..1] Date 229
         Description <Desc> [0..1] Text 229
         Amount <Amt> [0..1]  C24 229
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  230
             Type <Tp> [1..1]  230
{Or               Code <Cd> [1..1] CodeSet 231
Or}               Proprietary <Prtry> [1..1] Text 231
             Amount <Amt> [1..1] Amount C2, C8 231
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 216 March 2026
```

## File page 217

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  231
             Amount <Amt> [1..1] Amount C2, C8 231
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 232
             Reason <Rsn> [0..1] Text 232
             AdditionalInformation <AddtlInf> [0..1] Text 232
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C24 232
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  233
         Type <Tp> [1..1]  233
{Or           Code <Cd> [1..1] CodeSet 234
Or}           Proprietary <Prtry> [1..1] Text 234
         Amount <Amt> [1..1] Amount C2, C8 234
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  234
         Amount <Amt> [1..1] Amount C2, C8 234
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 235
         Reason <Rsn> [0..1] Text 235
         AdditionalInformation <AddtlInf> [0..1] Text 235
     CreditorReferenceInformation <CdtrRefInf> [0..1]  235
       Type <Tp> [0..1]  236
         CodeOrProprietary <CdOrPrtry> [1..1]  236
{Or           Code <Cd> [1..1] CodeSet 236
Or}           Proprietary <Prtry> [1..1] Text 236
         Issuer <Issr> [0..1] Text 237
       Reference <Ref> [0..1] Text 237
     Invoicer <Invcr> [0..1] ± 237
     Invoicee <Invcee> [0..1] ± 238
     TaxRemittance <TaxRmt> [0..1]  239
       Creditor <Cdtr> [0..1] ± 241
       Debtor <Dbtr> [0..1] ± 241
       UltimateDebtor <UltmtDbtr> [0..1] ± 241
       AdministrationZone <AdmstnZone> [0..1] Text 242
       ReferenceNumber <RefNb> [0..1] Text 242
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 217 March 2026
```

## File page 218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Method <Mtd> [0..1] Text 242
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 242
       TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 243
       Date <Dt> [0..1] Date 243
       SequenceNumber <SeqNb> [0..1] Quantity 243
       Record <Rcrd> [0..*]  243
         Type <Tp> [0..1] Text 244
         Category <Ctgy> [0..1] Text 244
         CategoryDetails <CtgyDtls> [0..1] Text 244
         DebtorStatus <DbtrSts> [0..1] Text 245
         CertificateIdentification <CertId> [0..1] Text 245
         FormsCode <FrmsCd> [0..1] Text 245
         Period <Prd> [0..1]  245
           Year <Yr> [0..1] Year 245
           Type <Tp> [0..1] CodeSet 245
           FromToDate <FrToDt> [0..1] ± 246
         TaxAmount <TaxAmt> [0..1]  247
           Rate <Rate> [0..1] Rate 247
           TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 247
           TotalAmount <TtlAmt> [0..1] Amount C2, C8 247
           Details <Dtls> [0..*]  248
             Period <Prd> [0..1]  248
               Year <Yr> [0..1] Year 248
               Type <Tp> [0..1] CodeSet 249
               FromToDate <FrToDt> [0..1] ± 249
             Amount <Amt> [1..1] Amount C2, C8 250
         AdditionalInformation <AddtlInf> [0..1] Text 250
     GarnishmentRemittance <GrnshmtRmt> [0..1]  250
       Type <Tp> [1..1]  251
         CodeOrProprietary <CdOrPrtry> [1..1]  251
{Or           Code <Cd> [1..1] CodeSet 252
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 218 March 2026
```

