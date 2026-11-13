---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.2 ExtendedTransactionType <XtndedTxTp>"]
file_pages: [4720, 4721]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.2 ExtendedTransactionType <XtndedTxTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4720 to 4721.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4720

```text
CodeName Name Definition
REAA RedemptionAssetAllocation Transaction is a redemption in an asset
allocation plan which enables investors
to withdraw, by percentage a certain
amount of cash from several sub-funds
of a same umbrella structure.
66.1.26.3.2  ExtendedTransactionType <XtndedTxTp>
Presence: [1..1]
Warning   Either TransactionType or ExtendedTransactionType or CorporateActionEventType or
ExtendedCorporateActionEventType must be present but not more than one.
Definition: Type of investment fund transaction.
Datatype: "Extended350Code" on page 5402
66.1.26.3.3  CorporateActionEventType <CorpActnEvtTp>
Presence: [1..1]
Warning   Either TransactionType or ExtendedTransactionType or CorporateActionEventType or
ExtendedCorporateActionEventType must be present but not more than one.
Definition: Type of corporate action event.
Datatype: "CorporateActionEventType1Code" on page 5288
CodeName Name Definition
DRIP DividendReinvestment Event is a dividend payment type where
cash dividend is rolled over into
additional shares in the issuing
company.
CAPG CapitalGainsDistribution Event is the distribution of profits
resulting from the sale of securities.
Shareholders of mutual funds, unit
trusts, or Sicavs are recipients of capital
gains distributions and are often
reinvested in additional shares of the
fund.
DVCA CashDividend Event is a distribution of cash to
shareholders, in proportion to their equity
holding. Ordinary dividends are recurring
and regular. The shareholder must take
cash and is not offered a choice in the
form of distribution.
DVOP DividendOption Event is a distribution of a dividend to
shareholders with the choice of payment
method. The shareholder must choose
the form of payment - stock, cash, or
both.
DVSE StockDividend Event is a dividend paid to shareholders
in the form of shares of stock in the
issuing company or in another company.
The shareholder must take stock and is
not offered a choice in the form of
distribution.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4720 May 2026
```

## File page 4721

```text
CodeName Name Definition
LIQU Liquidation Event is a liquidating dividend or
liquidation that consists of a distribution
of cash, assets, or both. Debt may be
paid in order of priority based on
preferred claims to assets specified by
the security. The security holder may be
able to choose the form of liquidation
distribution.
MRGR Merger Event is a mandatory or voluntary
exchange of outstanding securities as
the result of two or more companies
combining assets. Cash payments may
accompany share exchange.
NAME NameChange Event is a name change. The issuing
company changes its name. The event
shows the change from old name to new
name and may involve surrendering
physical shares with the old name to the
registrar.
SOFF SpinOff Event is a demerger or distribution or an
unbundling. It is a distribution of
subsidiary stock to the shareholders of
the parent company without a surrender
of shares. A spin-off represents a form of
divestiture resulting in an independent
company. Normally this is without cost to
the parent issue shareholder.
SPLF StockSplit Event is a change in nominal value, a
subdivision. It is an increase in a
corporation's number of outstanding
shares of stock without any change in
the shareholder's equity or the aggregate
market value at the time of the split.
Stock price and nominal value are
reduced accordingly.
SPLR ReverseStockSplit Event is a change in nominal value, a
consolidation. It is a decrease in number
of outstanding shares of stock without
any change in the shareholder's equity
or the aggregate market value at the
time of the split. Stock price and nominal
value are reduced accordingly.
TEND Tender Event is an acquisition or take-over or
offre publique de retrait (FR) or purchase
offer or buy-back. It is an offer made to
shareholders requesting them to sell
(tender) their shares for a specified price
usually at a premium over prevailing
market price. Generally, the objective of
a tender offer is to take control of the
target company.
BONU BonusIssue Event is a bonus issue or scrip issue or
capitalisation issue. Security holders are
awarded additional assets free of
payment from the issuer in proportion to
their holding. A bonus issue is typically
represented by shares, rights or
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4721 May 2026
```

