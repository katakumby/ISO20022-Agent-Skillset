---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.1 CashSettlement4", "66.1.42.1.2 CashAccountDetails <CshAcctDtls>", "66.1.42.1.2.9 SettlementInstructionReason <SttlmInstrRsn>", "66.1.42.1.2.9.1 Code <Cd>"]
file_pages: [5151]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.1.2.9.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5151 to 5151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5151

```text
SettlementInstructionReason <SttlmInstrRsn> contains one of the following
SettlementInstructionReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5151
Or}   Proprietary <Prtry> [1..1] ± 5151
66.1.42.1.2.9.1  Code <Cd>
Presence: [1..1]
Definition: Settlement instruction reason expressed as a code.
Datatype: "SettlementInstructionReason1Code" on page 5362
CodeName Name Definition
CSHI AllCredits Settlement of all credit amounts.
ALLL AllCreditsAndDebits Settlement of all credit and debit
amounts.
CSHO AllDebits Settlement of all debit amounts.
CHAR Charges Settlement of charges.
DIVI Dividend Settlement of dividends.
INTE Interest Settlement of interest.
SAVP InvestmentSavingsPlan Settlement of investments to a savings
plan.
REDM Redemption Settlement of redemptions or redemption
legs of a switch transaction.
SAVE SavingsPlan Settlement of investments to a savings
plan and withdrawals from a savings
plan.
BUYI SecuritiesPurchase Settlement of securities purchases.
SELL SecuritiesSale Settlement of securities sales.
SUBS Subscription Settlement of subscriptions or
subscription legs of a switch transaction.
WTHP WithdrawalSavingsPlan Settlement of withdrawals from a savings
plan.
CORP CorporateAction Settlement of corporate actions.
66.1.42.1.2.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement instruction reason expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5151 May 2026
```

