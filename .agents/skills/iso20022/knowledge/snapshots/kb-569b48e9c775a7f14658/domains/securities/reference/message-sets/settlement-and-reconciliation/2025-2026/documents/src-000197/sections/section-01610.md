---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.138 SecuritiesTransactionType27Code"]
file_pages: [2155, 2156]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.138 SecuritiesTransactionType27Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2155 to 2156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2155

```text
CodeName Name Definition
ETFT ExchangeTradedFunds Relates to an ETF creation or
redemption.
ISSU Issuance Relates to the issuance of a security
such as an equity or a depositary
receipt.
SLRE LendingReallocation Internal reallocation of a holding on loan
from one safekeeping account to
another.
INSP MoveOfStock Relates to a movement of shares into or
out of a pooled account.
SBBK SellBuyBack Relates to a sell buy back transaction.
REDI Withdrawal Relates to the withdrawal of specified
amounts from specified subaccounts.
REBL Rebalancing Relates to a rebalanced transaction.
35.2.2.138  SecuritiesTransactionType27Code
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2155 March 2026
```

## File page 2156

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2156 March 2026
```

