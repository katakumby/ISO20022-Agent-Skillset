---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.4 Message Building Blocks", "10.4.5 RequestDetails <ReqDtls>", "10.4.5.1 Reference <Ref>"]
file_pages: [159]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.4.5.1 Reference <Ref>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 159 to 159.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 159

```text
Constraints
• ModificationRequestPresenceRule
At least one modification request type element must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the receiver.
10.4.5.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the intra-balance modification is requested.
Reference <Ref> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 159
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 159
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 159
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 159
   PoolIdentification <PoolId> [0..1] Text 160
10.4.5.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
10.4.5.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
10.4.5.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
10.4.5.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 159 August 2026
```

