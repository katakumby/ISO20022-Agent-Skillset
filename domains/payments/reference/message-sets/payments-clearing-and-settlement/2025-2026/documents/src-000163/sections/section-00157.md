---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.35.2.1.4 LineDetails <LineDtls>"]
file_pages: [215]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 215 to 215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 215

```text
3.4.2.35.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  215
     Type <Tp> [0..1]  216
       CodeOrProprietary <CdOrPrtry> [1..1]  216
{Or         Code <Cd> [1..1] CodeSet 216
Or}         Proprietary <Prtry> [1..1] Text 216
       Issuer <Issr> [0..1] Text 217
     Number <Nb> [0..1] Text 217
     RelatedDate <RltdDt> [0..1] Date 217
   Description <Desc> [0..1] Text 217
   Amount <Amt> [0..1]  C27 217
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  218
       Type <Tp> [1..1]  218
{Or         Code <Cd> [1..1] CodeSet 219
Or}         Proprietary <Prtry> [1..1] Text 219
       Amount <Amt> [1..1] Amount C2, C11 219
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  219
       Amount <Amt> [1..1] Amount C2, C11 219
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 220
       Reason <Rsn> [0..1] Text 220
       AdditionalInformation <AddtlInf> [0..1] Text 220
3.4.2.35.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
215 March 2026
```

