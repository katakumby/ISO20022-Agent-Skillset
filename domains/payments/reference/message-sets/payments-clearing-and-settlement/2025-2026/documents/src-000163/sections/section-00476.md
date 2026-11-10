---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.3.21.11.2.1.4 LineDetails <LineDtls>"]
file_pages: [657]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 657 to 657.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 657

```text
5.4.3.21.11.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  657
     Type <Tp> [0..1]  658
       CodeOrProprietary <CdOrPrtry> [1..1]  658
{Or         Code <Cd> [1..1] CodeSet 658
Or}         Proprietary <Prtry> [1..1] Text 658
       Issuer <Issr> [0..1] Text 659
     Number <Nb> [0..1] Text 659
     RelatedDate <RltdDt> [0..1] Date 659
   Description <Desc> [0..1] Text 659
   Amount <Amt> [0..1]  C27 659
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  660
       Type <Tp> [1..1]  660
{Or         Code <Cd> [1..1] CodeSet 661
Or}         Proprietary <Prtry> [1..1] Text 661
       Amount <Amt> [1..1] Amount C2, C11 661
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  661
       Amount <Amt> [1..1] Amount C2, C11 661
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 662
       Reason <Rsn> [0..1] Text 662
       AdditionalInformation <AddtlInf> [0..1] Text 662
5.4.3.21.11.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
657 March 2026
```

