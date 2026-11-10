---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.236 TransferInFunction1Code"]
file_pages: [5379]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.236 TransferInFunction1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5379 to 5379.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5379

```text
CodeName Name Definition
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
REAA RedemptionAssetAllocation Transaction is a redemption in an asset
allocation plan which enables investors
to withdraw, by percentage a certain
amount of cash from several sub-funds
of a same umbrella structure.
66.2.2.236  TransferInFunction1Code
Definition: Specifies the function of the transfer in.
Type: CodeSet
CodeName Name Definition
ADRE AdviceAndRequest The transfer-in is an advice and request,
that is, the message is used to inform
the receiver to expect an unsolicited
transfer in confirmation and to request
account information for the transfer.
INST Instruction The transfer-in is an instruction.
66.2.2.237  TransferInFunction2Code
Definition: Specifies the function of the transfer in confirmation.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5379 May 2026
```

