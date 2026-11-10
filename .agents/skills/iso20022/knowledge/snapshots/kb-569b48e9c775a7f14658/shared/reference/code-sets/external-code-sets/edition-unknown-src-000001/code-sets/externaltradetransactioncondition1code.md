---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalTradeTransactionCondition1Code"]
code_set: "ExternalTradeTransactionCondition1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalTradeTransactionCondition1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalTradeTransactionCondition1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external Trade Transaction Condition code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`BCBL`-Board lots, not set for odd lots (UK specific).
*`BCBN`-Bad names, not set for good names (UK specific).
*`BCFD`-Form of delivery, not for foreign registration when unset (UK specific).
*`BCPD`-Place of delivery, in country of incorporation when unset (UK specific).
*`BCRO`-Result of option when set (UK specific).
*`BCRP`-Result of repo when set (UK specific).
*`BLKO`-The trade is a block trade or not, ie, whether allocation instruction will follow or not.
*`BTEX`-Trade to be executed done at best execution.
*`BTMI`-Bought minus indicator.
*`CALL`-Trade to be executed following the exercise of a call option on the security.
*`CBNS`-Trade is executed cum bonus.
*`CCPN`-Trade is executed cum coupon.
*`CDIV`-Trade is executed cum dividend.
*`CLBR`-Trade to be executed for closure of a previous position before the rollover of a position (Deferred Settlement Service).
*`CLEN`-Trade is executed clean, ie government tax must not be paid on the accrued interest on the bond.
*`CRST`-Cross trades are allowed whereby buy and sell orders are offset without recording the trade on the exchange
*`CRTS`-Trade is executed cum rights.
*`CWAR`-Trade is executed cum warrant.
*`DIOR`-Customer order where the customer gives specific instructions to the broker concerning the orders routing destination.
*`DIRT`-Trade is executed dirty, ie government tax must be paid on the accrued interest on the bond.
*`DORD`-Order is to be executed by a trading party other than the trading party to which the order is sent. In this case, the instructing party has traded with another broker which will subsequently send an advice of execution to the executing party who received the order and which is acting as clearing broker.
*`FORW`-Order is based on a forward price.
*`FRAC`-Fractional parts are allowed.
*`GTDL`-Delivery of the financial instrument on settlement date is guaranteed.
*`HIST`-Order is based on a historic price.
*`MAPR`-Trade was executed at market price.
*`MONT`-Trade to be executed for month-end settlement (Deferred Settlement Service).
*`NBFR`-Trade to be executed for a new trade position on the next month following the roll-over of a position (Deferred Settlement Service).
*`NCRS`-Cross trades, whereby buy and sell orders are offset without recording the trade on the exchange, are not allowed.
*`NEGO`-Trade for which the price is not the one quoted but an improved one, that is, the negotiated price.
*`NMPR`-Trade was executed outside of normal market conditions, for example, in the case of an iceberg order.
*`PETA`-Allows trader to explicitly request anonymity or disclosure in pre-trade market data feeds. Anonymity is relevant in markets where counterparties are regularly disclosed in order depth feeds. Disclosure is relevant when counterparties are not normally visible.
*`PUTT`-Trade to be executed following the exercise of a put option on the security.
*`SETI`-Trade is exempt from short-sale rules.
*`SPCU`-Trade is executed  with a special cum dividend, ie, buying after the ex date and getting the dividend.
*`SPEX`-Trade is executed  with a special ex dividend, ie, selling before the ex date without the coupon.
*`SPSI`-Sold plus indication.
*`SSTI`-Trade is sold short. When the seller does not have the financial instrument, the delivery is effected by borrowing the financial instrument by or for the account of the seller.
*`TEFR`-Trade executed this month following the rollover of positions.
*`TRFR`-Trade to be executed on the next month following the roll-over of positions.
*`WIBC`-Transaction is before the issue date after announcement of the auction.
*`WICD`-Transaction is after the issue date after announcement of the auction.
*`XBNS`-Trade is executed ex bonus.
*`XCPN`-Trade is executed ex coupon.
*`XDIV`-Trade is executed ex dividend.
*`XRTS`-Trade is executed ex rights.
*`XWAR`-Trade is executed ex warrant.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | BCBL |
| 2 | BCBN |
| 3 | BCFD |
| 4 | BCPD |
| 5 | BCRO |
| 6 | BCRP |
| 7 | BLKO |
| 8 | BTEX |
| 9 | BTMI |
| 10 | CALL |
| 11 | CBNS |
| 12 | CCPN |
| 13 | CDIV |
| 14 | CLBR |
| 15 | CLEN |
| 16 | CRST |
| 17 | CRTS |
| 18 | CWAR |
| 19 | DIOR |
| 20 | DIRT |
| 21 | DORD |
| 22 | FORW |
| 23 | FRAC |
| 24 | GTDL |
| 25 | HIST |
| 26 | MAPR |
| 27 | MONT |
| 28 | NBFR |
| 29 | NCRS |
| 30 | NEGO |
| 31 | NMPR |
| 32 | PETA |
| 33 | PUTT |
| 34 | SETI |
| 35 | SPCU |
| 36 | SPEX |
| 37 | SPSI |
| 38 | SSTI |
| 39 | TEFR |
| 40 | TRFR |
| 41 | WIBC |
| 42 | WICD |
| 43 | XBNS |
| 44 | XCPN |
| 45 | XDIV |
| 46 | XRTS |
| 47 | XWAR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
