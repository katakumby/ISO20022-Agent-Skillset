---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.1 PaymentIdentification <PmtId>"]
file_pages: [256]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.1 PaymentIdentification <PmtId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 256 to 256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdditionalEntryInformation <AddtlNtryInf> [0..*] Text 322
       SecuritiesTransactionReferences <SctiesTxRefs> [0..1]  322
         AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 323
         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 323
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 323
         ProcessingIdentification <PrcgId> [0..1] Text 323
Or}     BusinessError <BizErr> [1..*]  323
       Error <Err> [1..1]  323
{Or         Code <Cd> [1..1] CodeSet 324
Or}         Proprietary <Prtry> [1..1] Text 324
       Description <Desc> [0..1] Text 324
5.4.2.1.3.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: Reference to the instruction related to the payment for which information is requested.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 256 February 2025
```

