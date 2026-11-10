---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.11 RemittanceInformation <RmtInf>", "2.4.3.18.11.2 Structured <Strd>", "2.4.3.18.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "2.4.3.18.11.2.1.4 LineDetails <LineDtls>"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.11.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
2.4.3.18.11.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  87
     Type <Tp> [0..1]  88
       CodeOrProprietary <CdOrPrtry> [1..1]  88
{Or         Code <Cd> [1..1] CodeSet 88
Or}         Proprietary <Prtry> [1..1] Text 88
       Issuer <Issr> [0..1] Text 89
     Number <Nb> [0..1] Text 89
     RelatedDate <RltdDt> [0..1] Date 89
   Description <Desc> [0..1] Text 89
   Amount <Amt> [0..1]  C23 89
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  90
       Type <Tp> [1..1]  90
{Or         Code <Cd> [1..1] CodeSet 91
Or}         Proprietary <Prtry> [1..1] Text 91
       Amount <Amt> [1..1] Amount C2, C8 91
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  91
       Amount <Amt> [1..1] Amount C2, C8 91
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
       Reason <Rsn> [0..1] Text 92
       AdditionalInformation <AddtlInf> [0..1] Text 92
2.4.3.18.11.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
87 March 2026
```

