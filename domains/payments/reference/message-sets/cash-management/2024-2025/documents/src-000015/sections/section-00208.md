---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.6 SecuritiesTransactionReferences <SctiesTxRefs>", "5.4.2.1.3.2.1.6.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.6.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
5.4.2.1.3.2.1.6.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the securities transaction as known by the securities account
owner (or the instructing party managing the account).
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.6.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the securities transaction as known by the securities account
servicer.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.6.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a securities transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.1.6.4  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Identification of the securities transaction assigned by the processor of the instruction other
than the securities account owner, the securities account servicer and the market infrastructure.
Datatype: "Max35Text" on page 889
5.4.2.1.3.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason why the requested business information is not given.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  323
{Or     Code <Cd> [1..1] CodeSet 324
Or}     Proprietary <Prtry> [1..1] Text 324
   Description <Desc> [0..1] Text 324
5.4.2.1.3.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 323 February 2025
```

