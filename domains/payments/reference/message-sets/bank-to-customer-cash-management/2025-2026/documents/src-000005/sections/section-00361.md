---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.3 Transaction <Tx>", "3.4.2.15.18.2.26.3.2 Individual <Indv>", "3.4.2.15.18.2.26.3.2.6 SaleReferenceNumber <SaleRefNb>"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.3.2.6 SaleReferenceNumber <SaleRefNb>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
3.4.2.15.18.2.26.3.2.6  SaleReferenceNumber <SaleRefNb>
Presence: [0..1]
Definition: Unique reference of the sales as provided by the merchant.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.3.2.7  RePresentmentReason <RePresntmntRsn>
Presence: [0..1]
Definition: Reason for representment of a card transaction.
Datatype: "ExternalRePresentmentReason1Code" on page 900
3.4.2.15.18.2.26.3.2.8  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Sequential number of the card transaction, as assigned by the POI (Point of Interaction).
Usage: The sequential number is increased incrementally for each transaction.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.3.2.9  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the POI (Point Of Interaction).
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifier1" on
page 858 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionDateTime <TxDtTm> [1..1] DateTime 858
   TransactionReference <TxRef> [1..1] Text 858
3.4.2.15.18.2.26.3.2.10  Product <Pdct>
Presence: [0..1]
Definition: Product purchased with the transaction.
Product <Pdct> contains the following Product2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProductCode <PdctCd> [1..1] Text 518
   UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 518
   ProductQuantity <PdctQty> [0..1] Quantity 519
   UnitPrice <UnitPric> [0..1] Amount 519
   ProductAmount <PdctAmt> [0..1] Amount 519
   TaxType <TaxTp> [0..1] Text 520
   AdditionalProductInformation <AddtlPdctInf> [0..1] Text 520
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
517 March 2026
```

