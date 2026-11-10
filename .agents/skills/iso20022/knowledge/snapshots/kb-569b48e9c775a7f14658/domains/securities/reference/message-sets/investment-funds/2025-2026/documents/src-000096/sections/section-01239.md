---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.7 AmountOrUnitsOrPercentage <AmtOrUnitsOrPctg>", "41.4.4.8.7.5 HoldingsRedemptionRate <HldgsRedRate>"]
file_pages: [1742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.7.5 HoldingsRedemptionRate <HldgsRedRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1742 to 1742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1742

```text
41.4.4.8.7.5  HoldingsRedemptionRate <HldgsRedRate>
Presence: [1..1]
Definition: Portion of the investor's holdings to be redeemed.
Datatype: "PercentageRate" on page 5401
41.4.4.8.8  Rounding <Rndg>
Presence: [0..1]
Definition: Indicates the rounding direction applied to nearest unit.
Datatype: "RoundingDirection2Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
41.4.4.8.9  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the individual order.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
41.4.4.8.10  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
41.4.4.8.11  SettlementMethod <SttlmMtd>
Presence: [0..1]
Definition: Method by which the transaction is settled.
Datatype: "DeliveryReceiptType2Code" on page 5294
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1742 May 2026
```

