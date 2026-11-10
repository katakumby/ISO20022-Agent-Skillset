---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "3.4 Message Building Blocks", "3.4.2 TransactionIdentification <TxId>", "3.4.2.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [38]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 3.4.2.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 38 to 38.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 38

```text
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
3.4.2.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 497
3.4.2.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
3.4.2.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 497
3.4.2.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 497
3.4.3 ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus67Choice" on page 456 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rejected <Rjctd> [1..1] ± 456
Or   Repair <Rpr> [1..1] ± 457
Or   Cancelled <Canc> [1..1] ± 457
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 457
Or}   Proprietary <Prtry> [1..1] ± 457
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
38 March 2024
```

