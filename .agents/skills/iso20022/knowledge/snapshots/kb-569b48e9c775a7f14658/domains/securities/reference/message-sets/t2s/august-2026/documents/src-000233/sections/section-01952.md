---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.6 RequestDetails <ReqDtls>", "76.4.3.4.6.1 Reference <Ref>", "76.4.3.4.6.1.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [2672]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.6.1.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2672 to 2672.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2672

```text
Constraints
• ReferencePresenceRule
At least one reference must be present.
On Condition
    /AccountOwnerTransactionIdentification is absent
 And    /AccountServicerTransactionIdentification is absent
 And    /MarketInfrastructureTransactionIdentification is absent
 And    /ProcessorTransactionIdentification is absent
 And    /PoolIdentification is absent
Following Must be True
    /CommonIdentification Must be present
 Or    /TradeIdentification Must be present
 Or    /CounterpartyMarketInfrastructureTransactionIdentification Must be present
76.4.3.4.6.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
76.4.3.4.6.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
76.4.3.4.6.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
76.4.3.4.6.1.4  CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
76.4.3.4.6.1.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner, the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 3328
76.4.3.4.6.1.6  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2672 August 2026
```

