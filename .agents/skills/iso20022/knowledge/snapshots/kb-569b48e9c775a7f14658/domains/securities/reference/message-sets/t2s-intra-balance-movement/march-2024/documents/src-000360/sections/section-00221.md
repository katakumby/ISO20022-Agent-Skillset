---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>", "12.4.4.1.5 Modification <Mod>", "12.4.4.1.5.7 RequestDetails <ReqDtls>", "12.4.4.1.5.7.1 Reference <Ref>"]
file_pages: [271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1.5.7.1 Reference <Ref>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 271 to 271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 271

```text
Constraints
• ModificationRequestPresenceRule
At least one modification request type element must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the receiver.
12.4.4.1.5.7.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the intra-balance modification is requested.
Reference <Ref> contains the following References14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 271
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 271
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 271
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 271
   PoolIdentification <PoolId> [0..1] Text 272
12.4.4.1.5.7.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 497
12.4.4.1.5.7.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
12.4.4.1.5.7.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 497
12.4.4.1.5.7.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 497
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
271 March 2024
```

