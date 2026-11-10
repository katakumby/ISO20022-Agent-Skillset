---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.4 Message Building Blocks", "13.4.1 Identification <Id>", "13.4.1.4 MessageOriginator <MsgOrgtr>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.4.1.4 MessageOriginator <MsgOrgtr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
13.4.1.4  MessageOriginator <MsgOrgtr>
Presence: [0..1]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
13.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
13.4.2 RequestReference <ReqRef>
Presence: [1..1]
Definition: Reference of the original intra-balance movement cancellation request.
Datatype: "Max35Text" on page 3328
13.4.3 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
TransactionIdentification <TxId> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 222
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 222
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 222
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 222
   PoolIdentification <PoolId> [0..1] Text 222
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 221 August 2026
```

