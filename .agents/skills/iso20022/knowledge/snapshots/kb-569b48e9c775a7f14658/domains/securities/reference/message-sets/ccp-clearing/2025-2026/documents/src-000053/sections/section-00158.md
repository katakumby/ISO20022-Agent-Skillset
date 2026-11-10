---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.10 SecuritiesMovementType <SctiesMvmntTp>"]
file_pages: [209]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.10 SecuritiesMovementType <SctiesMvmntTp>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 209 to 209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 209

```text
5.4.5.10  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Indicates the securities movement direction, that is, whether this is a delivery or return.
Datatype: ReceiveDelivery1Code on page 481
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
5.4.5.11  Depository <Dpstry>
Presence: [1..1]
Definition: Place at which a trade settles.
Depository <Dpstry> contains one of the following elements (see PartyIdentification255Choice on
page 454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 454
Or   NameAndAddress <NmAndAdr> [1..1] ± 454
Or}   Country <Ctry> [1..1] CodeSet   'C5 454
5.4.5.12  TradingCapacity <TradgCpcty>
Presence: [0..1]
Definition: Identifies the trading capacity of the seller.
Datatype: TradingCapacity5Code on page 486
CodeName Name Definition
PRIN Principal Trading as Principal.
RISP RisklessPrincipal Trading as a riskless principal, ie, the
order to buy(sell) has been
simultaneously offset by an order to sell
(buy) with another party.
AGEN Agent Trading as Agent on behalf of a
customer.
5.4.5.13  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Place at which the security is traded.
Impacted by: C11 MarketTypeAndIdentificationRule
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 209
```

