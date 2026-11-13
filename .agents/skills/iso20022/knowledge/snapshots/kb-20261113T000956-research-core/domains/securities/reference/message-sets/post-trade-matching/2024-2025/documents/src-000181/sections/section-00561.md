---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.72 SettlingCapacity1Code"]
file_pages: [650, 651]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.72 SettlingCapacity1Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 650 to 651.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 650

```text
CodeName Name Definition
TBAC TBAClosing Relates to a To Be Announced (TBA)
closing trade.
TRAD Trade Relates to the settlement of a trade.
TRPO TripartyRepo Relates to a triparty repurchase
agreement.
TRVO TripartyReverseRepo Relates to a triparty reverse repurchase
agreement.
TURN Turnaround Relates to a turnaround: the same
security is bought and sold to settle the
same day, to or from different brokers.
GUAR GuaranteedClose Trade which is guaranteed to be
finalized.
OFIT OfferingIssuingTrade Offering issue trade.
7.2.2.72  SettlingCapacity1Code
Definition: Specifies the role of the party in the settlement of the transaction.
Type: CodeSet
CodeName Name Definition
CUST SettlingCustodian Settlement party is a custodian. It
receives/delivers the securities and
carries out custodial duties.
SAGE SettlingAgent Settlement party is trading and settling
transactions in financial instruments on
behalf of its client(s).
SPRI SettlingPrincipal Settlement party is settling its own
trades.
7.2.2.73  Side3Code
Definition: Side taken by a party on an order.
Type: CodeSet
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 650 February 2025
```

## File page 651

```text
CodeName Name Definition
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 651 February 2025
```

