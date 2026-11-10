---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "12.4 Message Building Blocks", "12.4.1 Identification <Id>", "12.4.1.5 MessageRecipient <MsgRcpt>"]
file_pages: [204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 12.4.1.5 MessageRecipient <MsgRcpt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 204 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 204

```text
12.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
12.4.2 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
TransactionIdentification <TxId> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 204
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 204
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 204
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 205
   PoolIdentification <PoolId> [0..1] Text 205
12.4.2.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
12.4.2.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
12.4.2.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 204 August 2026
```

