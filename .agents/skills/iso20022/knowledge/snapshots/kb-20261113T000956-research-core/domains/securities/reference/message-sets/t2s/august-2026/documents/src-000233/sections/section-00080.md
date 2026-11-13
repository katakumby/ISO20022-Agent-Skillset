---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "8.4 Message Building Blocks", "8.4.1 Identification <Id>", "8.4.1.4 MessageOriginator <MsgOrgtr>"]
file_pages: [120]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 8.4.1.4 MessageOriginator <MsgOrgtr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 120 to 120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 120

```text
8.4.1.4  MessageOriginator <MsgOrgtr>
Presence: [0..1]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
8.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
8.4.2 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
Impacted by: C13 "NoAccountOwnerTransactionIdentificationRule"
TransactionIdentification <TxId> contains the following TransactionIdentifications24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 121
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 121
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 121
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 121
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 120 August 2026
```

