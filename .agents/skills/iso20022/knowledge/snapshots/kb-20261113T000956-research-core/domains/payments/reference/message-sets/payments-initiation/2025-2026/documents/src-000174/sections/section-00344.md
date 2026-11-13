---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [492, 493]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 492 to 493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 521
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 522
     ReferenceNumber <RefNb> [0..1] Text 523
     Date <Dt> [0..1] Date 524
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 524
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 524
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 524
   SecuritiesData <SctiesData> [0..*]  524
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 525
     Amount <Amt> [0..1] Amount C1, C13 525
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 525
5.4.2.18.17.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 492 March 2026
```

## File page 493

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  494
     CodeOrProprietary <CdOrPrtry> [1..1]  494
{Or       Code <Cd> [1..1] CodeSet 494
Or}       Proprietary <Prtry> [1..1] Text 494
     Issuer <Issr> [0..1] Text 494
   Number <Nb> [0..1] Text 495
   RelatedDate <RltdDt> [0..1]  495
     Type <Tp> [1..1]  495
{Or       Code <Cd> [1..1] CodeSet 495
Or}       Proprietary <Prtry> [1..1] Text 495
     Date <Dt> [1..1] Date 495
   LineDetails <LineDtls> [0..*]  496
     Identification <Id> [1..*]  496
       Type <Tp> [0..1]  497
         CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or           Code <Cd> [1..1] CodeSet 497
Or}           Proprietary <Prtry> [1..1] Text 497
         Issuer <Issr> [0..1] Text 498
       Number <Nb> [0..1] Text 498
       RelatedDate <RltdDt> [0..1] Date 498
     Description <Desc> [0..1] Text 498
     Amount <Amt> [0..1]  C18 498
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  499
         Type <Tp> [1..1]  499
{Or           Code <Cd> [1..1] CodeSet 500
Or}           Proprietary <Prtry> [1..1] Text 500
         Amount <Amt> [1..1] Amount C2, C12 500
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  500
         Amount <Amt> [1..1] Amount C2, C12 500
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 501
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 493 March 2026
```

