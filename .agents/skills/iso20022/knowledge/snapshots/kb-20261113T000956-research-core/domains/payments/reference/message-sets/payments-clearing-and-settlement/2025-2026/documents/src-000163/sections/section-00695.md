---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [949, 950]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 949 to 950.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 949

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 978
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 979
     ReferenceNumber <RefNb> [0..1] Text 980
     Date <Dt> [0..1] Date 981
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 981
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 981
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 981
   SecuritiesData <SctiesData> [0..*]  981
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 982
     Amount <Amt> [0..1] Amount C1, C8 982
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 982
7.4.2.40.30.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
949 March 2026
```

## File page 950

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  951
     CodeOrProprietary <CdOrPrtry> [1..1]  951
{Or       Code <Cd> [1..1] CodeSet 951
Or}       Proprietary <Prtry> [1..1] Text 951
     Issuer <Issr> [0..1] Text 951
   Number <Nb> [0..1] Text 952
   RelatedDate <RltdDt> [0..1]  952
     Type <Tp> [1..1]  952
{Or       Code <Cd> [1..1] CodeSet 952
Or}       Proprietary <Prtry> [1..1] Text 952
     Date <Dt> [1..1] Date 952
   LineDetails <LineDtls> [0..*]  953
     Identification <Id> [1..*]  953
       Type <Tp> [0..1]  954
         CodeOrProprietary <CdOrPrtry> [1..1]  954
{Or           Code <Cd> [1..1] CodeSet 954
Or}           Proprietary <Prtry> [1..1] Text 954
         Issuer <Issr> [0..1] Text 955
       Number <Nb> [0..1] Text 955
       RelatedDate <RltdDt> [0..1] Date 955
     Description <Desc> [0..1] Text 955
     Amount <Amt> [0..1]  C57 955
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
         Type <Tp> [1..1]  956
{Or           Code <Cd> [1..1] CodeSet 957
Or}           Proprietary <Prtry> [1..1] Text 957
         Amount <Amt> [1..1] Amount C2, C9 957
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  957
         Amount <Amt> [1..1] Amount C2, C9 957
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 958
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
950 March 2026
```

