---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPostTradeEquity1Code"]
code_set: "ExternalPostTradeEquity1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPostTradeEquity1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPostTradeEquity1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Information related to the post trade of equities.
*`ALGO`-Flag for transactions executed as a result of an investment firm engaging in  algorithmic trading
*`AMND`-Flag when a previously published transaction is amended.
*`BENC`-Flag for transactions executed in reference to a price that is calculated over 
multiple time instances according to a given benchmark.
*`CANC`-Flag when a previously published transaction is cancelled.
*`CONT`-Flag for transactions that are contingent on the purchase, sale, creation or redemption of a derivative contract or other financial instrument where all the components of the trade are meant to be executed as a single lot.
*`OILQ`-Flag for transactions in an illiquid instrument traded at a system-set percentage of a reference price.
*`NLIQ`-Flag for transactions made within the current volume weighted spread reflected on the order book or the quotes of the market makers of the trading venue operating that system.
*`PRIC`-Flag for transactions executed subject to conditions other than the current market price of that financial instrument.
*`NPFT`-Flag for non-price forming transactions
*`PORT`-Flag for transactions in five or more different financial instruments where those transactions are traded at the same time by the same client.

It is used as a single lot price and that is not a ‘package transaction'.
*`LRGS`-Flag for transactions large in scale relative to normal market size, executed under a permitted post-trade deferral.
*`RFPT`-Flag for transactions which are executed under systems.
*`SDIV`-Flag for transactions where dividends accrue to the non-entitled party due to ex- or cum-dividend timing.

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
| 1 | ALGO |
| 2 | AMND |
| 3 | BENC |
| 4 | CANC |
| 5 | CONT |
| 6 | OILQ |
| 7 | NLIQ |
| 8 | PRIC |
| 9 | NPFT |
| 10 | PORT |
| 11 | LRGS |
| 12 | RFPT |
| 13 | SDIV |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
