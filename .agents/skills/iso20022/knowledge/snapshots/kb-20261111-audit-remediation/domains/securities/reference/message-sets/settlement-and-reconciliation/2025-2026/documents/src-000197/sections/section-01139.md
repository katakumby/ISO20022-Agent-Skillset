---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.47 SecurityClassificationType2Choice", "35.1.16.47.1 CFI <CFI>"]
file_pages: [1584, 1585, 1586]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.47.1 CFI <CFI>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1584 to 1586.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1584

```text
35.1.16.47.1  CFI <CFI>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification.
Datatype: "CFIOct2015Identifier" on page 2186
35.1.16.47.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Definition: Other type of classification of the financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see "GenericIdentification3"
on page 1495 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1495
   Issuer <Issr> [0..1] Text 1495
35.1.16.48  SecuritiesTransactionType43Choice
Definition: Choice of formats for a repair reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1584
Or}   Proprietary <Prtry> [1..1] ± 1587
35.1.16.48.1  Code <Cd>
Presence: [1..1]
Definition: Securities transaction type expressed as an ISO 20022 code.
Datatype: "SecuritiesTransactionType25Code" on page 2150
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1584 March 2026
```

## File page 1585

```text
CodeName Name Definition
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
REDM Redemption Relates to a redemption of funds (funds
industry only).
RELE DepositoryReceiptReleaseCancellation Relates to a release (into/from local) of
depository receipt operation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1585 March 2026
```

## File page 1586

```text
CodeName Name Definition
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
ETFT ExchangeTradedFunds Relates to an ETF creation or
redemption.
REBL Rebalancing Relates to a rebalanced transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1586 March 2026
```

