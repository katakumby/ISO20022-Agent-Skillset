---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.1 Unstructured <Ustrd>"]
file_pages: [945, 946, 947, 948]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.1 Unstructured <Ustrd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 945 to 948.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 945

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 978
         Issuer <Issr> [0..1] Text 978
       Garnishee <Grnshee> [0..1] ± 978
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 979
       ReferenceNumber <RefNb> [0..1] Text 980
       Date <Dt> [0..1] Date 981
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 981
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 981
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 981
     SecuritiesData <SctiesData> [0..*]  981
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 982
       Amount <Amt> [0..1] Amount C1, C8 982
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 982
7.4.2.40.30.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 1244
7.4.2.40.30.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
945 March 2026
```

## File page 946

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  949
     Type <Tp> [0..1]  951
       CodeOrProprietary <CdOrPrtry> [1..1]  951
{Or         Code <Cd> [1..1] CodeSet 951
Or}         Proprietary <Prtry> [1..1] Text 951
       Issuer <Issr> [0..1] Text 951
     Number <Nb> [0..1] Text 952
     RelatedDate <RltdDt> [0..1]  952
       Type <Tp> [1..1]  952
{Or         Code <Cd> [1..1] CodeSet 952
Or}         Proprietary <Prtry> [1..1] Text 952
       Date <Dt> [1..1] Date 952
     LineDetails <LineDtls> [0..*]  953
       Identification <Id> [1..*]  953
         Type <Tp> [0..1]  954
           CodeOrProprietary <CdOrPrtry> [1..1]  954
{Or             Code <Cd> [1..1] CodeSet 954
Or}             Proprietary <Prtry> [1..1] Text 954
           Issuer <Issr> [0..1] Text 955
         Number <Nb> [0..1] Text 955
         RelatedDate <RltdDt> [0..1] Date 955
       Description <Desc> [0..1] Text 955
       Amount <Amt> [0..1]  C57 955
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
           Type <Tp> [1..1]  956
{Or             Code <Cd> [1..1] CodeSet 957
Or}             Proprietary <Prtry> [1..1] Text 957
           Amount <Amt> [1..1] Amount C2, C9 957
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  957
           Amount <Amt> [1..1] Amount C2, C9 957
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
946 March 2026
```

## File page 947

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 958
           Reason <Rsn> [0..1] Text 958
           AdditionalInformation <AddtlInf> [0..1] Text 958
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C57 958
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  959
       Type <Tp> [1..1]  959
{Or         Code <Cd> [1..1] CodeSet 960
Or}         Proprietary <Prtry> [1..1] Text 960
       Amount <Amt> [1..1] Amount C2, C9 960
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  960
       Amount <Amt> [1..1] Amount C2, C9 960
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 961
       Reason <Rsn> [0..1] Text 961
       AdditionalInformation <AddtlInf> [0..1] Text 961
   CreditorReferenceInformation <CdtrRefInf> [0..1]  961
     Type <Tp> [0..1]  962
       CodeOrProprietary <CdOrPrtry> [1..1]  962
{Or         Code <Cd> [1..1] CodeSet 962
Or}         Proprietary <Prtry> [1..1] Text 962
       Issuer <Issr> [0..1] Text 963
     Reference <Ref> [0..1] Text 963
   Invoicer <Invcr> [0..1] ± 963
   Invoicee <Invcee> [0..1] ± 964
   TaxRemittance <TaxRmt> [0..1]  965
     Creditor <Cdtr> [0..1] ± 967
     Debtor <Dbtr> [0..1] ± 967
     UltimateDebtor <UltmtDbtr> [0..1] ± 967
     AdministrationZone <AdmstnZone> [0..1] Text 968
     ReferenceNumber <RefNb> [0..1] Text 968
     Method <Mtd> [0..1] Text 968
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 968
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
947 March 2026
```

## File page 948

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C9 969
     Date <Dt> [0..1] Date 969
     SequenceNumber <SeqNb> [0..1] Quantity 969
     Record <Rcrd> [0..*]  969
       Type <Tp> [0..1] Text 970
       Category <Ctgy> [0..1] Text 970
       CategoryDetails <CtgyDtls> [0..1] Text 970
       DebtorStatus <DbtrSts> [0..1] Text 971
       CertificateIdentification <CertId> [0..1] Text 971
       FormsCode <FrmsCd> [0..1] Text 971
       Period <Prd> [0..1]  971
         Year <Yr> [0..1] Year 971
         Type <Tp> [0..1] CodeSet 971
         FromToDate <FrToDt> [0..1] ± 972
       TaxAmount <TaxAmt> [0..1]  973
         Rate <Rate> [0..1] Rate 973
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 973
         TotalAmount <TtlAmt> [0..1] Amount C2, C9 973
         Details <Dtls> [0..*]  974
           Period <Prd> [0..1]  974
             Year <Yr> [0..1] Year 974
             Type <Tp> [0..1] CodeSet 975
             FromToDate <FrToDt> [0..1] ± 975
           Amount <Amt> [1..1] Amount C2, C9 976
       AdditionalInformation <AddtlInf> [0..1] Text 976
   GarnishmentRemittance <GrnshmtRmt> [0..1]  976
     Type <Tp> [1..1]  977
       CodeOrProprietary <CdOrPrtry> [1..1]  977
{Or         Code <Cd> [1..1] CodeSet 978
Or}         Proprietary <Prtry> [1..1] Text 978
       Issuer <Issr> [0..1] Text 978
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
948 March 2026
```

