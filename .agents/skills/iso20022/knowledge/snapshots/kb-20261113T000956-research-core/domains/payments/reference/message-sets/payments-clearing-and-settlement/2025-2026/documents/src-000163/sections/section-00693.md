---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.29 Tax <Tax>", "7.4.2.40.29.11 Record <Rcrd>", "7.4.2.40.29.11.8 TaxAmount <TaxAmt>", "7.4.2.40.29.11.8.4 Details <Dtls>", "7.4.2.40.29.11.8.4.2 Amount <Amt>"]
file_pages: [941, 942, 943, 944]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.29.11.8.4.2 Amount <Amt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 941 to 944.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 941

```text
Definition: Range of time between a start date and an end date for which the tax report is provided.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 1168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 1168
   ToDate <ToDt> [1..1] Date 1168
7.4.2.40.29.11.8.4.2  Amount <Amt>
Presence: [1..1]
Definition: Underlying tax amount related to the specified period.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.2.40.29.11.9  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details of the tax record.
Datatype: "Max140Text" on page 1244
7.4.2.40.30  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
941 March 2026
```

## File page 942

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 945
   Structured <Strd> [0..*]  945
     ReferredDocumentInformation <RfrdDocInf> [0..*]  949
       Type <Tp> [0..1]  951
         CodeOrProprietary <CdOrPrtry> [1..1]  951
{Or           Code <Cd> [1..1] CodeSet 951
Or}           Proprietary <Prtry> [1..1] Text 951
         Issuer <Issr> [0..1] Text 951
       Number <Nb> [0..1] Text 952
       RelatedDate <RltdDt> [0..1]  952
         Type <Tp> [1..1]  952
{Or           Code <Cd> [1..1] CodeSet 952
Or}           Proprietary <Prtry> [1..1] Text 952
         Date <Dt> [1..1] Date 952
       LineDetails <LineDtls> [0..*]  953
         Identification <Id> [1..*]  953
           Type <Tp> [0..1]  954
             CodeOrProprietary <CdOrPrtry> [1..1]  954
{Or               Code <Cd> [1..1] CodeSet 954
Or}               Proprietary <Prtry> [1..1] Text 954
             Issuer <Issr> [0..1] Text 955
           Number <Nb> [0..1] Text 955
           RelatedDate <RltdDt> [0..1] Date 955
         Description <Desc> [0..1] Text 955
         Amount <Amt> [0..1]  C57 955
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
             Type <Tp> [1..1]  956
{Or               Code <Cd> [1..1] CodeSet 957
Or}               Proprietary <Prtry> [1..1] Text 957
             Amount <Amt> [1..1] Amount C2, C9 957
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
942 March 2026
```

## File page 943

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  957
             Amount <Amt> [1..1] Amount C2, C9 957
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 958
             Reason <Rsn> [0..1] Text 958
             AdditionalInformation <AddtlInf> [0..1] Text 958
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C57 958
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  959
         Type <Tp> [1..1]  959
{Or           Code <Cd> [1..1] CodeSet 960
Or}           Proprietary <Prtry> [1..1] Text 960
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
{Or           Code <Cd> [1..1] CodeSet 962
Or}           Proprietary <Prtry> [1..1] Text 962
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
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
943 March 2026
```

## File page 944

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Method <Mtd> [0..1] Text 968
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C9 968
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
{Or           Code <Cd> [1..1] CodeSet 978
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
944 March 2026
```

