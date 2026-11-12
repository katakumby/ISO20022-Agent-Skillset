---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.1 BlockedStatusReason2Choice", "66.1.45.1.2 Reason <Rsn>"]
file_pages: [5165, 5166]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.1.2 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5165 to 5166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5165

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Transaction type for which the account is blocked and the underlying reason.
Reason <Rsn> contains the following BlockedStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionType <TxTp> [1..1]  5165
{Or     Code <Cd> [1..1] CodeSet 5165
Or}     Proprietary <Prtry> [1..1] ± 5167
   Blocked <Blckd> [1..1] Indicator 5167
   Reason <Rsn> [0..*]  5167
{Or     Code <Cd> [1..1] CodeSet 5167
Or}     Proprietary <Prtry> [1..1] ± 5168
   AdditionalInformation <AddtlInf> [1..1] Text 5168
66.1.45.1.2.1  TransactionType <TxTp>
Presence: [1..1]
Definition: Type of transaction for which the account has a blocked status.
TransactionType <TxTp> contains one of the following TransactionType5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5165
Or}   Proprietary <Prtry> [1..1] ± 5167
66.1.45.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Transaction type expressed as a code.
Datatype: "InvestmentFundTransactionType1Code" on page 5325
CodeName Name Definition
ALLL All All types of transactions.
SELL SecuritiesSale Sale of securities.
BUYI SecuritiesPurchase Purchase of securities.
SWIO SwitchOut Transaction is a subscription leg of a
switch order execution.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5165 May 2026
```

## File page 5166

```text
CodeName Name Definition
TRIN TransferIn Transaction is an incoming credit to an
account on the shareholders register,
and is not linked to a shift in investment
(subscription or switch), but to account
management.
TOUT TransferOut Transaction is a debit to an account on
the shareholders register, and is not
linked to a shift in investment
(redemption or switch), but to account
management.
SUBS Subscription Transaction is a subscription to an
investment fund.
REDM Redemption Transaction is a redemption of an
investment fund.
CDEP CashDeposit Transaction is a cash deposit.
CWIT CashWithdrawal Transaction is a cash withdrawal.
DIVP DividendPayment Transaction is the payment of dividends
and other proceeds.
CAEV CorporationActionEvent Transaction is the result of a corporate
action.
CROI CrossIn Transaction is a cross-in.
CROO CrossOut Transaction is a cross out.
DIVI Dividend Transaction is a dividend.
INSP InSpecie Transaction is an InSpecie.
OTHR Other Transaction is another type of
transaction.
REAA RedemptionAssetAllocation Transaction is a redemption in an asset
allocation plan which enables investors
to withdraw, by percentage a certain
amount of cash from several sub-funds
of a same umbrella structure.
RWPL RedemptionWithdrawingPlan Transaction is a withdrawal by
individuals in the framework of a
structured plan for investments made in
the past.
RDIV ReinvestmentOfDividend Transaction is a reinvestment of
dividend.
SSPL SubscriptionSavingsPlan Transaction is a subscription for a
savings plan, that is, money set aside by
individuals in the framework of a
structured plan for a special purpose, for
example, retirement.
SUAA SubscriptionAssetAllocation Transaction is a subscription in an asset
allocation plan that enables investors to
allocate, by percentage a certain amount
of cash into several sub-funds of a same
umbrella structure.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5166 May 2026
```

