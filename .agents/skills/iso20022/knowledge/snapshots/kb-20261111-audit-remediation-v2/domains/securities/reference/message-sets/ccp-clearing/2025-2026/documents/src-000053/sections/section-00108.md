---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.3 TradeLegIdentification <TradLegId>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.3 TradeLegIdentification <TradLegId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
DeliveryAccount <DlvryAcct> contains the following elements (see SecuritiesAccount19 on page 375
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
4.4.5.4.3  TradeLegIdentification <TradLegId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction (that is the trade leg) as known by the
instructing party.
Datatype: Max35Text on page 493
4.4.5.4.4  TradeIdentification <TradId>
Presence: [0..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: Max35Text on page 493
4.4.5.4.5  TradeExecutionIdentification <TradExctnId>
Presence: [0..1]
Definition: Unique reference assigned by the trading venue when the trade is executed.
Datatype: Max35Text on page 493
4.4.5.4.6  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: UTIIdentifier on page 490
4.4.5.4.7  OrderIdentification <OrdrId>
Presence: [0..1]
Definition: Identifies the order sent by the final investor to an intermediary in order to initiate a trade in
the former's name. This identification is then matched with the equivalent trade by the clearing.
Datatype: Max35Text on page 493
4.4.5.4.8  AllocationIdentification <AllcnId>
Presence: [0..1]
Definition: Identifies the portion of assets within a determined trade that shall be allocated to different
clients.
Datatype: Max35Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 147
```

