---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.3.7.12.11.2.1.4 LineDetails <LineDtls>"]
file_pages: [227]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.1.4 LineDetails <LineDtls>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 227 to 227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
3.4.3.7.12.11.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  227
     Type <Tp> [0..1]  228
       CodeOrProprietary <CdOrPrtry> [1..1]  228
{Or         Code <Cd> [1..1] CodeSet 228
Or}         Proprietary <Prtry> [1..1] Text 228
       Issuer <Issr> [0..1] Text 229
     Number <Nb> [0..1] Text 229
     RelatedDate <RltdDt> [0..1] Date 229
   Description <Desc> [0..1] Text 229
   Amount <Amt> [0..1]  C24 229
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  230
       Type <Tp> [1..1]  230
{Or         Code <Cd> [1..1] CodeSet 231
Or}         Proprietary <Prtry> [1..1] Text 231
       Amount <Amt> [1..1] Amount C2, C8 231
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  231
       Amount <Amt> [1..1] Amount C2, C8 231
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 232
       Reason <Rsn> [0..1] Text 232
       AdditionalInformation <AddtlInf> [0..1] Text 232
3.4.3.7.12.11.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 227 March 2026
```

