---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "7.4 Message Building Blocks", "7.4.1 Identification <Id>", "7.4.1.5 MessageRecipient <MsgRcpt>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 7.4.1.5 MessageRecipient <MsgRcpt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
7.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 417 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 418
   LEI <LEI> [0..1] IdentifierSet 418
7.4.2 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
TransactionIdentification <TxId> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 121
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 121
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 121
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 122
   PoolIdentification <PoolId> [0..1] Text 122
7.4.2.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 497
7.4.2.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
7.4.2.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
121 March 2024
```

