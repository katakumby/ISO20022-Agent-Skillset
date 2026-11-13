---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.5 OrderIdentification <OrdrId>"]
file_pages: [101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.5 OrderIdentification <OrdrId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 101 to 101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 101

```text
Datatype: UTIIdentifier on page 490
3.4.6.5  OrderIdentification <OrdrId>
Presence: [0..1]
Definition: Identifies the order sent by the final investor to an intermediary in order to initiate a trade in
the former's name. This identification is then matched with the equivalent trade by the clearing.
Datatype: Max35Text on page 493
3.4.6.6  AllocationIdentification <AllcnId>
Presence: [0..1]
Definition: Identifies the portion of assets within a determined trade that shall be allocated to different
clients.
Datatype: Max35Text on page 493
3.4.6.7  Status <Sts>
Presence: [0..1]
Definition: Provides the status of the trade leg.
Datatype: Status5Code on page 484
CodeName Name Definition
REJT Rejected Instruction has been rejected.
PACK Accepted Instruction has been accepted and is
validated for further processing.
PDNG Pending Instruction is pending.
3.4.6.8  TradeDate <TradDt>
Presence: [1..1]
Definition: Provides the date or date and time of trade transaction.
TradeDate <TradDt> contains one of the following elements (see DateAndDateTime2Choice on
page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
3.4.6.9  TransactionDateTime <TxDtTm>
Presence: [0..1]
Definition: Date and time used to determine the price applicable to a trade. If the trade is registered
"after market" hours, the trading price will the price of the day but the actual trade date will be the next
working day.
Datatype: ISODateTime on page 487
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 101
```

