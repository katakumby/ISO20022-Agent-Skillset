---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.1 Unstructured <Ustrd>"]
file_pages: [1108, 1109, 1110, 1111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.1 Unstructured <Ustrd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1108 to 1111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1108

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 1141
         Issuer <Issr> [0..1] Text 1141
       Garnishee <Grnshee> [0..1] ± 1141
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 1142
       ReferenceNumber <RefNb> [0..1] Text 1143
       Date <Dt> [0..1] Date 1144
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 1144
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 1144
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 1144
     SecuritiesData <SctiesData> [0..*]  1144
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1145
       Amount <Amt> [0..1] Amount C1, C9 1145
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 1145
9.4.3.11.11.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 1244
9.4.3.11.11.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1108 March 2026
```

## File page 1109

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  1112
     Type <Tp> [0..1]  1114
       CodeOrProprietary <CdOrPrtry> [1..1]  1114
{Or         Code <Cd> [1..1] CodeSet 1114
Or}         Proprietary <Prtry> [1..1] Text 1114
       Issuer <Issr> [0..1] Text 1114
     Number <Nb> [0..1] Text 1115
     RelatedDate <RltdDt> [0..1]  1115
       Type <Tp> [1..1]  1115
{Or         Code <Cd> [1..1] CodeSet 1115
Or}         Proprietary <Prtry> [1..1] Text 1115
       Date <Dt> [1..1] Date 1115
     LineDetails <LineDtls> [0..*]  1116
       Identification <Id> [1..*]  1116
         Type <Tp> [0..1]  1117
           CodeOrProprietary <CdOrPrtry> [1..1]  1117
{Or             Code <Cd> [1..1] CodeSet 1117
Or}             Proprietary <Prtry> [1..1] Text 1117
           Issuer <Issr> [0..1] Text 1118
         Number <Nb> [0..1] Text 1118
         RelatedDate <RltdDt> [0..1] Date 1118
       Description <Desc> [0..1] Text 1118
       Amount <Amt> [0..1]  C18 1118
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1119
           Type <Tp> [1..1]  1119
{Or             Code <Cd> [1..1] CodeSet 1120
Or}             Proprietary <Prtry> [1..1] Text 1120
           Amount <Amt> [1..1] Amount C2, C8 1120
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  1120
           Amount <Amt> [1..1] Amount C2, C8 1120
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1109 March 2026
```

## File page 1110

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1121
           Reason <Rsn> [0..1] Text 1121
           AdditionalInformation <AddtlInf> [0..1] Text 1121
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C18 1121
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1122
       Type <Tp> [1..1]  1122
{Or         Code <Cd> [1..1] CodeSet 1123
Or}         Proprietary <Prtry> [1..1] Text 1123
       Amount <Amt> [1..1] Amount C2, C8 1123
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  1123
       Amount <Amt> [1..1] Amount C2, C8 1123
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1124
       Reason <Rsn> [0..1] Text 1124
       AdditionalInformation <AddtlInf> [0..1] Text 1124
   CreditorReferenceInformation <CdtrRefInf> [0..1]  1124
     Type <Tp> [0..1]  1125
       CodeOrProprietary <CdOrPrtry> [1..1]  1125
{Or         Code <Cd> [1..1] CodeSet 1125
Or}         Proprietary <Prtry> [1..1] Text 1125
       Issuer <Issr> [0..1] Text 1126
     Reference <Ref> [0..1] Text 1126
   Invoicer <Invcr> [0..1] ± 1126
   Invoicee <Invcee> [0..1] ± 1127
   TaxRemittance <TaxRmt> [0..1]  1128
     Creditor <Cdtr> [0..1] ± 1130
     Debtor <Dbtr> [0..1] ± 1130
     UltimateDebtor <UltmtDbtr> [0..1] ± 1130
     AdministrationZone <AdmstnZone> [0..1] Text 1131
     ReferenceNumber <RefNb> [0..1] Text 1131
     Method <Mtd> [0..1] Text 1131
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 1131
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1110 March 2026
```

## File page 1111

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 1132
     Date <Dt> [0..1] Date 1132
     SequenceNumber <SeqNb> [0..1] Quantity 1132
     Record <Rcrd> [0..*]  1132
       Type <Tp> [0..1] Text 1133
       Category <Ctgy> [0..1] Text 1133
       CategoryDetails <CtgyDtls> [0..1] Text 1133
       DebtorStatus <DbtrSts> [0..1] Text 1134
       CertificateIdentification <CertId> [0..1] Text 1134
       FormsCode <FrmsCd> [0..1] Text 1134
       Period <Prd> [0..1]  1134
         Year <Yr> [0..1] Year 1134
         Type <Tp> [0..1] CodeSet 1134
         FromToDate <FrToDt> [0..1] ± 1135
       TaxAmount <TaxAmt> [0..1]  1136
         Rate <Rate> [0..1] Rate 1136
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 1136
         TotalAmount <TtlAmt> [0..1] Amount C2, C8 1136
         Details <Dtls> [0..*]  1137
           Period <Prd> [0..1]  1137
             Year <Yr> [0..1] Year 1137
             Type <Tp> [0..1] CodeSet 1138
             FromToDate <FrToDt> [0..1] ± 1138
           Amount <Amt> [1..1] Amount C2, C8 1139
       AdditionalInformation <AddtlInf> [0..1] Text 1139
   GarnishmentRemittance <GrnshmtRmt> [0..1]  1139
     Type <Tp> [1..1]  1140
       CodeOrProprietary <CdOrPrtry> [1..1]  1140
{Or         Code <Cd> [1..1] CodeSet 1141
Or}         Proprietary <Prtry> [1..1] Text 1141
       Issuer <Issr> [0..1] Text 1141
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1111 March 2026
```

