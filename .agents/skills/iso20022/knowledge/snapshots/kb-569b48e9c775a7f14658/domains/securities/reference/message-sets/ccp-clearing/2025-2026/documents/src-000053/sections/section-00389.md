---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.26 SafekeepingPlace3Code"]
file_pages: [482]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.26 SafekeepingPlace3Code

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 482 to 482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 482

```text
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
12.2.2.26  SafekeepingPlace3Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
12.2.2.27  ShortLong1Code
Definition: Specifies whether the securities position is short or long, that is, whether the balance is a
negative or positive balance.
Type: CodeSet
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
12.2.2.28  Side1Code
Definition: Indicates the side of the quote request, from the buy-side perspective.
Type: CodeSet
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 482
```

