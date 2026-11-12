---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [496, 497]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 496 to 497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 496

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 525
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 526
     ReferenceNumber <RefNb> [0..1] Text 527
     Date <Dt> [0..1] Date 528
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 528
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 528
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 528
   SecuritiesData <SctiesData> [0..*]  528
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 529
     Amount <Amt> [0..1] Amount C1, C11 529
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 529
4.4.3.27.23.30.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
496 March 2026
```

## File page 497

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  498
     CodeOrProprietary <CdOrPrtry> [1..1]  498
{Or       Code <Cd> [1..1] CodeSet 498
Or}       Proprietary <Prtry> [1..1] Text 498
     Issuer <Issr> [0..1] Text 498
   Number <Nb> [0..1] Text 499
   RelatedDate <RltdDt> [0..1]  499
     Type <Tp> [1..1]  499
{Or       Code <Cd> [1..1] CodeSet 499
Or}       Proprietary <Prtry> [1..1] Text 499
     Date <Dt> [1..1] Date 499
   LineDetails <LineDtls> [0..*]  500
     Identification <Id> [1..*]  500
       Type <Tp> [0..1]  501
         CodeOrProprietary <CdOrPrtry> [1..1]  501
{Or           Code <Cd> [1..1] CodeSet 501
Or}           Proprietary <Prtry> [1..1] Text 501
         Issuer <Issr> [0..1] Text 502
       Number <Nb> [0..1] Text 502
       RelatedDate <RltdDt> [0..1] Date 502
     Description <Desc> [0..1] Text 502
     Amount <Amt> [0..1]  C59 502
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  503
         Type <Tp> [1..1]  503
{Or           Code <Cd> [1..1] CodeSet 504
Or}           Proprietary <Prtry> [1..1] Text 504
         Amount <Amt> [1..1] Amount C2, C12 504
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  504
         Amount <Amt> [1..1] Amount C2, C12 504
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 505
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
497 March 2026
```

