---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.2 Structured <Strd>", "4.4.3.27.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.27.11.2.1.4 LineDetails <LineDtls>"]
file_pages: [403]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 403 to 403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 403

```text
4.4.3.27.11.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  403
     Type <Tp> [0..1]  404
       CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or         Code <Cd> [1..1] CodeSet 404
Or}         Proprietary <Prtry> [1..1] Text 404
       Issuer <Issr> [0..1] Text 405
     Number <Nb> [0..1] Text 405
     RelatedDate <RltdDt> [0..1] Date 405
   Description <Desc> [0..1] Text 405
   Amount <Amt> [0..1]  C59 405
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
       Type <Tp> [1..1]  406
{Or         Code <Cd> [1..1] CodeSet 407
Or}         Proprietary <Prtry> [1..1] Text 407
       Amount <Amt> [1..1] Amount C2, C12 407
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  407
       Amount <Amt> [1..1] Amount C2, C12 407
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
       Reason <Rsn> [0..1] Text 408
       AdditionalInformation <AddtlInf> [0..1] Text 408
4.4.3.27.11.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
403 March 2026
```

