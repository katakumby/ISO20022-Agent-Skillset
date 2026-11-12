---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.15 AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls>", "11.4.6.2.15.1 RelatedSettlementObligationIdentification <RltdSttlmOblgtnId>"]
file_pages: [363]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.15.1 RelatedSettlementObligationIdentification <RltdSttlmOblgtnId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 363 to 363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls> contains the following
SettlementObligation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RelatedSettlementObligationIdentification
<RltdSttlmOblgtnId>
[0..1] Text 363
   ObligationType <OblgtnTp> [0..1]  363
{Or     Code <Cd> [1..1] CodeSet 364
Or}     Proprietary <Prtry> [1..1] ± 364
   Description <Desc> [0..1] Text 364
   TradeDate <TradDt> [0..1] Date 364
   Quantity <Qty> [1..1] ± 364
   NetPositionPrice <NetPosPric> [0..1] ± 365
   TradingCurrency <TradgCcy> [0..1] CodeSet C19 365
   SettlementAmount <SttlmAmt> [1..1] ± 365
   SettlementDate <SttlmDt> [1..1] Date 366
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 366
   Payment <Pmt> [1..1] CodeSet 366
   References <Refs> [0..1]  366
     TradeLegNotificationIdentification <TradLegNtfctnId> [0..*]  367
{Or       TradeLegNotificationIdentification
<TradLegNtfctnId>
[1..1] Text 367
Or}       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 367
     NetPositionIdentification <NetPosId> [0..1] Text 367
11.4.6.2.15.1  RelatedSettlementObligationIdentification <RltdSttlmOblgtnId>
Presence: [0..1]
Definition: Provides the identification of an existing obligation that is linked to the new obligation.
Datatype: Max35Text on page 493
11.4.6.2.15.2  ObligationType <OblgtnTp>
Presence: [0..1]
Definition: Indicates the type of the obligation.
ObligationType <OblgtnTp> contains one of the following ObligationType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 364
Or}   Proprietary <Prtry> [1..1] ± 364
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 363
```

