---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.12 TradeQuantity <TradQty>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.12 TradeQuantity <TradQty>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
CodeName Name Definition
uptick restriction. Used as audit trail on
exchanges.
DEFI AsDefined Indicates, in the case of a multileg
instrument,that the sides of the legs are
the same as defined at the creation of
the multileg instrument.
OPPO Opposite Indicates, in the case of a multileg
instrument,that the sides of the legs are
the opposite of their definition at the
creation of the multileg instrument.
UNDI Undisclosed The side of the indication of interest is
not disclosed.
5.4.5.16.12  TradeQuantity <TradQty>
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
5.4.5.16.13  DealPrice <DealPric>
Presence: [1..1]
Definition: Specifies the price of the traded financial instrument.
DealPrice <DealPric> contains the following elements (see Price14 on page 462 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 463
   Type <Tp> [0..1] CodeSet 463
5.4.5.16.14  GrossAmount <GrssAmt>
Presence: [0..1]
Definition: Principal amount of a trade (price multiplied by quantity).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 218
```

