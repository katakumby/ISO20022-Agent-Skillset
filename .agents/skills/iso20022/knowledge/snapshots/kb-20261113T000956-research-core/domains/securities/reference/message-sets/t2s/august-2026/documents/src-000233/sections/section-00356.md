---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.7 RequestDetails <ReqDtls>", "19.4.4.1.5.7.1 Reference <Ref>"]
file_pages: [462]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.7.1 Reference <Ref>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 462 to 462.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 462

```text
Constraints
• ModificationRequestPresenceRule
At least one modification request type element must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the receiver.
19.4.4.1.5.7.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the intra-balance modification is requested.
Reference <Ref> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 462
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 462
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 462
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 462
   PoolIdentification <PoolId> [0..1] Text 463
19.4.4.1.5.7.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
19.4.4.1.5.7.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
19.4.4.1.5.7.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
19.4.4.1.5.7.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 462 August 2026
```

