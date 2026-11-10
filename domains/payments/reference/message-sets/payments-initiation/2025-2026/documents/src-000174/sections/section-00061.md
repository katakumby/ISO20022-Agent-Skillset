---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.1 Unstructured <Ustrd>"]
file_pages: [91, 92, 93, 94]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.1 Unstructured <Ustrd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 91 to 94.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 91

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 124
         Issuer <Issr> [0..1] Text 124
       Garnishee <Grnshee> [0..1] ± 124
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 125
       ReferenceNumber <RefNb> [0..1] Text 126
       Date <Dt> [0..1] Date 127
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C19 127
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 127
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 127
     SecuritiesData <SctiesData> [0..*]  127
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 128
       Amount <Amt> [0..1] Amount C1, C20 128
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 128
2.4.2.19.26.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 608
2.4.2.19.26.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 91 March 2026
```

## File page 92

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  95
     Type <Tp> [0..1]  97
       CodeOrProprietary <CdOrPrtry> [1..1]  97
{Or         Code <Cd> [1..1] CodeSet 97
Or}         Proprietary <Prtry> [1..1] Text 97
       Issuer <Issr> [0..1] Text 97
     Number <Nb> [0..1] Text 98
     RelatedDate <RltdDt> [0..1]  98
       Type <Tp> [1..1]  98
{Or         Code <Cd> [1..1] CodeSet 98
Or}         Proprietary <Prtry> [1..1] Text 98
       Date <Dt> [1..1] Date 98
     LineDetails <LineDtls> [0..*]  99
       Identification <Id> [1..*]  99
         Type <Tp> [0..1]  100
           CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or             Code <Cd> [1..1] CodeSet 100
Or}             Proprietary <Prtry> [1..1] Text 100
           Issuer <Issr> [0..1] Text 101
         Number <Nb> [0..1] Text 101
         RelatedDate <RltdDt> [0..1] Date 101
       Description <Desc> [0..1] Text 101
       Amount <Amt> [0..1]  C33 101
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  102
           Type <Tp> [1..1]  102
{Or             Code <Cd> [1..1] CodeSet 103
Or}             Proprietary <Prtry> [1..1] Text 103
           Amount <Amt> [1..1] Amount C2, C19 103
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  103
           Amount <Amt> [1..1] Amount C2, C19 103
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 92 March 2026
```

## File page 93

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 104
           Reason <Rsn> [0..1] Text 104
           AdditionalInformation <AddtlInf> [0..1] Text 104
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C33 104
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  105
       Type <Tp> [1..1]  105
{Or         Code <Cd> [1..1] CodeSet 106
Or}         Proprietary <Prtry> [1..1] Text 106
       Amount <Amt> [1..1] Amount C2, C19 106
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  106
       Amount <Amt> [1..1] Amount C2, C19 106
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 107
       Reason <Rsn> [0..1] Text 107
       AdditionalInformation <AddtlInf> [0..1] Text 107
   CreditorReferenceInformation <CdtrRefInf> [0..1]  107
     Type <Tp> [0..1]  108
       CodeOrProprietary <CdOrPrtry> [1..1]  108
{Or         Code <Cd> [1..1] CodeSet 108
Or}         Proprietary <Prtry> [1..1] Text 108
       Issuer <Issr> [0..1] Text 109
     Reference <Ref> [0..1] Text 109
   Invoicer <Invcr> [0..1] ± 109
   Invoicee <Invcee> [0..1] ± 110
   TaxRemittance <TaxRmt> [0..1]  111
     Creditor <Cdtr> [0..1] ± 113
     Debtor <Dbtr> [0..1] ± 113
     UltimateDebtor <UltmtDbtr> [0..1] ± 113
     AdministrationZone <AdmstnZone> [0..1] Text 114
     ReferenceNumber <RefNb> [0..1] Text 114
     Method <Mtd> [0..1] Text 114
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C19 114
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 93 March 2026
```

## File page 94

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C19 115
     Date <Dt> [0..1] Date 115
     SequenceNumber <SeqNb> [0..1] Quantity 115
     Record <Rcrd> [0..*]  115
       Type <Tp> [0..1] Text 116
       Category <Ctgy> [0..1] Text 116
       CategoryDetails <CtgyDtls> [0..1] Text 116
       DebtorStatus <DbtrSts> [0..1] Text 117
       CertificateIdentification <CertId> [0..1] Text 117
       FormsCode <FrmsCd> [0..1] Text 117
       Period <Prd> [0..1]  117
         Year <Yr> [0..1] Year 117
         Type <Tp> [0..1] CodeSet 117
         FromToDate <FrToDt> [0..1] ± 118
       TaxAmount <TaxAmt> [0..1]  119
         Rate <Rate> [0..1] Rate 119
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C19 119
         TotalAmount <TtlAmt> [0..1] Amount C2, C19 119
         Details <Dtls> [0..*]  120
           Period <Prd> [0..1]  120
             Year <Yr> [0..1] Year 120
             Type <Tp> [0..1] CodeSet 121
             FromToDate <FrToDt> [0..1] ± 121
           Amount <Amt> [1..1] Amount C2, C19 122
       AdditionalInformation <AddtlInf> [0..1] Text 122
   GarnishmentRemittance <GrnshmtRmt> [0..1]  122
     Type <Tp> [1..1]  123
       CodeOrProprietary <CdOrPrtry> [1..1]  123
{Or         Code <Cd> [1..1] CodeSet 124
Or}         Proprietary <Prtry> [1..1] Text 124
       Issuer <Issr> [0..1] Text 124
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 94 March 2026
```

