---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.5 FinancialInstrumentDetails <FinInstrmDtls>", "8.4.8.5.7 Transaction <Tx>", "8.4.8.5.7.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.5.7.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
8.4.8.5.7.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
8.4.8.5.7.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
8.4.8.5.7.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
8.4.8.5.7.4  CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
8.4.8.5.7.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner, the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
8.4.8.5.7.6  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
8.4.8.5.7.7  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 255 March 2026
```

