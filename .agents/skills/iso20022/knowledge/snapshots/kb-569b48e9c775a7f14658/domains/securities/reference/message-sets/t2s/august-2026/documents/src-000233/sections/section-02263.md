---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.52 InterestComputationMethodFormat4Choice", "82.1.19.52.2 Proprietary <Prtry>"]
file_pages: [3036, 3037, 3038]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.52.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3036 to 3038.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3036

```text
CodeName Name Definition
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
NARR Narrative Other method than A001-A020. See
Narrative.
82.1.19.52.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the format of interest computation method.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.53  SecuritiesTransactionType44Choice
Definition: Choice of formats for settlement transaction type information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3036
Or}   Proprietary <Prtry> [1..1] ± 3039
82.1.19.53.1  Code <Cd>
Presence: [1..1]
Definition: Securities transaction type expressed as an ISO 20022 code.
Datatype: "SecuritiesTransactionType26Code" on page 3295
CodeName Name Definition
BSBK BuySellBack Relates to a buy sell back transaction.
COLI CollateralIn Relates to a collateral transaction, from
the point of view of the collateral taker or
its agent.
COLO CollateralOut Relates to a collateral transaction, from
the point of view of the collateral giver or
its agent.
MKDW MarkDown Relates to the decrease of positions held
by an International Central Securities
Depository (ICSD) at the common
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3036 August 2026
```

## File page 3037

```text
CodeName Name Definition
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
REDM Redemption Relates to a redemption of funds (funds
industry only).
REPU Repo Relates to a repurchase agreement
transaction.
RODE ReturnDeliveryWithoutMatching Relates to the return of financial
instruments resulting from a rejected
delivery without a matching operation.
RVPO ReverseRepurchaseAgreement Relates to a reverse repurchase
agreement transaction.
SECB SecuritiesBorrowing Relates to a securities borrowing
operation.
SECL SecuritiesLending Relates to a securities lending operation.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3037 August 2026
```

## File page 3038

```text
CodeName Name Definition
TRVO TripartyReverseRepo Relates to a triparty reverse repurchase
agreement.
TURN Turnaround Relates to a turnaround: the same
security is bought and sold to settle the
same day, to or from different brokers.
BYIY BuyIn Relates to a buy-in by the market
following a delivery transaction failure.
CNCB CentralBankCollateralOperation Relates to a collateral delivery/receipt to
a national central bank for central bank
credit operations.
OWNE ExternalAccountTransfer Relates to an account transfer involving
more than one instructing party
(message sender) and/or account
servicer (messages receiver).
FCTA FactorUpdate Relates to a factor update.
OWNI InternalAccountTransfer Relates to an account transfer involving
one instructing party (message sender)
at one account servicer (messages
receiver).
RELE DepositoryReceiptReleaseCancellation Relates to a release (into/from local) of
depository receipt operation.
SBRE BorrowingReallocation Internal reallocation of a borrowed
holding from one safekeeping account to
another.
CORP CorporateAction Relates to a corporate action.
CLAI MarketClaim Relates to a market claim.
AUTO AutoCollateralisation Relates to an auto-collateralisation
movement.
SWIF SwitchFrom Transaction is a change of an
investment from one sub-fund to another
sub-fund (redemption-leg).
SWIT SwitchTo Transaction is a change of an
investment from one sub-fund to another
sub-fund (subscription-leg).
CONV DepositoryReceiptConversion Relates to a depository receipt
conversion.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3038 August 2026
```

