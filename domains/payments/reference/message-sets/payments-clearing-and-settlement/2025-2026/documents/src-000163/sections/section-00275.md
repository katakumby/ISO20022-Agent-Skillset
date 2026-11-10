---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.2 Structured <Strd>", "4.4.3.27.11.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [399, 400]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 399 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 428
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 429
     ReferenceNumber <RefNb> [0..1] Text 430
     Date <Dt> [0..1] Date 431
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 431
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 431
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 431
   SecuritiesData <SctiesData> [0..*]  431
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 432
     Amount <Amt> [0..1] Amount C1, C11 432
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 432
4.4.3.27.11.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
399 March 2026
```

## File page 400

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  401
     CodeOrProprietary <CdOrPrtry> [1..1]  401
{Or       Code <Cd> [1..1] CodeSet 401
Or}       Proprietary <Prtry> [1..1] Text 401
     Issuer <Issr> [0..1] Text 401
   Number <Nb> [0..1] Text 402
   RelatedDate <RltdDt> [0..1]  402
     Type <Tp> [1..1]  402
{Or       Code <Cd> [1..1] CodeSet 402
Or}       Proprietary <Prtry> [1..1] Text 402
     Date <Dt> [1..1] Date 402
   LineDetails <LineDtls> [0..*]  403
     Identification <Id> [1..*]  403
       Type <Tp> [0..1]  404
         CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or           Code <Cd> [1..1] CodeSet 404
Or}           Proprietary <Prtry> [1..1] Text 404
         Issuer <Issr> [0..1] Text 405
       Number <Nb> [0..1] Text 405
       RelatedDate <RltdDt> [0..1] Date 405
     Description <Desc> [0..1] Text 405
     Amount <Amt> [0..1]  C59 405
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
         Type <Tp> [1..1]  406
{Or           Code <Cd> [1..1] CodeSet 407
Or}           Proprietary <Prtry> [1..1] Text 407
         Amount <Amt> [1..1] Amount C2, C12 407
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  407
         Amount <Amt> [1..1] Amount C2, C12 407
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
400 March 2026
```

