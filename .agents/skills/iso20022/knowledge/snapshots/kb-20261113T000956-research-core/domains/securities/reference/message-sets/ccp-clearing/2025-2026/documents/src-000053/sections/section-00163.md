---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.9 SettlementDate <SttlmDt>", "5.4.5.16.9.2 DateCode <DtCd>", "5.4.5.16.9.2.1 Code <Cd>"]
file_pages: [216, 217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.9.2.1 Code <Cd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 216 to 217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 216
Or}   Proprietary <Prtry> [1..1] ± 216
5.4.5.16.9.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
5.4.5.16.9.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
5.4.5.16.10  TradingCurrency <TradgCcy>
Presence: [0..1]
Definition: Specifies the ISO code of the trade currency.
Impacted by: C18 ValidationByTable
Datatype: CurrencyCode on page 476
Constraints
• ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters.
5.4.5.16.11  BuySellIndicator <BuySellInd>
Presence: [1..1]
Definition: Identifies the trade leg indicator which gives the trade side (buy or sell).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 216
```

## File page 217

```text
Datatype: Side1Code on page 482
CodeName Name Definition
BUYI Buy Order is buy driven.
SELL Sell Order is sell driven.
TWOS TwoSided Indicates that the side refers to both
buys and sells.
BUMI BuyMinus A round-lot market order to buy minus is
an order to buy a stated amount of a
stock provided that its price is:
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 217
```

