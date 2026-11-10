---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.55 SuspendedStatusReason1Code"]
file_pages: [874, 875, 876, 877, 878]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.55 SuspendedStatusReason1Code

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 874 to 878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 874

```text
CodeName Name Definition
USTO UserDefinedStandingOrder Liquidity transfer standing order type,
that has been customised or defined to
the specific need of the user.
PSTO PredefinedStandingOrder Liquidity transfer standing order type, as
predefined in the system.
37.2.2.55  SuspendedStatusReason1Code
Definition: Specifies the reason the transaction/instruction is suspended.
Type: CodeSet
CodeName Name Definition
SUBY SuspendedByYourself Transaction/instruction is suspended
following your earlier suspension
instruction.
SUBS SuspendedBySystem Transaction/instruction is suspended
following a system suspension
instruction.
37.2.2.56  SystemBalanceType2Code
Definition: Specifies the nature of the balance within a system processing the transactions.
Type: CodeSet
CodeName Name Definition
OPNG Opening Book balance of the account at the
beginning of the account servicer's
business day. It always equals the
closing book balance from the previous
business day.
Note: the available balance at the
beginning of the account servicer's
business day may be different from the
closing book balance from the previous
business day.
INTM Interim Balance calculated in the course of the
account servicer's business day, at the
time specified, and subject to further
changes during the business day. The
interim balance is calculated on the
basis of booked credit and debit items
during the calculation time/period
specified.
CLSG Closing Balance of the account at the end of the
account servicer's business day. It is the
sum of the opening balance at the
beginning of the day and all entries
booked to the account during the
account servicer's business day.
BOOK Book Balance that is registered in the books of
the account servicer.
CRRT Current Balance of the account at a precise
moment in time.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 874 February 2025
```

## File page 875

```text
CodeName Name Definition
PDNG Pending Balance of securities pending delivery,
such as the orders to sell securities have
been executed but settlement of the
open transactions has not been
confirmed.
LRLD LimitRelated Balance of a specific limit value, such as
a bilateral balance is calculated in
relation to a given bilateral limit.
AVLB Available Balance of money or securities that is at
the disposal of the account owner on the
date specified.
LTSF LiquidityTransfer Balance composed of the sum of all
liquidity transfers made to or from an
account.
CRDT Credit Balance representing the sum of all
credit entries booked to an account.
EAST EligibleAssets Balance representing the potential loan a
Central Bank would make in cash if the
collateral is pledged, such as securities
available and eligible as collateral with
the central bank.
PYMT Payment Balance representing the sum of entries
as a result of payments processing.
Entries relating to fees, interest, or other
movements not a result of payments
sent or received by the account owner
are not included.
BLCK Blocked Balance representing the regulatory
reserve that a financial institution must
have with the account servicing
institution, such as the minimum credit
balance a financial institution is to keep
with its Central Bank for mandatory
reserve purposes. In some countries, a
blocked balance is known as a 'reserve'
balance.
XPCD Expected Balance, composed of booked entries
and pending items known at the time of
calculation, which projects the end of
day balance if everything is booked on
the account and no other entry is posted.
DLOD DaylightOverdraft Balance representing the intra day
overdraft granted by the central bank to
financial institutions participating in a
RTGS system. This balance may vary
over time and shall be offset at the end
of the day.
XCRD ExpectedCredit Balance, composed of booked entries
and pending items known at the time of
calculation, which projects the end of
day credit balance if everything books to
the account and no other credit entry is
posted.
XDBT ExpectedDebit Balance, composed of booked entries
and pending items known at the time of
calculation, which projects the end of
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 875 February 2025
```

## File page 876

```text
CodeName Name Definition
day debit balance if everything books to
the account and no other debit entry is
posted.
ADJT Adjustment Average balance to be held in the
settlement account at the end of each
day in order to fulfil the reserve due.
The approximation will be always made
rounding up.
PRAV ProgressiveAverage Average of the daily balances on the
account used to fulfil the reserve
requirements calculated from the
beginning of the maintenance period.
DBIT Debit Balance representing the sum of all debit
entries booked to an account.
THRE Threshold Balance representing the amount that
will be destined for investment.
Difference between available balance
and threshold for investment limit.
NOTE Noted Balance representing the amount that a
financial institution has set aside for a
specific reason and which is therefore
not available.
FSET ForecastSettlement Balance representing the forecast of
total of all cash legs for trades that are
ready to settle via a central securities
depository. Amounts shown are still
subject to processing of the securities
settlement.
BLOC BlockedTrades Balance representing the projected total
of all cash legs for trades settling via a
central securities depository that have
been matched but blocked in order to not
settle. These blocked trades are
included in the calculation for settlement
(for example to avoid overdrafts).
Usage rule: Blocking can be done by
account owner or its counterparties.
Usually this is done to chain transactions
or to prioritise other trades. Blocked
trades have an indicator that prevents
the transactions from settling. Once
matched, they can settle whenever the
freeze is lifted. In this case they will
move to FSET. Lifting the freeze can
happen anytime during the day and the
transaction will be settling in the next
settlement cycle which can be the same
day if the (international) central
securities depository's operates several
settlements cycles per day.
OTHB OtherBlockedTrades Balance representing the projected total
of all cash legs for trades settling via a
central securities depository that have
been matched but blocked in order to not
settle. These blocked transactions are
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 876 February 2025
```

## File page 877

```text
CodeName Name Definition
not included in the calculation for
settlement.
CUST Custody Balance representing the projected total
of all asset servicing transactions such
as dividends, income corporate actions
equivalents, tax returns, etc.
FORC CashForecast Balance representing the total of all
balance types representing transactions
to settle, blocked items and custody
transactions.
COLC DividendsCollection Balance representing the projected total
amount of all payment obligations to the
participant (bank), based on their role as
main paying agent.
FUND NetFunding Balance representing the net amount to
be funded resulting from all transactions
which have an impact on the funding
requirement.
PIPO PayInPayOut Balance representing the fictive forecast
of automated direct debits or payment
based on standing arrangements
between a central securities depository
and the user.
Usage: Pay-Ins and Pay-Outs can be
different based on individual payment
instructions or available funds.
XCHG ExchangeForecast Balance representing the forecast of the
total of all cash legs of transactions
traded in exchanges.
CCPS CentralCounterparty Balance representing the forecast of the
total of all cash legs of transactions
traded in exchanges that operate a
central counterparty functionality.
TOHB TotalOnHold Balance representing the total of the
payments that were put on hold because
the limits have been exceeded.
COHB CreditOnHold Balance representing the total incoming
payments that were put on hold because
the credit limit has been exceeded.
DOHB DebitOnHold Balance representing the total outgoing
payments that were put on hold because
the debit limit has been exceeded.
TPBL TotalProcessed Balance representing the total of the
payments that have been processed and
are waiting for settlement during the day.
CPBL CreditProcessed Balance representing the total incoming
payments that have been processed and
are waiting for settlement.
DPBL DebitProcessed Balance representing the total outgoing
payments that have been processed and
are waiting for settlement.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 877 February 2025
```

## File page 878

```text
CodeName Name Definition
FUTB TotalFuture Balance representing the total of the
payments with a processing date in the
future.
REJB TotalRejected Balance representing the total of the
payments that have been rejected.
FCOL FirmCollateralisation Balance representing the forecast of the
cash-equivalent resulting from evaluation
of existing holdings at central securities
depositary that are qualified to serve as
collateral.
FCOU UsedAmountsFirmCollateralisation Balance representing the cash
equivalent resulting from evaluation of
existing holdings at CSD that are
qualified to serve as collateral and have
been used as collateral.
SCOL SelfCollateralisation Balance representing the forecast of the
cash-equivalent resulting from evaluation
of the net incoming balance of securities
qualified to serve as collateral for which
settlement instructions are held at.
SCOU UsedAmountsSelfCollateralisation Balance representing the cash-
equivalent resulting from evaluation of
incoming securities, qualified to serve as
collateral and actually used as collateral,
which have been settled during the
settlement process.
CUSA CustodyActual Balance representing the actual total of
all asset servicing transactions such as
dividends, income corporate actions
equivalents, tax returns, redemptions,
etc.
XCHC CCPGuaranteedForecasting Balance representing the forecast of the
total of all cash legs of transactions in
exchanges, going through CCP
functions.
XCHN NonCCPGuaranteedForecasting Balance representing the forecast of the
total of all cash legs of transactions
traded in exchanges not going through
central counter party (CCP) functions.
DSET DefinitiveSettledSecurities Balance representing the cash
equivalent of all settled securities
transactions.
LACK LackOfHoldingsTransactions Balance representing the cash
equivalent of transactions with a lack of
holdings.
NSET NonSettledSecurities Balance representing the cash
equivalent of all non-settled securities
transactions.
OTCC CCPGuaranteedOTCTransactions Balance representing the Forecast of the
total of all cash-legs of transactions 'over
the counter' (OTC), going through central
counter party (CCP) functions.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 878 February 2025
```

