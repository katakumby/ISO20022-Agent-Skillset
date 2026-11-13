---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.16 TradeQuantity <TradQty>"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.16 TradeQuantity <TradQty>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
CodeName Name Definition
UNDI Undisclosed The side of the indication of interest is
not disclosed.
4.4.5.4.16  TradeQuantity <TradQty>
Presence: [1..1]
Definition: Identifies the quantity of the trade leg.
TradeQuantity <TradQty> contains one of the following elements (see
FinancialInstrumentQuantity1Choice on page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
4.4.5.4.17  DealPrice <DealPric>
Presence: [1..1]
Definition: Specifies the price of the traded financial instrument.
DealPrice <DealPric> contains the following elements (see Price14 on page 462 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 463
   Type <Tp> [0..1] CodeSet 463
4.4.5.4.18  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest that has accumulated on a bond since the last interest payment up to, but not
including, the settlement date.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
AmountAndDirection21 on page 377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
4.4.5.4.19  PlaceOfTrade <PlcOfTrad>
Presence: [1..1]
Definition: Place at which the security is traded.
Impacted by: C15 MarketTypeAndIdentificationRule
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 153
```

