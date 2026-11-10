---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [795, 796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 795 to 796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 795

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 824
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 825
     ReferenceNumber <RefNb> [0..1] Text 826
     Date <Dt> [0..1] Date 827
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 827
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 827
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 827
   SecuritiesData <SctiesData> [0..*]  827
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 828
     Amount <Amt> [0..1] Amount C1, C11 828
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 828
6.4.2.47.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
795 March 2026
```

## File page 796

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  797
     CodeOrProprietary <CdOrPrtry> [1..1]  797
{Or       Code <Cd> [1..1] CodeSet 797
Or}       Proprietary <Prtry> [1..1] Text 797
     Issuer <Issr> [0..1] Text 797
   Number <Nb> [0..1] Text 798
   RelatedDate <RltdDt> [0..1]  798
     Type <Tp> [1..1]  798
{Or       Code <Cd> [1..1] CodeSet 798
Or}       Proprietary <Prtry> [1..1] Text 798
     Date <Dt> [1..1] Date 798
   LineDetails <LineDtls> [0..*]  799
     Identification <Id> [1..*]  799
       Type <Tp> [0..1]  800
         CodeOrProprietary <CdOrPrtry> [1..1]  800
{Or           Code <Cd> [1..1] CodeSet 800
Or}           Proprietary <Prtry> [1..1] Text 800
         Issuer <Issr> [0..1] Text 801
       Number <Nb> [0..1] Text 801
       RelatedDate <RltdDt> [0..1] Date 801
     Description <Desc> [0..1] Text 801
     Amount <Amt> [0..1]  C39 801
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  802
         Type <Tp> [1..1]  802
{Or           Code <Cd> [1..1] CodeSet 803
Or}           Proprietary <Prtry> [1..1] Text 803
         Amount <Amt> [1..1] Amount C2, C12 803
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  803
         Amount <Amt> [1..1] Amount C2, C12 803
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 804
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
796 March 2026
```

