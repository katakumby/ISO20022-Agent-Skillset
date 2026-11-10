---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"]
content_origin: "source-transcription"
---

# Order and Confirmation

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Order and Confirmation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P125** Order and Confirmation

**P126** Order messages are used to instruct the executing party to subscribe, to redeem or to switch a given amount/quantity of a specified financial instrument.

**P127** There are three types of order message, subscription, redemption and switch.

**P128** In the funds industry, orders may be instructed in a variety of different ways, for example, some institutions group orders before sending them to the next party in the chain.

**P129** In order to cater for this, two sub-categories have been created for the subscription and the redemption types of messages.

**P130** Bulk order

**P131** A bulk message is typically a message containing a series of individual order transactions from different accounts, but for the same financial instrument with the same intermediary. The order will result in a single cash settlement, rather than settlement per individual order, executed using one single method. This order is sent by a concentrator or a party collecting orders and bulking them to relay the transactions to the transfer agent or another intermediary.

**P132** Order

**P133** An order message is typically a message containing a single order or multiple orders (list of orders related to several financial instruments) for the same account. It is a 'shopping list' for one account. This type of order is typically sent by financial advisers or banks that are managing a portfolio for a particular account.

**P134** In short, a bulk order is "one financial instrument-n accounts"; and an order is "one account- one financial instrument" if it is a single order and "one account-n financial instruments" if it is a multiple order.

**P135** No specific message/s have been created for cross or 'bed and breakfast' orders. In some countries, for legal reasons, these must appear as separate orders, while in others, the two orders may be given together. Therefore, no specific order has been created for a bed and breakfast order, as this transaction is the combination of a redemption and a subscription linked together. Limit and forward orders are not covered, as these are not common in the funds industry.

[T7 - complete table](../tables/tbl-0007.md)

**P136** The following messages were removed from the SWIFTNet funds service 18 November 2017:

[T8 - complete table](../tables/tbl-0008.md)

**P137** The order confirmation messages are to be used for confirmation amendment 

**P138** In the 2017 maintenance, the 'classic' funds messages, for example, SubscriptionOrder (setr.010), RedemptionOrder (setr.004), were updated to include hedge/alternative funds functionality.

**P139** Users that are planning to implement the SWIFTNet funds messages for hedge/alternative funds orders should use the 'classic' messages (setr.010, 001, 012, 004, 005, 005, 016 and 017) in preference to the 'alternative funds' messages (setr.059, 060, 061, 062, 064) which are also documented in this message definition report and will remain in the SWIFTNet Funds solution until there is no demand. 

