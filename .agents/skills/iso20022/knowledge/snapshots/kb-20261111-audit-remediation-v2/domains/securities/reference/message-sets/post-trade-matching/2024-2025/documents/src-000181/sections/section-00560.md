---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.71 SettlementTransactionType7Code"]
file_pages: [648, 649]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.71 SettlementTransactionType7Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 648 to 649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 648

```text
CodeName Name Definition
FRCL FreeCleanSettlement Delivery will be made free of payment
but a clean payment order will be sent.
KNOC KnockedOut Settlement transaction relates to options,
futures or derivatives that are expired
worthless.
PHYS Physical Securities are to be physically settled.
CSDP CSDPaymentOnly Transaction on a security that is not
eligible at the Central Securities
Depository (CSD) but for which the
payment will be enacted by the CSD.
SPCS SplitCurrencySettlement Settlement is in two different currencies.
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
UNEX Unexposed Delivery cannot be performed until
money is received.
7.2.2.71  SettlementTransactionType7Code
Definition: Specifies underlying information regarding the type of settlement transaction.
Type: CodeSet
CodeName Name Definition
BSBK BuySellBack Relates to a buy sell back transaction.
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
(repurchase, pre-release, proceed of
corp. event realigned).
MKUP MarkUp Relates to the increase of positions held
by an International Central Securities
Depository (ICSD) at the common
depository due to custody operations
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 648 February 2025
```

## File page 649

```text
CodeName Name Definition
(repurchase, pre-release, proceed of
corporate event realigned).
NETT Netting Relates to the netting of settlement
instructions.
NSYN NonSyndicated Relates to the issue of medium and short
term paper (CP, CD, MTN, notes.) under
a program and without syndication
arrangement.
OWNE ExternalAccountTransfer Relates to an account transfer involving
more than one instructing party
(messages sender) and/or account
servicer (messages receiver).
OWNI InternalAccountTransfer Relates to an account transfer involving
one instructing party (messages sender)
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
RELE DepositoryReceiptReleaseCancellation Relates to a release (into/from local) of
depository receipt operation.
REPU Repo Relates to a repurchase agreement
transaction.
RODE ReturnDeliveryWithoutMatching Relates to the return of financial
instruments resulting from a rejected
delivery without matching operation.
RPTO Reporting Relates to a transaction that is for
reporting purposes only.
RVPO ReverseRepurchaseAgreement Relates to a reverse repurchase
agreement transaction.
SBBK SellBuyBack Relates to a sell buy back transaction.
SECB SecuritiesBorrowing Relates to a securities borrowing
operation.
SECL SecuritiesLending Relates to a securities lending operation.
SYND SyndicateUnderwriters Relates to the issue of financial
instruments through a syndicate of
underwriters and a lead manager.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 649 February 2025
```

