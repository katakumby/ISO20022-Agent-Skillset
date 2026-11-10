---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.14 TradingCurrency <TradgCcy>"]
file_pages: [151, 152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.14 TradingCurrency <TradgCcy>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 151 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
• OtherIdentificationPresenceRule
(Rule)
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
4.4.5.4.14  TradingCurrency <TradgCcy>
Presence: [0..1]
Definition: Specifies the ISO code of the trade currency.
Impacted by: C21 ValidationByTable
Datatype: CurrencyCode on page 476
Constraints
• ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters.
4.4.5.4.15  BuySellIndicator <BuySellInd>
Presence: [1..1]
Definition: Identifies the trade leg indicator which gives the trade side (buy or sell).
Datatype: Side1Code on page 482
CodeName Name Definition
BUYI Buy Order is buy driven.
SELL Sell Order is sell driven.
TWOS TwoSided Indicates that the side refers to both
buys and sells.
BUMI BuyMinus A round-lot market order to buy minus is
an order to buy a stated amount of a
stock provided that its price is:
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 151
```

## File page 152

```text
CodeName Name Definition
- not higher than the last sale if the last
sale was a minus or zero minus tick and
- not higher than the last sale minus the
minimum fractional change in the stock if
the last sale was a plus or zero plus tick.
A limit price order to buy minus also
states the highest price at which it can
be executed.
SEPL SellPlus A round-lot market order to sell plus is
an order to sell a stated amount of a
stock provided that its price is:
- not lower than the last sale if the last
sale was a plus or zero plus tick and
- not lower than the last sale minus the
minimum fractional change in the stock if
the last sale was a minus or zero minus
tick.
A limit-price order to sell plus also states
the lowest price at which it can be
executed.
SESH SellShort An order to sell a security that the seller
does not own; a sale effected by
delivering a security borrowed by, or for
the account of, the seller. Can only be
executed on a plus or zero plus tick.
SSEX SellShortExempt Short sale exempt from short-sale rules.
CROS Cross Identifies an order for which a broker
wishes to take the other side and cross
with the client.
CRSH CrossShort Identifies a type of order for which a
broker wants to cross with the client in
the case a client wants to establish a
short position, and sends a Sell Short
order to the broker. Many exchanges
have tick rules needing to be enforced,
and the order getting converted from Sell
Short to Cross (instead of Cross Short)
could result in an illegal short sell.
CSHE CrossShortExempt Identifies a type of order for which a
broker wants to cross with the client in
the case a client wants to establish a
short position and is exempt from the
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 152
```

