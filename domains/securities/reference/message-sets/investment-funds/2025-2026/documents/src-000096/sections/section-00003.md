---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [11, 12, 13, 14, 15, 16, 17, 18, 19]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08", "acmt.002.001.08", "acmt.003.001.08", "acmt.005.001.06", "acmt.006.001.07", "camt.040.001.04", "camt.041.001.04", "camt.042.001.04", "camt.043.001.04", "camt.044.001.03", "camt.045.001.03", "reda.001.001.05", "reda.002.001.05", "reda.004.001.07", "reda.005.001.03", "semt.001.001.03", "semt.002.001.02", "semt.003.001.02", "semt.004.001.02", "semt.005.001.02", "semt.006.001.02", "semt.007.001.02", "sese.001.001.10", "sese.002.001.09", "sese.003.001.10", "sese.004.001.09", "sese.005.001.10", "sese.006.001.09", "sese.007.001.10", "sese.008.001.09", "sese.009.001.09", "sese.010.001.07", "sese.011.001.10", "sese.012.001.12", "sese.013.001.12", "sese.014.001.09", "sese.018.001.10", "sese.019.001.09", "sese.043.001.02", "setr.001.001.05", "setr.002.001.05", "setr.003.001.05", "setr.004.001.05", "setr.005.001.05", "setr.006.001.06", "setr.007.001.05", "setr.008.001.05", "setr.009.001.05", "setr.010.001.05", "setr.011.001.05", "setr.012.001.06", "setr.013.001.05", "setr.014.001.05", "setr.015.001.05", "setr.016.001.05", "setr.017.001.05", "setr.018.001.05", "setr.047.001.03", "setr.049.001.03", "setr.051.001.03", "setr.053.001.03", "setr.055.001.03", "setr.057.001.03", "setr.058.001.03"]
---

# 1 Message Set Overview

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 11 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
1 Message Set Overview
Introduction
This document describes the Investment Funds message set. It includes the new version of the
MessageDefinitions that have been added as part of the maintenance cycle 2025-2026 (See MCR
#276) and approved by the Securities Standards Evaluation Group on 27 January 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
acmt.001.001.08
AccountOpeningInstructionV08
The AccountOpeningInstruction message is sent by an
account owner, for example, an investor or its
designated agent to the account servicer, for example,
a registrar, transfer agent, custodian or securities
depository, to instruct the opening of an account or the
opening of an account and the establishment of an
investment plan.
acmt.002.001.08
AccountDetailsConfirmationV08
The AccountDetailsConfirmation message is sent by
an account servicer, for example, a registrar, transfer
agent, custodian bank or securities depository to the
account owner, for example, an investor to confirm the
opening of an account, execution of an
AccountModificationInstruction or to return information
requested in a GetAccountDetails message.
acmt.003.001.08
AccountModificationInstructionV08
The AccountModificationInstruction message is sent by
an account owner, for example, an investor or its
designated agent to the account servicer, for example,
a registrar, transfer agent, custodian bank or securities
depository to modify, that is, create, update or delete
specific details of an existing account.
acmt.005.001.06
RequestForAccountManagementStatusReportV
06
The RequestForAccountManagementStatusReport
message is sent by an account owner, for example, an
investor or its designated agent, to the account
servicer, for example, a registrar, transfer agent,
custodian bank or securities depository to request the
status of an AccountOpeningInstruction,
GetAccountDetails or an
AccountModificationInstruction.
acmt.006.001.07
AccountManagementStatusReportV07
The AccountManagementStatusReport message is
sent by an account servicer, for example, a registrar,
transfer agent, custodian bank or securities depository
to the account owner or its designated agent, for
example, an investor to report on the receipt or the
processing status of a previously received account
management message.
camt.040.001.04
FundEstimatedCashForecastReportV04
A report provider, such as a transfer agent, sends the
FundEstimatedCashForecastReport message to the
report user, such as an investment manager or pricing
agent, to report the estimated cash incomings and
outgoings of one or more share classes of an
investment fund on one or more trade dates.
The cash movements may result from, for example,
redemption, subscription, switch transactions or
reinvestment of dividends.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 11 May 2026
```

## File page 12

```text
MessageDefinition Definition
camt.041.001.04
FundConfirmedCashForecastReportV04
A report provider, such as a transfer agent, sends the
FundConfirmedCashForecastReport message to the
report user, such as an investment manager or pricing
agent, to report the confirmed cash incomings and
outgoings of one or more share classes of an
investment fund on one or more trade dates.
The cash movements may result from, for example,
redemption, subscription, switch transactions or
reinvestment of dividends.
camt.042.001.04
FundDetailedEstimatedCashForecastReportV0
4
A report provider, such as a transfer agent, sends the
FundDetailedEstimatedCashForecastReport message
to the report user, such as an investment manager or
pricing agent, to report the estimated cash incomings
and outgoings, sorted by country, institution name or
other criteria defined by the user of one or more share
classes of an investment fund on one or more trade
dates.
The cash movements may result from, for example,
redemption, subscription, switch transactions or
reinvestment of dividends.
camt.043.001.04
FundDetailedConfirmedCashForecastReportV0
4
A report provider, such as a transfer agent, sends the
FundDetailedConfirmedCashForecastReport message
to the report user, such as an investment manager or
pricing agent, to report the confirmed cash incomings
and outgoings, sorted by country, institution name or
other criteria defined by the user of one or more share
classes of an investment fund on one or more trade
dates.
The cash movements may result from, for example,
redemption, subscription, switch transactions or
reinvestment of dividends.
camt.044.001.03
FundConfirmedCashForecastReportCancellatio
nV03
A report provider, such as a transfer agent, sends the
FundConfirmedCashForecastReportCancellation
message to the report user, such as an investment
manager or pricing agent, to cancel a previously sent
FundConfirmedCashForecastReport message.
camt.045.001.03
FundDetailedConfirmedCashForecastReportCa
ncellationV03
A report provider, such as a transfer agent, sends the
FundDetailedConfirmedCashForecastReportCancellati
on messages to the report user, such as an investment
manager, fund accountant or any other interested
party, to cancel a previously sent
FundDetailedConfirmedCashForecastReport.
reda.001.001.05
PriceReportV05
A report provider, for example, a transfer agent, fund
accountant or market data provider, sends the
PriceReport message to the report recipient, for
example, a fund management company, transfer
agent, market data provider, regulator or any other
interested party to provide the net asset value and
price information for financial instruments on specific
trade dates and, optionally, to quote price variation
information.
reda.002.001.05
PriceReportCancellationV05
A report provider, for example, a transfer agent, fund
accountant or market data provider, sends the
PriceReportCancellation message to the report
recipient, for example, a fund management company,
transfer agent, market data provider, regulator or any
other interested party to cancel previously sent prices.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 12 May 2026
```

## File page 13

```text
MessageDefinition Definition
reda.004.001.07
FundReferenceDataReportV07
The FundReferenceDataReport message is sent by a
report provider, for example, a fund promoter, fund
management company, transfer agent, or market data
provider to the report recipient, for example, a
professional investor, investment fund distributor,
market data provider, regulator or other interested
party, to provide the key reference data for financial
instruments to facilitate trading. The message may also
include reporting data concerning product governance,
such as target market data, and a breakdown of the
costs and fees.
reda.005.001.03
InvestmentFundReportRequestV03
The InvestmentFundReportRequest message is sent
by a report user, for example, a professional investor,
investment fund distributor, market data provider,
regulator or other interested party to the report
provider, for example, a fund promoter, fund
management company, transfer agent, or market data
provider to request a report.
The Investment Fund Report Request message can be
used to request one or many fund reference data
report messages.
semt.001.001.03
SecuritiesMessageRejectionV03
An account servicer, for example, a registrar, transfer
agent or custodian bank, sends the
SecuritiesMessageRejection message to the account
owner, for example, an investor or its authorised agent,
to reject a previously received message on which
action cannot be taken.
The message may also be sent by an executing party,
for example, transfer agent to the instructing party, for
example, investment manager or its authorised
representative to reject a previously received message
on which action cannot be taken.
semt.002.001.02
CustodyStatementOfHoldingsV02
An account servicer, for example, a transfer agent
sends the CustodyStatementOfHoldings message to
the account owner, for example, a fund manager or an
account owner's designated agent to provide detailed
holdings of the portfolio at a specified moment in time.
The message provides, at a moment in time, the
quantity and identification of the financial instruments
that the account servicer holds for the account owner.
The message can also include availability and the
location of holdings to facilitate trading and minimise
settlement issues.
The message reports all information per financial
instrument, ie, when a financial instrument is held at
multiple places of safekeeping, the total holdings for all
locations can be provided.
semt.003.001.02
AccountingStatementOfHoldingsV02
An account servicer, for example, a transfer agent
sends the AccountStatementOfHoldings message to
the account owner, for example, a fund manager or an
account owner's designated agent to provide detailed
holdings of the portfolio at a specified moment in time.
The message provides, at a moment in time,
valuations of the portfolio together with details of each
financial instrument holding.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 13 May 2026
```

## File page 14

```text
MessageDefinition Definition
The message can be sent either audited or un-audited
and may be provided on a trade date or settlement
date basis.
semt.004.001.02
CustodyStatementOfHoldingsCancellationV02
An account servicer, for example, a transfer agent,
sends the CustodyStatementOfHoldingsCancellation
message to the account owner, for example, an
investment manager or its authorised representative to
cancel a previously sent CustodyStatementOfHoldings
message.
semt.005.001.02
AccountingStatementOfHoldingsCancellationV0
2
An account servicer, for example, a transfer agent,
sends the AccountingStatementofHoldingsCancellation
message to the account owner, for example, a fund
manager or an account owner's designated agent, to
notify the cancellation of a previously sent
AccountingStatementOfHoldings message.
semt.006.001.02
StatementOfInvestmentFundTransactionsV02
An account servicer, for example, a transfer agent
sends the StatementOfInvestmentFundTransactions
message to the account owner, for example, an
investment manager or its authorised representative to
provide detailed transactions (increases and
decreases) of holdings which occurred during a
specified period of time.
semt.007.001.02
StatementOfInvestmentFundTransactionsCanc
ellationV02
An account servicer, for example, a transfer agent
sends the
StatementOfInvestmentFundTransactionsCancellation
message to the account owner, for example, an
investment manager or its authorised representative to
cancel a previously sent
StatementOfInvestmentFundTransactions message.
sese.001.001.10
TransferOutInstructionV10
The TransferOutInstruction message is sent by an
instructing party, for example, an investment manager
or its authorised representative, to the executing party,
for example, a transfer agent, to instruct the delivery of
a financial instrument, free of payment, on a given date
from a specified party.
This message may also be used to instruct the delivery
of a financial instrument, free of payment, to another of
the instructing parties own accounts or to a third party.
sese.002.001.09
TransferOutCancellationRequestV09
The TransferOutCancellationRequest message is sent
by an instructing party, for example, an investment
manager or its authorised representative, to the
executing party, for example, a transfer agent, to
request the cancellation of a previously sent transfer
out instruction.
sese.003.001.10
TransferOutConfirmationV10
sese.004.001.09
ReversalOfTransferOutConfirmationV09
The ReversalOfTransferOutConfirmation message is
sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an
investment manager or its authorised representative, to
cancel a previously sent transfer out confirmation.
sese.005.001.10
TransferInInstructionV10
sese.006.001.09 The TransferInCancellationRequest message is sent
by an instructing party, for example, an investment
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 14 May 2026
```

## File page 15

```text
MessageDefinition Definition
TransferInCancellationRequestV09 manager or its authorised representative, to the
executing party, for example, a transfer agent, to
request the cancellation of a previously sent transfer in
instruction.
sese.007.001.10
TransferInConfirmationV10
The TransferInConfirmation message is sent by an
executing party, for example, a transfer agent, to the
instructing party, for example, an investment manager
or its authorised representative, to confirm the receipt
of a financial instrument, free of payment, on a given
date, from a specified party.
This message may also be used to confirm the receipt
of a financial instrument, free of payment, from another
of the instructing parties own accounts or from a third
party.
This message may also be used as an advice, that is,
the message is used to provide account information.
sese.008.001.09
ReversalOfTransferInConfirmationV09
The ReversalOfTransferInConfirmation message is
sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an
investment manager or its authorised representative, to
cancel a previously sent transfer in confirmation.
sese.009.001.09
RequestForTransferStatusReportV09
The RequestForTransferStatusReport is sent by an
instructing party, for example, an investment manager
or its authorised representative, to the executing party,
for example, a transfer agent to request the status of a
previously instructed transfer.
The RequestForTransferStatusReport may also be
sent by any party in the transfer transaction to another
party in the transfer transaction chain to request
information relevant for the settlement of a transfer
transaction.
sese.010.001.07
TransferCancellationStatusReportV07
The TransferCancellationStatusReport message is
sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an
investment manager or one of its authorised
representatives to provide the status of a previously
received transfer cancellation instruction.
sese.011.001.10
TransferInstructionStatusReportV10
The TransferInstructionStatusReport message is sent
by an executing party, for example, a transfer agent, to
the instructing party, for example, an investment
manager or one of its authorised representatives to
provide the status of a previously received request for
holdings information, portfolio transfer or transfer
instruction.
It may also be used to report the status of an event
related to the asset being transferred or provide
additional information.
The TransferInstructionStatusReport message may
also be sent by any party in the transfer transaction to
another party in the transfer transaction chain to
provide information relevant for the settlement of a
transfer transaction.
sese.012.001.12
PortfolioTransferInstructionV12
The PortfolioTransferInstruction message is sent by an
instructing party, for example, a (new) plan manager
(transferee), to the executing party, for example, a (old)
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 15 May 2026
```

## File page 16

```text
MessageDefinition Definition
plan manager (transferor), on behalf of the initiating
party, for example, an investor (client), to instruct the
transfer of financial instruments from the client's
account at the old plan manager (transferor) to the
clients account at the new plan manager (transferee).
sese.013.001.12
PortfolioTransferConfirmationV12
The PortfolioTransferConfirmation message is sent by
an executing party, for example, a (old) plan manager
(transferor), to the instructing party for example, a
(new) plan manager (transferee), to confirm the
transfer of financial instruments from the client's
account at the old plan manager (transferor) to the
clients account at the new plan manager (transferee).
sese.014.001.09
PortfolioTransferCancellationRequestV09
The PortfolioTransferCancellationRequest message is
sent by, for example, an investment manager or its
authorised representative, to the executing party, for
example, a transfer agent, to request the cancellation
of a previously sent PortfolioTransferInstruction
message.
sese.018.001.10
AccountHoldingInformationV10
The AccountHoldingInformation message is sent by an
executing party, for example, a (old) plan manager
(transferor), to the instructing party, for example, a
(new) plan manager (transferee), to provide
information about financial instruments held on behalf
of a client.
sese.019.001.09
AccountHoldingInformationRequestV09
The AccountHoldingInformationRequest message is
sent by an instructing party, for example, a (new) plan
manager (transferee), to the executing party, for
example, a (old) plan manager (transferor), on behalf
of the initiating party, for example, an investor (client),
to request information about financial instruments held
on behalf of the client.
sese.043.001.02
PortfolioTransferCompletionV02
The PortfolioTransferCompletion message is sent by
an executing party, for example, a (old) plan manager
(transferor), to the instructing party for example, a
(new) plan manager (transferee), to confirm that the
transfer of financial instruments from the client's
account at the old plan manager (transferor) to the
clients account at the new plan manager (transferee)
has been completed.
setr.001.001.05
RedemptionBulkOrderV05
The RedemptionBulkOrder message is sent by an
instructing party, for example, an investment manager
or its authorised representative, to the executing party,
for example, a transfer agent, to instruct a redemption
from a financial instrument for two or more accounts.
setr.002.001.05
RedemptionBulkOrderCancellationRequestV05
The RedemptionBulkOrderCancellationRequest
message is sent by an instructing party, for example,
an investment manager or its authorised
representative, to the executing party, for example, a
transfer agent, to request the cancellation of a
previously sent RedemptionBulkOrder.
setr.003.001.05
RedemptionBulkOrderConfirmationV05
The RedemptionBulkOrderConfirmation message is
sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an
investment manager or its authorised representative, to
confirm the details of execution for a previously
received RedemptionBulkOrder message.
setr.004.001.05 The RedemptionOrder message is sent by an
instructing party, for example, an investment manager
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 16 May 2026
```

## File page 17

```text
MessageDefinition Definition
RedemptionOrderV05 or its authorised representative, to the executing party,
for example, a transfer agent, to instruct the
redemption of one or more financial instruments for
one investment fund account.
setr.005.001.05
RedemptionOrderCancellationRequestV05
The RedemptionOrderCancellationRequest message
is sent by an instructing party, for example, an
investment manager or its authorised representative, to
the executing party, for example, a transfer agent, to
request the cancellation of a previously sent
RedemptionOrder.
setr.006.001.06
RedemptionOrderConfirmationV06
The RedemptionOrderConfirmation message is sent by
an executing party, for example, a transfer agent, to
the instructing party, for example, an investment
manager or its authorised representative, to confirm
the details of execution for a previously received
RedemptionOrder message.
setr.007.001.05
SubscriptionBulkOrderV05
The SubscriptionBulkOrder message is sent by an
instructing party, for example, an investment manager
or its authorised representative, to the executing party,
for example, a transfer agent, to instruct a subscription
to a financial instrument for two or more accounts.
setr.008.001.05
SubscriptionBulkOrderCancellationRequestV05
The SubscriptionBulkOrderCancellationRequest
message is sent by an instructing party, for example,
an investment manager or its authorised
representative, to the executing party, for example, a
transfer agent, to request the cancellation of a
previously sent SubscriptionBulkOrder.
setr.009.001.05
SubscriptionBulkOrderConfirmationV05
The SubscriptionBulkOrderConfirmation message is
sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an
investment manager or its authorised representative, to
confirm the details of the execution of a
SubscriptionBulkOrder instruction.
setr.010.001.05
SubscriptionOrderV05
The SubscriptionOrder message is sent by an
instructing party, for example, an investment manager
or its authorised representative, to the executing party,
for example, a transfer agent, to instruct the
subscription of one or more financial instruments for
one investment fund account.
setr.011.001.05
SubscriptionOrderCancellationRequestV05
The SubscriptionOrderCancellationRequest message
is sent by an instructing party, for example, an
investment manager or its authorised representative, to
the executing party, for example, a transfer agent, to
request the cancellation of a previously sent
SubscriptionOrder.
setr.012.001.06
SubscriptionOrderConfirmationV06
The SubscriptionOrderConfirmation message is sent
by an executing party, for example, a transfer agent, to
the instructing party, for example, an investment
manager or its authorised representative, to confirm
the details of the execution of a SubscriptionOrder
instruction.
setr.013.001.05
SwitchOrderV05
The SwitchOrder message is sent by an instructing
party, for example, an investment manager or its
authorised representative, to the executing party, for
example, a transfer agent, to instruct a switch
transaction from a financial instrument or multiple
financial instruments to a different specified financial
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 17 May 2026
```

## File page 18

```text
MessageDefinition Definition
instrument or instruments for a specified amount/
quantity.
setr.014.001.05
SwitchOrderCancellationRequestV05
The SwitchOrderCancellationRequest message is sent
by an instructing party, for example, an investment
manager or its authorised representative, to the
executing party, for example, a transfer agent, to
request the cancellation of a previously sent
SwitchOrder instruction.
setr.015.001.05
SwitchOrderConfirmationV05
The SwitchOrderConfirmation message is sent by an
executing party, for example, a transfer agent, to the
instructing party, for example, an investment manager
or its authorised representative, to confirm the details
of the execution of a previously received SwitchOrder
instruction.
setr.016.001.05
OrderInstructionStatusReportV05
The OrderInstructionStatusReport message is sent by
an executing party, for example, a transfer agent, to
the instructing party, for example, an investment
manager or its authorised representative, to report the
status of an order from the time the executing party
receives the order until the time the order is executed.
setr.017.001.05
OrderCancellationStatusReportV05
The OrderCancellationStatusReport message is sent
by an executing party, for example, a transfer agent, to
the instructing party, for example, an investment
manager or its authorised representative, to report the
status of an order cancellation request that was
previously received.
setr.018.001.05
RequestForOrderStatusReportV05
The RequestForOrderStatusReport message is sent by
an instructing party, for example, an investment
manager or its authorised representative, to the
executing party, for example, a transfer agent, to
request the status of one or more order instructions or
order cancellation requests.
setr.047.001.03
SubscriptionOrderConfirmationCancellationInstr
uctionV03
The
SubscriptionOrderConfirmationCancellationInstruction
message is sent by an executing party, for example, a
transfer agent, to the instructing party, for example, an
investment manager or its authorised representative, to
cancel a previously sent
SubscriptionOrderConfirmation.
setr.049.001.03
SubscriptionBulkOrderConfirmationCancellation
InstructionV03
The
SubscriptionBulkOrderConfirmationCancellationInstruct
ion message is sent by an executing party, for
example, a transfer agent, to the instructing party, for
example, an investment manager or its authorised
representative, to cancel a previously sent
SubscriptionBulkOrderConfirmation.
setr.051.001.03
RedemptionOrderConfirmationCancellationInstr
uctionV03
The
RedemptionOrderConfirmationCancellationInstruction
message is sent by an executing party, for example, a
transfer agent, to the instructing party, for example, an
investment manager or its authorised representative, to
cancel a previously sent
RedemptionOrderConfirmation.
setr.053.001.03
RedemptionBulkOrderConfirmationCancellationI
nstructionV03
The
RedemptionBulkOrderConfirmationCancellationInstruct
ion message is sent by an executing party, for
example, a transfer agent, to the instructing party, for
example, an investment manager or its authorised
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 18 May 2026
```

## File page 19

```text
MessageDefinition Definition
representative, to cancel a previously sent
RedemptionBulkOrderConfirmation.
setr.055.001.03
SwitchOrderConfirmationCancellationInstruction
V03
The SwitchOrderConfirmationCancellationInstruction
message is sent by an executing party, for example, a
transfer agent, to the instructing party, for example, an
investment manager or its authorised representative, to
cancel a previously sent SwitchOrderConfirmation.
setr.057.001.03
OrderConfirmationStatusReportV03
The OrderConfirmationStatusReport message is sent
by an instructing party, for example, an investment
manager or its authorised representative, to the
executing party, for example, a transfer agent, to report
the status of an order confirmation or an order
confirmation amendment.
setr.058.001.03
RequestForOrderConfirmationStatusReportV03
The RequestForOrderConfirmationStatusReport
message is ent by an executing party, for example, a
transfer agent, to the instructing party, for example, an
investment manager or its authorised representative, to
request the status of one or more order confirmations.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Investment Funds - Maintenance 2025 - 2026 19 May 2026
```

