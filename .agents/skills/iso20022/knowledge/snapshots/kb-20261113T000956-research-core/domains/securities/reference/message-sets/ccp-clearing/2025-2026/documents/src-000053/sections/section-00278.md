---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.15 AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls>", "11.4.6.2.15.12 References <Refs>", "11.4.6.2.15.12.1 TradeLegNotificationIdentification <TradLegNtfctnId>"]
file_pages: [367]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.15.12.1 TradeLegNotificationIdentification <TradLegNtfctnId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 367 to 367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 367

```text
References <Refs> contains the following Reference24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeLegNotificationIdentification <TradLegNtfctnId> [0..*]  367
{Or     TradeLegNotificationIdentification <TradLegNtfctnId> [1..1] Text 367
Or}     UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 367
   NetPositionIdentification <NetPosId> [0..1] Text 367
11.4.6.2.15.12.1  TradeLegNotificationIdentification <TradLegNtfctnId>
Presence: [0..*]
Definition: Reference allocated by the central counterparty - central counterpatry trade leg reference
identification that uniquely identifies the trade.
TradeLegNotificationIdentification <TradLegNtfctnId> contains one of the following
TradeLegNotificationIdentification1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TradeLegNotificationIdentification <TradLegNtfctnId> [1..1] Text 367
Or}   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 367
11.4.6.2.15.12.1.1  TradeLegNotificationIdentification <TradLegNtfctnId>
Presence: [1..1]
Definition: Reference allocated by the central counterparty - central counterpatry trade leg reference
identification that uniquely identifies the trade.
Datatype: Max35Text on page 493
11.4.6.2.15.12.1.2  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: UTIIdentifier on page 490
11.4.6.2.15.12.2  NetPositionIdentification <NetPosId>
Presence: [0..1]
Definition: After netting, reference that is common to a net transaction to settle and all its underlying
trades.
Datatype: Max35Text on page 493
11.4.7 SettlementParties <SttlmPties>
Presence: [0..1]
Definition: Provides details about the receiving parties involved in the settlement chain.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 367
```

