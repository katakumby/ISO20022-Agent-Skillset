---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.15 AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls>", "11.4.6.2.15.6 NetPositionPrice <NetPosPric>"]
file_pages: [365]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.15.6 NetPositionPrice <NetPosPric>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 365 to 365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 365

```text
Quantity <Qty> contains one of the following elements (see FinancialInstrumentQuantity1Choice on
page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
11.4.6.2.15.6  NetPositionPrice <NetPosPric>
Presence: [0..1]
Definition: Provides the price applied to that net position.
NetPositionPrice <NetPosPric> contains the following elements (see Price14 on page 462 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 463
   Type <Tp> [0..1] CodeSet 463
11.4.6.2.15.7  TradingCurrency <TradgCcy>
Presence: [0..1]
Definition: Specifies the ISO code of the trade currency.
Impacted by: C19 ValidationByTable
Datatype: CurrencyCode on page 476
Constraints
• ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters.
11.4.6.2.15.8  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Provides the total amount to be settled.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 365
```

