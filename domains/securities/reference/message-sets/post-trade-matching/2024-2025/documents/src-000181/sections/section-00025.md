---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05"]
file_pages: [28, 29, 30]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3 setr.027.001.05 SecuritiesTradeConfirmationV05

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 28 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

```text
3 setr.027.001.05
SecuritiesTradeConfirmationV05
3.1 MessageDefinition Functionality
SCOPE
Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to
provide trade confirmation on a per-account basis based on instructions provided by the instructing
party in the SecuritiesAllocationInstruction message.
It may also be used to provide trade confirmation on the trade level from an executing party or an
instructing party to the custodian or an affirming party directly or through CMU.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
The custodian or the affirming party is typically the custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or their agent.
USAGE
Initiator: In local matching, the initiator of this message is always the executing party. In central
matching the initiator may be either the executing party or instructing party.
Respondent: instructing party, a custodian or an affirming party responds with
SecuritiesTradeConfirmationResponse (accept or reject) message.
Outline
The SecuritiesTradeConfirmationV05 MessageDefinition is composed of 22 MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmation message as known by
the account owner (or the instructing party acting on its behalf).
B. NumberCount
Count of the number of transactions linked.
C. References
Reference to the transaction identifier issued by a business party and/or market infrastructure. It
may also be used to reference a previous transaction, for example, a block/allocation instruction, or
tie a set of messages together.
D. TradeDetails
Details of the trade.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 28 February 2025
```

## File page 29

```text
E. FinancialInstrumentIdentification
Unique and unambiguous identifier of a financial instrument, assigned under a formal or proprietary
identification scheme.
F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. UnderlyingFinancialInstrument
Underlying financial instrument to which an trade confirmation is related.
H. Stipulations
Additional restrictions on the financial instrument, related to the stipulation.
I. ConfirmationParties
Parties involved in the confirmation of the details of a trade.
J. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
K. StandingSettlementInstruction
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
L. DeliveringSettlementParties
Specifies the chain of delivering settlement parties.
M. ReceivingSettlementParties
Specifies the chain of receiving settlement parties.
N. CashParties
Cash parties involved in the specific transaction.
O. ClearingDetails
Provides clearing member information.
P. SettlementAmount
Total amount of money to be paid or received in exchange for the securities. The amount includes
the principal with any commissions and fees or accrued interest.
Q. OtherAmounts
Other amounts than the settlement amount.
R. OtherPrices
Other prices than the deal price.
S. OtherBusinessParties
Other business parties relevant to the transaction.
T. TwoLegTransactionDetails
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 29 February 2025
```

## File page 30

```text
Specifies a transaction that the trading parties are agreeing to repurchase, sell back or return the
same or similar securities at a later time.
The two leg transaction details defines the closing leg conditions of a two leg transaction. It is also
used to define the anticipated closing leg conditions at the time of opening the closed-end
transaction.
U. RegulatoryStipulations
Specifies regulatory stipulations that financial institutions must be compliant with in the country,
region, and/or area they conduct business.
V. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 30 February 2025
```

