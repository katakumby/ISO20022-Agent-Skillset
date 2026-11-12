---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "9.4.3.11.11.2.1.4 LineDetails <LineDtls>"]
file_pages: [1116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1116 to 1116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1116

```text
9.4.3.11.11.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  1116
     Type <Tp> [0..1]  1117
       CodeOrProprietary <CdOrPrtry> [1..1]  1117
{Or         Code <Cd> [1..1] CodeSet 1117
Or}         Proprietary <Prtry> [1..1] Text 1117
       Issuer <Issr> [0..1] Text 1118
     Number <Nb> [0..1] Text 1118
     RelatedDate <RltdDt> [0..1] Date 1118
   Description <Desc> [0..1] Text 1118
   Amount <Amt> [0..1]  C18 1118
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1119
       Type <Tp> [1..1]  1119
{Or         Code <Cd> [1..1] CodeSet 1120
Or}         Proprietary <Prtry> [1..1] Text 1120
       Amount <Amt> [1..1] Amount C2, C8 1120
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  1120
       Amount <Amt> [1..1] Amount C2, C8 1120
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1121
       Reason <Rsn> [0..1] Text 1121
       AdditionalInformation <AddtlInf> [0..1] Text 1121
9.4.3.11.11.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1116 March 2026
```

