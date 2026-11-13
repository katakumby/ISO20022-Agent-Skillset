---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.7 AccruedInterestAmount <AcrdIntrstAmt>"]
file_pages: [208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.7 AccruedInterestAmount <AcrdIntrstAmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 208 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 208

```text
NetPositionAmount <NetPosAmt> contains the following elements (see AmountAndDirection21 on
page 377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
5.4.5.7  AccruedInterestAmount <AcrdIntrstAmt>
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
5.4.5.8  AverageDealPrice <AvrgDealPric>
Presence: [0..1]
Definition: This is the price of the trade.
AverageDealPrice <AvrgDealPric> contains the following elements (see Price14 on page 462 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 463
   Type <Tp> [0..1] CodeSet 463
5.4.5.9  NetQuantity <NetQty>
Presence: [1..1]
Definition: Identifies the quantity of the trade leg.
NetQuantity <NetQty> contains one of the following elements (see
FinancialInstrumentQuantity1Choice on page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 208
```

