---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05"]
file_pages: [3487, 3488]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53 setr.013.001.05 SwitchOrderV05

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3487 to 3488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3487

```text
53 setr.013.001.05
SwitchOrderV05
53.1 MessageDefinition Functionality
Scope
The SwitchOrder message is sent by an instructing party, for example, an investment manager or its
authorised representative, to the executing party, for example, a transfer agent, to instruct a switch
transaction from a financial instrument or multiple financial instruments to a different specified financial
instrument or instruments for a specified amount/quantity.
Usage
The SwitchOrder message is used to either:
- instruct one switch transaction comprising one or more redemption legs and one or more subscription
legs, that is, a single switch transaction that can be a one to one, many to one, many to many or one to
many switch transaction, or,
- instruct one or many switch transactions each comprising one redemption leg and one subscription
leg, that is, multiple simple switch transactions.
The SwitchOrder message may be used to either:
- instruct a switch transaction for one investment account, or,
- instruct a switch transaction for separate accounts at the redemption and subscription leg levels.
The message caters for a switch from one financial instrument to another financial instrument (within
the same fund family), many to one, many to many and one to many.
The message caters for switch transactions that result in an additional cash payment from the investor
or a transaction that results in a net payment to the investor. Not all institutions or funds permit this type
of switch and acceptance is therefore not automatic.
There is no limitation on the number of switch legs in a switch message. The number allowed is defined
by the fund prospectus or by the service level agreement (SLA) in place between the two parties.
However, if the SwitchOrderDetails sequence is present more than once, then the
RedemptionLegDetails and SubscriptionLegDetails sequences may only be present once.
If SwitchOrderDetails\InvestmentAccount is used, then the InvestmentAccountDetails sequences in
SubscriptionLegDetails and RedemptionLegDetails are not allowed. This functionality is to be used by
institutions that set up two accounts per investor, rather than one investment account.
There is no switch driver type in the message to indicate whether the switch is buy or sell driven. A
driver is not needed since it is possible to indicate the total subscription amount or the total redemption
amount. Only one of these two amounts should be used.
The subscription quantity can be expressed in one of the following ways:
- Amount: the monetary value (either GROSS or NET) of the financial instrument to be subscribed to,
for example, the subscription of EUR 1,000 of financial instrument ISIN LU1234567890 or
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3487 May 2026
```

## File page 3488

```text
- Unit: the number of units of the financial instrument to be subscribed to, for example, the subscription
of 10 units of financial instrument ISIN LU1234567890 or
- Percentage of the total redemption amount: when the switch transaction is redemption driven, it is the
part of the redemption amount that must be switched to a specific financial instrument, for example, the
subscription quantity of financial instrument ISIN LU1234567890 represents 50% of the redemption
amount of the financial instrument ISIN LU4444444444.
The redemption quantity can be expressed in one of the following ways:
- Amount: the monetary value (either GROSS or NET) of the financial instrument to be redeemed, for
example, the redemption of EUR 1,000 of financial instrument ISIN LU1234567890, or
- Unit: the number of units of financial instrument to be redeemed, for example, the redemption of 10
units of financial instrument ISIN LU1234567890, or
- Rate: the part of the portfolio to be redeemed, for example, the redemption of 10% of the holdings in
financial instrument ISIN LU1234567890, or
- Percentage of the total subscription amount: when the switch transaction is subscription driven, it is
the part of the subscription amount that must be the result of the redemption of a specific financial
instrument, for example, the redemption quantity in financial instrument ABC represents 50% of the
subscription amount of the financial instrument ISIN LU4444444444.
Outline
The SwitchOrderV05 MessageDefinition is composed of 7 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. MessagePagination
Pagination of the message.
E. SwitchOrderDetails
Information related to the switch order.
F. CopyDetails
Information provided when the message is a copy of a previous message.
G. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3488 May 2026
```

