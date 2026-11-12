---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.4 SecondaryClientOrderIdentification <ScndryClntOrdrId>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.4 SecondaryClientOrderIdentification <ScndryClntOrdrId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
3.4.4.4  SecondaryClientOrderIdentification <ScndryClntOrdrId>
Presence: [0..*]
Definition: Assigned by the party that originates the order. Can be used to provide the
ClientOrderIdentification used by an exchange or executing system.
Datatype: "Max35Text" on page 669
3.4.4.5  ListIdentification <ListId>
Presence: [0..*]
Definition: Unique identifier for a list, as assigned by the trading party. The identifier must be unique
within a single trading day.
Datatype: "Max35Text" on page 669
3.4.4.6  Side <Sd>
Presence: [1..1]
Definition: Coded list to specify the side of the order.
Datatype: "Side3Code" on page 650
CodeName Name Definition
BUYI Buy Order is buy driven.
SELL Sell Order is sell driven.
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
UNDI Undisclosed The side of the indication of interest is
not disclosed.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 50 February 2025
```

