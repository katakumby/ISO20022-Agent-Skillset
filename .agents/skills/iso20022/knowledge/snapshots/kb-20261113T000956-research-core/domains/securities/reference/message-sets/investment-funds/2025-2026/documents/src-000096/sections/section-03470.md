---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.1 TransactionType <TxTp>"]
file_pages: [4719]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.1 TransactionType <TxTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4719 to 4719.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4719

```text
Constraints
• TransactionTypeLegExecutionIdentificationRule
If TransactionType is SWII or SWIO, then LegExecutionIdentification is optional. If TransactionType
is neither SWII nor SWIO, then LegExecutionIdentification is not allowed.
• TransactionTypeLegIdentificationRule
If TransactionType is SWII or SWIO, then LegIdentification is optional. If TransactionType is neither
SWII nor SWIO, then LegIdentification is not allowed.
66.1.26.3.1  TransactionType <TxTp>
Presence: [1..1]
Warning   Either TransactionType or ExtendedTransactionType or CorporateActionEventType or
ExtendedCorporateActionEventType must be present but not more than one.
Definition: Type of investment fund transaction.
Datatype: "TransactionType2Code" on page 5378
CodeName Name Definition
REDM Redemption Transaction is a redemption of an
investment fund.
SUBS Subscription Transaction is a subscription to an
investment fund.
SSPL SubscriptionSavingsPlan Transaction is a subscription for a
savings plan, that is, money set aside by
individuals in the framework of a
structured plan for a special purpose, for
example, retirement.
RWPL RedemptionWithdrawingPlan Transaction is a withdrawal by
individuals in the framework of a
structured plan for investments made in
the past.
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
SWII SwitchIn Transaction is a subscription leg of a
switch order execution.
SWIO SwitchOut Transaction is a subscription leg of a
switch order execution.
SUAA SubscriptionAssetAllocation Transaction is a subscription in an asset
allocation plan that enables investors to
allocate, by percentage a certain amount
of cash into several sub-funds of a same
umbrella structure.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4719 May 2026
```

