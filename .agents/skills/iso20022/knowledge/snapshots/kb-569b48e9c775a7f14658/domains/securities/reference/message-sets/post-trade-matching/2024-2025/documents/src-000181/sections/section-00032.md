---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.7 Payment <Pmt>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.7 Payment <Pmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
CodeName Name Definition
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
LEND Lend Order is to lend securities.
BORW Borrow Order is to borrow securities.
OPEX OptionExercise Exercise of an option contract.
3.4.4.7  Payment <Pmt>
Presence: [0..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 623
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 51 February 2025
```

