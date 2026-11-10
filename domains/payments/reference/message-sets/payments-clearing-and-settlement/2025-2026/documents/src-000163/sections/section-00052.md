---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.11 RemittanceInformation <RmtInf>", "2.4.3.18.11.2 Structured <Strd>", "2.4.3.18.11.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [83, 84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.11.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 83 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 112
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 113
     ReferenceNumber <RefNb> [0..1] Text 114
     Date <Dt> [0..1] Date 115
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 115
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 115
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 115
   SecuritiesData <SctiesData> [0..*]  115
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 116
     Amount <Amt> [0..1] Amount C1, C9 116
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 116
2.4.3.18.11.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
83 March 2026
```

## File page 84

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  85
     CodeOrProprietary <CdOrPrtry> [1..1]  85
{Or       Code <Cd> [1..1] CodeSet 85
Or}       Proprietary <Prtry> [1..1] Text 85
     Issuer <Issr> [0..1] Text 85
   Number <Nb> [0..1] Text 86
   RelatedDate <RltdDt> [0..1]  86
     Type <Tp> [1..1]  86
{Or       Code <Cd> [1..1] CodeSet 86
Or}       Proprietary <Prtry> [1..1] Text 86
     Date <Dt> [1..1] Date 86
   LineDetails <LineDtls> [0..*]  87
     Identification <Id> [1..*]  87
       Type <Tp> [0..1]  88
         CodeOrProprietary <CdOrPrtry> [1..1]  88
{Or           Code <Cd> [1..1] CodeSet 88
Or}           Proprietary <Prtry> [1..1] Text 88
         Issuer <Issr> [0..1] Text 89
       Number <Nb> [0..1] Text 89
       RelatedDate <RltdDt> [0..1] Date 89
     Description <Desc> [0..1] Text 89
     Amount <Amt> [0..1]  C23 89
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  90
         Type <Tp> [1..1]  90
{Or           Code <Cd> [1..1] CodeSet 91
Or}           Proprietary <Prtry> [1..1] Text 91
         Amount <Amt> [1..1] Amount C2, C8 91
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  91
         Amount <Amt> [1..1] Amount C2, C8 91
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
84 March 2026
```

