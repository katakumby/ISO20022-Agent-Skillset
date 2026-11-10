---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.27.23.30.2.1.4 LineDetails <LineDtls>"]
file_pages: [500]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 500 to 500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 500

```text
4.4.3.27.23.30.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  500
     Type <Tp> [0..1]  501
       CodeOrProprietary <CdOrPrtry> [1..1]  501
{Or         Code <Cd> [1..1] CodeSet 501
Or}         Proprietary <Prtry> [1..1] Text 501
       Issuer <Issr> [0..1] Text 502
     Number <Nb> [0..1] Text 502
     RelatedDate <RltdDt> [0..1] Date 502
   Description <Desc> [0..1] Text 502
   Amount <Amt> [0..1]  C59 502
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  503
       Type <Tp> [1..1]  503
{Or         Code <Cd> [1..1] CodeSet 504
Or}         Proprietary <Prtry> [1..1] Text 504
       Amount <Amt> [1..1] Amount C2, C12 504
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  504
       Amount <Amt> [1..1] Amount C2, C12 504
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 505
       Reason <Rsn> [0..1] Text 505
       AdditionalInformation <AddtlInf> [0..1] Text 505
4.4.3.27.23.30.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
500 March 2026
```

