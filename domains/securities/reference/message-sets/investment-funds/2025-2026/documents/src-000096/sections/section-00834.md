---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "36.4.15.5.1.8 CurrentYearSubscriptionDetails <CurYrSbcptDtls>", "36.4.15.5.1.8.4 TotalAmountYearToDate <TtlAmtYrToDt>"]
file_pages: [1159]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1.8.4 TotalAmountYearToDate <TtlAmtYrToDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1159 to 1159.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1159

```text
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
36.4.15.5.1.8.4  TotalAmountYearToDate <TtlAmtYrToDt>
Presence: [1..1]
Definition: Total amount subscribed in the current tax year.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
36.4.15.5.1.9  BonusOrWithdrawal <BnsOrWdrwl>
Presence: [0..*]
Definition: Bonus paid out or withdrawn.
BonusOrWithdrawal <BnsOrWdrwl> contains the following BonusWithdrawal2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TypeOfAmount <TpOfAmt> [1..1]  1160
{Or     Code <Cd> [1..1] CodeSet 1160
Or}     Proprietary <Prtry> [1..1] ± 1160
   Amount <Amt> [0..1] Amount C2 1160
   Reason <Rsn> [0..1]  1161
{Or     Code <Cd> [1..1] CodeSet 1161
Or}     Proprietary <Prtry> [1..1] ± 1161
   UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1161
   Outstanding <Outsdng> [0..1] Indicator 1162
   Reference <Ref> [0..1] Text 1162
   AdditionalInformation <AddtlInf> [0..*] ± 1162
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1159 May 2026
```

