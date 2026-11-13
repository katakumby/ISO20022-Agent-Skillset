---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.1 ReferredDocumentInformation <RfrdDocInf>"]
file_pages: [211, 212]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.1 ReferredDocumentInformation <RfrdDocInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 211 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 211

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Garnishee <Grnshee> [0..1] ± 240
     GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 241
     ReferenceNumber <RefNb> [0..1] Text 242
     Date <Dt> [0..1] Date 243
     RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 243
     FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 243
     EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 243
   SecuritiesData <SctiesData> [0..*]  243
     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 244
     Amount <Amt> [0..1] Amount C1, C10 244
   AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 244
3.4.2.35.2.1  ReferredDocumentInformation <RfrdDocInf>
Presence: [0..*]
Definition: Provides the identification and the content of the referred document.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
211 March 2026
```

## File page 212

```text
ReferredDocumentInformation <RfrdDocInf> contains the following
ReferredDocumentInformation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  213
     CodeOrProprietary <CdOrPrtry> [1..1]  213
{Or       Code <Cd> [1..1] CodeSet 213
Or}       Proprietary <Prtry> [1..1] Text 213
     Issuer <Issr> [0..1] Text 213
   Number <Nb> [0..1] Text 214
   RelatedDate <RltdDt> [0..1]  214
     Type <Tp> [1..1]  214
{Or       Code <Cd> [1..1] CodeSet 214
Or}       Proprietary <Prtry> [1..1] Text 214
     Date <Dt> [1..1] Date 214
   LineDetails <LineDtls> [0..*]  215
     Identification <Id> [1..*]  215
       Type <Tp> [0..1]  216
         CodeOrProprietary <CdOrPrtry> [1..1]  216
{Or           Code <Cd> [1..1] CodeSet 216
Or}           Proprietary <Prtry> [1..1] Text 216
         Issuer <Issr> [0..1] Text 217
       Number <Nb> [0..1] Text 217
       RelatedDate <RltdDt> [0..1] Date 217
     Description <Desc> [0..1] Text 217
     Amount <Amt> [0..1]  C27 217
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  218
         Type <Tp> [1..1]  218
{Or           Code <Cd> [1..1] CodeSet 219
Or}           Proprietary <Prtry> [1..1] Text 219
         Amount <Amt> [1..1] Amount C2, C11 219
       AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  219
         Amount <Amt> [1..1] Amount C2, C11 219
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 220
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
212 March 2026
```

