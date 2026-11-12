---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.79 TradingCapacity4Code"]
file_pages: [654, 655]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.79 TradingCapacity4Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 654 to 655.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 654

```text
CodeName Name Definition
BRBR BrokerToBroker A trade from a broker to another broker.
RISK RiskTrade Trade involving risk.
VWAP VWAPGuarantee Trade whose price is guaranteed as the
weighted average of the trade prices on
a specific day.
AGEN Agency Trade in which an agent intermediates
between a buyer and a seller.
GUAR GuaranteedClose Trade which is guaranteed to be
finalized.
EMTR EmployeeTradeReporting Transaction relates to employee trade
reporting.
ISSU Issuance Relates to the issuance of a security
such as an equity or a depositary
receipt.
BOST BondStart The trade is a Bond start.
BOEN BondEnd The trade is a Bond end.
LABO LendingAndBorrowing Indicates that the trade is a Lending and
borrowing.
BORE BondRepricing The trade is a Bond repricing.
OFIT OfferingIssuingTrade Indicates that the trade is a Offering
issue trade.
BOSU BondSubstitution The trade is a Bond substitution.
FBBT FutureBuyBackTrade The security will be bought back in the
future.
OPTN Options Indicates that the trade is a Option
contract trade.
FUOP FuturesOption Indicates that the trade is a Futures
option contract trade.
FUTR Futures Indicates that the trade is a Futures
contract trade.
7.2.2.79  TradingCapacity4Code
Definition: Specifies the role of a trading party in a transaction.
Type: CodeSet
CodeName Name Definition
PRIN Principal Trading as Principal.
CPRN CrossingPrincipal Crossing as a principal.
RISP RisklessPrincipal Trading as a riskless principal, ie, the
order to buy(sell) has been
simultaneously offset by an order to sell
(buy) with another party.
PROP Proprietary Trading for its firm. The transaction
affects the firm's own account, not that of
its customers.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 654 February 2025
```

## File page 655

```text
CodeName Name Definition
AGEN Agent Trading as Agent on behalf of a
customer.
CAGN CrossingAgent Crossing as an agent.
OAGN OtherAgent Acting as an agent for a party other than
a customer.
PRAG PrincipalAgent Acting as an agent for some executions
and principal for others in the same
transaction.
BAGN ActingAgent Party acting as an agent for both
customer and another person.
INFI InvestmentFirm Any legal person whose regular
occupation or business is the provision
of one or more investment services to
third parties and/or the performance of
one or more investment activities on a
professional basis.
MKTM MarketMaker Dealer or specialist that is trading for
their own account in the OTC market.
Market makers are expected to maintain
an orderly market by being available to
buy or sell.
MLTF MultilateralTradingFacility Multilateral Trading Facility (MTF) is a
multilateral system which brings together
multiple third-party buying and selling
interests in financial instruments in a way
that results in a contract.
RMKT RegulatedMarket Regulated market on which financial
instruments can be traded according to
rules defined by the stock exchange.
SINT SystematicInternaliser Firms which, on an organised, frequent
and systematic basis, deal on their own
account by executing client orders
outside a regulated market or an MTF.
SIs have the obligation to provide, and
make public, a definite bid and offer
quote for liquid securities.
TAGT TransferAgent Party appointed by the Fund
Management Company. It updates
records of investor accounts to reflect
the daily investor purchases,
redemptions, switches, transfers, and re-
registrations. It ensures the timely
settlement of transactions, and may
provide tax information to the investor
and/or to its intermediaries. It may
calculate, collect, and rebate
commissions. It prepares and distributes
confirmations reflecting transactions,
resulting in unit or cash account
movements to the investor or the
investor's intermediary. It responds to
inquiries concerning account status, and
processes the income distribution.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 655 February 2025
```

