---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [354, 355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 354 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 354

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 383
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 384
     ReferenceNumber <RefNb> [0..1] Text 385
     Date <Dt> [0..1] Date 386
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 386
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 386
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 386
   SecuritiesData <SctiesData> [0..*]  386
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 387
     Amount <Amt> [0..1] Amount C1, C10 387
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 387
4.4.3.8.9.11.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 354 March 2026
```

## File page 355

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  356
     CodeOrProprietary <CdOrPrtry> [1..1]  356
{Or       Code <Cd> [1..1] CodeSet 356
Or}       Proprietary <Prtry> [1..1] Text 356
     Issuer <Issr> [0..1] Text 356
   Number <Nb> [0..1] Text 357
   RelatedDate <RltdDt> [0..1]  357
     Type <Tp> [1..1]  357
{Or       Code <Cd> [1..1] CodeSet 357
Or}       Proprietary <Prtry> [1..1] Text 357
     Date <Dt> [1..1] Date 357
   LineDetails <LineDtls> [0..*]  358
     Identification <Id> [1..*]  358
       Type <Tp> [0..1]  359
         CodeOrProprietary <CdOrPrtry> [1..1]  359
{Or           Code <Cd> [1..1] CodeSet 359
Or}           Proprietary <Prtry> [1..1] Text 359
         Issuer <Issr> [0..1] Text 360
       Number <Nb> [0..1] Text 360
       RelatedDate <RltdDt> [0..1] Date 360
     Description <Desc> [0..1] Text 360
     Amount <Amt> [0..1]  C24 360
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  361
         Type <Tp> [1..1]  361
{Or           Code <Cd> [1..1] CodeSet 362
Or}           Proprietary <Prtry> [1..1] Text 362
         Amount <Amt> [1..1] Amount C2, C9 362
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  362
         Amount <Amt> [1..1] Amount C2, C9 362
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 363
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 355 March 2026
```

