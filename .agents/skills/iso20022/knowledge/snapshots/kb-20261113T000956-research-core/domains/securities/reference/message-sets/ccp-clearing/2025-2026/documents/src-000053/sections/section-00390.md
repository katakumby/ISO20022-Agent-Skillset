---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.29 StatementUpdateType1Code"]
file_pages: [483]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.29 StatementUpdateType1Code

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 483 to 483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 483

```text
CodeName Name Definition
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
UNDI Undisclosed The side of the indication of interest is
not disclosed.
12.2.2.29  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 483
```

