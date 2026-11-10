---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [1112, 1113]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1112 to 1113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1112

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 1141
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 1142
     ReferenceNumber <RefNb> [0..1] Text 1143
     Date <Dt> [0..1] Date 1144
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 1144
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 1144
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 1144
   SecuritiesData <SctiesData> [0..*]  1144
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1145
     Amount <Amt> [0..1] Amount C1, C9 1145
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 1145
9.4.3.11.11.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1112 March 2026
```

## File page 1113

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  1114
     CodeOrProprietary <CdOrPrtry> [1..1]  1114
{Or       Code <Cd> [1..1] CodeSet 1114
Or}       Proprietary <Prtry> [1..1] Text 1114
     Issuer <Issr> [0..1] Text 1114
   Number <Nb> [0..1] Text 1115
   RelatedDate <RltdDt> [0..1]  1115
     Type <Tp> [1..1]  1115
{Or       Code <Cd> [1..1] CodeSet 1115
Or}       Proprietary <Prtry> [1..1] Text 1115
     Date <Dt> [1..1] Date 1115
   LineDetails <LineDtls> [0..*]  1116
     Identification <Id> [1..*]  1116
       Type <Tp> [0..1]  1117
         CodeOrProprietary <CdOrPrtry> [1..1]  1117
{Or           Code <Cd> [1..1] CodeSet 1117
Or}           Proprietary <Prtry> [1..1] Text 1117
         Issuer <Issr> [0..1] Text 1118
       Number <Nb> [0..1] Text 1118
       RelatedDate <RltdDt> [0..1] Date 1118
     Description <Desc> [0..1] Text 1118
     Amount <Amt> [0..1]  C18 1118
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1119
         Type <Tp> [1..1]  1119
{Or           Code <Cd> [1..1] CodeSet 1120
Or}           Proprietary <Prtry> [1..1] Text 1120
         Amount <Amt> [1..1] Amount C2, C8 1120
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  1120
         Amount <Amt> [1..1] Amount C2, C8 1120
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1121
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1113 March 2026
```

