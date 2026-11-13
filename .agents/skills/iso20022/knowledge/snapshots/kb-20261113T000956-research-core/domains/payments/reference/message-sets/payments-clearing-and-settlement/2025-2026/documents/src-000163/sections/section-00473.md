---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [653, 654]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 653 to 654.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 653

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 682
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 683
     ReferenceNumber <RefNb> [0..1] Text 684
     Date <Dt> [0..1] Date 685
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 685
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 685
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 685
   SecuritiesData <SctiesData> [0..*]  685
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 686
     Amount <Amt> [0..1] Amount C1, C10 686
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 686
5.4.3.21.11.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
653 March 2026
```

## File page 654

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  655
     CodeOrProprietary <CdOrPrtry> [1..1]  655
{Or       Code <Cd> [1..1] CodeSet 655
Or}       Proprietary <Prtry> [1..1] Text 655
     Issuer <Issr> [0..1] Text 655
   Number <Nb> [0..1] Text 656
   RelatedDate <RltdDt> [0..1]  656
     Type <Tp> [1..1]  656
{Or       Code <Cd> [1..1] CodeSet 656
Or}       Proprietary <Prtry> [1..1] Text 656
     Date <Dt> [1..1] Date 656
   LineDetails <LineDtls> [0..*]  657
     Identification <Id> [1..*]  657
       Type <Tp> [0..1]  658
         CodeOrProprietary <CdOrPrtry> [1..1]  658
{Or           Code <Cd> [1..1] CodeSet 658
Or}           Proprietary <Prtry> [1..1] Text 658
         Issuer <Issr> [0..1] Text 659
       Number <Nb> [0..1] Text 659
       RelatedDate <RltdDt> [0..1] Date 659
     Description <Desc> [0..1] Text 659
     Amount <Amt> [0..1]  C27 659
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  660
         Type <Tp> [1..1]  660
{Or           Code <Cd> [1..1] CodeSet 661
Or}           Proprietary <Prtry> [1..1] Text 661
         Amount <Amt> [1..1] Amount C2, C11 661
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  661
         Amount <Amt> [1..1] Amount C2, C11 661
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 662
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
654 March 2026
```

