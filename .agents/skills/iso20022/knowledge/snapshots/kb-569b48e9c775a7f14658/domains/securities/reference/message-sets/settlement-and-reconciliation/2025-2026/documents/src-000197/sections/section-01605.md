---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.131 SecuritiesSettlementStatus2Code"]
file_pages: [2143, 2144, 2145]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.131 SecuritiesSettlementStatus2Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2143 to 2145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2143

```text
Type: CodeSet
CodeName Name Definition
FULL FullyPaid Security is fully paid.
NILL NillPaid Security is nill paid.
PART PartiallyPaid Security is partially paid.
35.2.2.131  SecuritiesSettlementStatus2Code
Definition: Provides the status of settlement of an instruction.
Type: CodeSet
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
USET Unsettled Instruction is unsettled.
SETT Settled Full settlement.
PAIN PartialSettlement Part of the instruction remains unsettled.
35.2.2.132  SecuritiesStatementType1Code
Definition: Specifies whether the statement is an accounting or a custody statement.
Type: CodeSet
CodeName Name Definition
CUST Custody Statement is a custody statement.
ACCT Accounting Statement is an accounting statement.
35.2.2.133  SecuritiesTransactionType22Code
Definition: Specifies underlying information regarding the type of settlement transaction.
Type: CodeSet
CodeName Name Definition
BSBK BuySellBack Relates to a buy sell back transaction.
BYIY BuyIn Relates to a buy-in by the market
following a delivery transaction failure.
CNCB CentralBankCollateralOperation Relates to a collateral delivery/receipt to
a national central bank for central bank
credit operations.
COLI CollateralIn Relates to a collateral transaction, from
the point of view of the collateral taker or
its agent.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2143 March 2026
```

## File page 2144

```text
CodeName Name Definition
COLO CollateralOut Relates to a collateral transaction, from
the point of view of the collateral giver or
its agent.
CONV DepositoryReceiptConversion Relates to a depository receipt
conversion.
FCTA FactorUpdate Relates to a factor update.
INSP MoveOfStock Relates to a movement of shares into or
out of a pooled account.
ISSU Issuance Relates to the issuance of a security
such as an equity or a depositary
receipt.
MKDW MarkDown Relates to the decrease of positions held
by an International Central Securities
Depository (ICSD) at the common
depository due to custody operations
(repurchase, pre-release, proceeds of
corporate event realigned).
MKUP MarkUp Relates to the increase of positions held
by an International Central Securities
Depository (ICSD) at the common
depository due to custody operations
(repurchase, pre-release, proceeds of
corporate event realigned).
NETT Netting Relates to the netting of settlement
instructions.
NSYN NonSyndicated Relates to the issue of medium and short
term paper (CP, CD, MTN, notes) under
a program and without syndication
arrangement.
OWNE ExternalAccountTransfer Relates to an account transfer involving
more than one instructing party
(message sender) and/or account
servicer (messages receiver).
OWNI InternalAccountTransfer Relates to an account transfer involving
one instructing party (message sender)
at one account servicer (messages
receiver).
PAIR PairOff Relates to a pair-off: the transaction is
paired off and netted against one or
more previous transactions.
PLAC Placement Relates to the placement/new issue of a
financial instrument.
PORT PortfolioMove Relates to a portfolio move from one
investment manager to another and/or
from an account servicer to another. It is
generally charged differently than
another account transfer, hence the
need to identify this type of transfer as
such.
REAL Realignment Relates to a realignment of positions.
REDI Withdrawal Relates to the withdrawal of specified
amounts from specified subaccounts.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2144 March 2026
```

## File page 2145

```text
CodeName Name Definition
REDM Redemption Relates to a redemption of funds (funds
industry only).
RELE DepositoryReceiptReleaseCancellation Relates to a release (into/from local) of
depository receipt operation.
REPU Repo Relates to a repurchase agreement
transaction.
RODE ReturnDeliveryWithoutMatching Relates to the return of financial
instruments resulting from a rejected
delivery without a matching operation.
RVPO ReverseRepurchaseAgreement Relates to a reverse repurchase
agreement transaction.
SBBK SellBuyBack Relates to a sell buy back transaction.
SBRE BorrowingReallocation Internal reallocation of a borrowed
holding from one safekeeping account to
another.
SECB SecuritiesBorrowing Relates to a securities borrowing
operation.
SECL SecuritiesLending Relates to a securities lending operation.
SLRE LendingReallocation Internal reallocation of a holding on loan
from one safekeeping account to
another.
SUBS Subscription Relates to a subscription to funds (funds
industry only).
SYND SyndicateUnderwriters Relates to the issue of financial
instruments through a syndicate of
underwriters and a lead manager.
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
CLAI MarketClaim Relates to a market claim.
CORP CorporateAction Relates to a corporate action.
AUTO AutoCollateralisation Relates to an auto-collateralisation
movement.
SWIF SwitchFrom Transaction is a change of an
investment from one sub-fund to another
sub-fund (redemption-leg).
SWIT SwitchTo Transaction is a change of an
investment from one sub-fund to another
sub-fund (subscription-leg).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2145 March 2026
```

