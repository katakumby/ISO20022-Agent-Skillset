---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.11 RemittanceInformation <RmtInf>"]
file_pages: [75, 76, 77, 78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.11 RemittanceInformation <RmtInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 75 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

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
2.4.3.18.11  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
75 March 2026
```

## File page 76

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 79
   Structured <Strd> [0..*]  79
     ReferredDocumentInformation <RfrdDocInf> [0..*]  83
       Type <Tp> [0..1]  85
         CodeOrProprietary <CdOrPrtry> [1..1]  85
{Or           Code <Cd> [1..1] CodeSet 85
Or}           Proprietary <Prtry> [1..1] Text 85
         Issuer <Issr> [0..1] Text 85
       Number <Nb> [0..1] Text 86
       RelatedDate <RltdDt> [0..1]  86
         Type <Tp> [1..1]  86
{Or           Code <Cd> [1..1] CodeSet 86
Or}           Proprietary <Prtry> [1..1] Text 86
         Date <Dt> [1..1] Date 86
       LineDetails <LineDtls> [0..*]  87
         Identification <Id> [1..*]  87
           Type <Tp> [0..1]  88
             CodeOrProprietary <CdOrPrtry> [1..1]  88
{Or               Code <Cd> [1..1] CodeSet 88
Or}               Proprietary <Prtry> [1..1] Text 88
             Issuer <Issr> [0..1] Text 89
           Number <Nb> [0..1] Text 89
           RelatedDate <RltdDt> [0..1] Date 89
         Description <Desc> [0..1] Text 89
         Amount <Amt> [0..1]  C23 89
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  90
             Type <Tp> [1..1]  90
{Or               Code <Cd> [1..1] CodeSet 91
Or}               Proprietary <Prtry> [1..1] Text 91
             Amount <Amt> [1..1] Amount C2, C8 91
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
76 March 2026
```

## File page 77

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  91
             Amount <Amt> [1..1] Amount C2, C8 91
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
             Reason <Rsn> [0..1] Text 92
             AdditionalInformation <AddtlInf> [0..1] Text 92
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C23 92
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  93
         Type <Tp> [1..1]  93
{Or           Code <Cd> [1..1] CodeSet 94
Or}           Proprietary <Prtry> [1..1] Text 94
         Amount <Amt> [1..1] Amount C2, C8 94
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  94
         Amount <Amt> [1..1] Amount C2, C8 94
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 95
         Reason <Rsn> [0..1] Text 95
         AdditionalInformation <AddtlInf> [0..1] Text 95
     CreditorReferenceInformation <CdtrRefInf> [0..1]  95
       Type <Tp> [0..1]  96
         CodeOrProprietary <CdOrPrtry> [1..1]  96
{Or           Code <Cd> [1..1] CodeSet 96
Or}           Proprietary <Prtry> [1..1] Text 96
         Issuer <Issr> [0..1] Text 97
       Reference <Ref> [0..1] Text 97
     Invoicer <Invcr> [0..1] ± 97
     Invoicee <Invcee> [0..1] ± 98
     TaxRemittance <TaxRmt> [0..1]  99
       Creditor <Cdtr> [0..1] ± 101
       Debtor <Dbtr> [0..1] ± 101
       UltimateDebtor <UltmtDbtr> [0..1] ± 101
       AdministrationZone <AdmstnZone> [0..1] Text 102
       ReferenceNumber <RefNb> [0..1] Text 102
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
77 March 2026
```

## File page 78

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Method <Mtd> [0..1] Text 102
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 102
       TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 103
       Date <Dt> [0..1] Date 103
       SequenceNumber <SeqNb> [0..1] Quantity 103
       Record <Rcrd> [0..*]  103
         Type <Tp> [0..1] Text 104
         Category <Ctgy> [0..1] Text 104
         CategoryDetails <CtgyDtls> [0..1] Text 104
         DebtorStatus <DbtrSts> [0..1] Text 105
         CertificateIdentification <CertId> [0..1] Text 105
         FormsCode <FrmsCd> [0..1] Text 105
         Period <Prd> [0..1]  105
           Year <Yr> [0..1] Year 105
           Type <Tp> [0..1] CodeSet 105
           FromToDate <FrToDt> [0..1] ± 106
         TaxAmount <TaxAmt> [0..1]  107
           Rate <Rate> [0..1] Rate 107
           TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 107
           TotalAmount <TtlAmt> [0..1] Amount C2, C8 107
           Details <Dtls> [0..*]  108
             Period <Prd> [0..1]  108
               Year <Yr> [0..1] Year 108
               Type <Tp> [0..1] CodeSet 109
               FromToDate <FrToDt> [0..1] ± 109
             Amount <Amt> [1..1] Amount C2, C8 110
         AdditionalInformation <AddtlInf> [0..1] Text 110
     GarnishmentRemittance <GrnshmtRmt> [0..1]  110
       Type <Tp> [1..1]  111
         CodeOrProprietary <CdOrPrtry> [1..1]  111
{Or           Code <Cd> [1..1] CodeSet 112
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
78 March 2026
```

