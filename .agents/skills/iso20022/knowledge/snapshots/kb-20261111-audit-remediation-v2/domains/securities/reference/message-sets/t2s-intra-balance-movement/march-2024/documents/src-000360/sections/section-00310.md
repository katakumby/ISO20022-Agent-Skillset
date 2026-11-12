---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.7 Movements <Mvmnts>", "16.4.7.2 Movement <Mvmnt>", "16.4.7.2.2 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [375]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.7.2.2 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 375 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
16.4.7.2.2  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 497
16.4.7.2.3  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
16.4.7.2.4  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 497
16.4.7.2.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 497
16.4.7.2.6  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
16.4.7.2.7  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 497
16.4.7.2.8  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
375 March 2024
```

