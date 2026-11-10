---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.4 Message Building Blocks", "11.4.6 RequestDetails <ReqDtls>", "11.4.6.1 Reference <Ref>"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.4.6.1 Reference <Ref>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
Constraints
• ModificationRequestPresenceRule
At least one modification request type element must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the receiver.
11.4.6.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the intra-balance modification is requested.
Reference <Ref> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 184
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 184
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 184
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 184
   PoolIdentification <PoolId> [0..1] Text 185
11.4.6.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
11.4.6.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
11.4.6.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
11.4.6.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 184 August 2026
```

