---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.8.9.11.2.1.4 LineDetails <LineDtls>"]
file_pages: [358]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.1.4 LineDetails <LineDtls>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 358 to 358.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 358

```text
4.4.3.8.9.11.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  358
     Type <Tp> [0..1]  359
       CodeOrProprietary <CdOrPrtry> [1..1]  359
{Or         Code <Cd> [1..1] CodeSet 359
Or}         Proprietary <Prtry> [1..1] Text 359
       Issuer <Issr> [0..1] Text 360
     Number <Nb> [0..1] Text 360
     RelatedDate <RltdDt> [0..1] Date 360
   Description <Desc> [0..1] Text 360
   Amount <Amt> [0..1]  C24 360
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  361
       Type <Tp> [1..1]  361
{Or         Code <Cd> [1..1] CodeSet 362
Or}         Proprietary <Prtry> [1..1] Text 362
       Amount <Amt> [1..1] Amount C2, C9 362
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  362
       Amount <Amt> [1..1] Amount C2, C9 362
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 363
       Reason <Rsn> [0..1] Text 363
       AdditionalInformation <AddtlInf> [0..1] Text 363
4.4.3.8.9.11.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 358 March 2026
```

