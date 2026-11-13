---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [223, 224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 223 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 223

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 252
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 253
     ReferenceNumber <RefNb> [0..1] Text 254
     Date <Dt> [0..1] Date 255
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 255
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 255
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 255
   SecuritiesData <SctiesData> [0..*]  255
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 256
     Amount <Amt> [0..1] Amount C1, C9 256
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 256
3.4.3.7.12.11.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 223 March 2026
```

## File page 224

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  225
     CodeOrProprietary <CdOrPrtry> [1..1]  225
{Or       Code <Cd> [1..1] CodeSet 225
Or}       Proprietary <Prtry> [1..1] Text 225
     Issuer <Issr> [0..1] Text 225
   Number <Nb> [0..1] Text 226
   RelatedDate <RltdDt> [0..1]  226
     Type <Tp> [1..1]  226
{Or       Code <Cd> [1..1] CodeSet 226
Or}       Proprietary <Prtry> [1..1] Text 226
     Date <Dt> [1..1] Date 226
   LineDetails <LineDtls> [0..*]  227
     Identification <Id> [1..*]  227
       Type <Tp> [0..1]  228
         CodeOrProprietary <CdOrPrtry> [1..1]  228
{Or           Code <Cd> [1..1] CodeSet 228
Or}           Proprietary <Prtry> [1..1] Text 228
         Issuer <Issr> [0..1] Text 229
       Number <Nb> [0..1] Text 229
       RelatedDate <RltdDt> [0..1] Date 229
     Description <Desc> [0..1] Text 229
     Amount <Amt> [0..1]  C24 229
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  230
         Type <Tp> [1..1]  230
{Or           Code <Cd> [1..1] CodeSet 231
Or}           Proprietary <Prtry> [1..1] Text 231
         Amount <Amt> [1..1] Amount C2, C8 231
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  231
         Amount <Amt> [1..1] Amount C2, C8 231
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 232
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 224 March 2026
```

