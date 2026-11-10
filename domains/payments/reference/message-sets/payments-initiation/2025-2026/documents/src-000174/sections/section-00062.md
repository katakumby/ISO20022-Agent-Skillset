---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [95, 96]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 95 to 96.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 95

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 124
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 125
     ReferenceNumber <RefNb> [0..1] Text 126
     Date <Dt> [0..1] Date 127
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C19 127
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 127
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 127
   SecuritiesData <SctiesData> [0..*]  127
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 128
     Amount <Amt> [0..1] Amount C1, C20 128
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 128
2.4.2.19.26.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 95 March 2026
```

## File page 96

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  97
     CodeOrProprietary <CdOrPrtry> [1..1]  97
{Or       Code <Cd> [1..1] CodeSet 97
Or}       Proprietary <Prtry> [1..1] Text 97
     Issuer <Issr> [0..1] Text 97
   Number <Nb> [0..1] Text 98
   RelatedDate <RltdDt> [0..1]  98
     Type <Tp> [1..1]  98
{Or       Code <Cd> [1..1] CodeSet 98
Or}       Proprietary <Prtry> [1..1] Text 98
     Date <Dt> [1..1] Date 98
   LineDetails <LineDtls> [0..*]  99
     Identification <Id> [1..*]  99
       Type <Tp> [0..1]  100
         CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or           Code <Cd> [1..1] CodeSet 100
Or}           Proprietary <Prtry> [1..1] Text 100
         Issuer <Issr> [0..1] Text 101
       Number <Nb> [0..1] Text 101
       RelatedDate <RltdDt> [0..1] Date 101
     Description <Desc> [0..1] Text 101
     Amount <Amt> [0..1]  C33 101
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  102
         Type <Tp> [1..1]  102
{Or           Code <Cd> [1..1] CodeSet 103
Or}           Proprietary <Prtry> [1..1] Text 103
         Amount <Amt> [1..1] Amount C2, C19 103
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  103
         Amount <Amt> [1..1] Amount C2, C19 103
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 104
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 96 March 2026
```

