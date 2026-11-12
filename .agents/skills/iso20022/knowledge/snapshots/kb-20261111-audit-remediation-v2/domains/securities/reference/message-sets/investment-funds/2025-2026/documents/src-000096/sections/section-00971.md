---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.8 CurrentYearSubscriptionDetails <CurYrSbcptDtls>", "38.4.15.4.1.8.4 TotalAmountYearToDate <TtlAmtYrToDt>"]
file_pages: [1351]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.8.4 TotalAmountYearToDate <TtlAmtYrToDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1351 to 1351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1351

```text
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
38.4.15.4.1.8.4  TotalAmountYearToDate <TtlAmtYrToDt>
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
38.4.15.4.1.9  BonusOrWithdrawal <BnsOrWdrwl>
Presence: [0..*]
Definition: Bonus paid out or withdrawn.
BonusOrWithdrawal <BnsOrWdrwl> contains the following BonusWithdrawal2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TypeOfAmount <TpOfAmt> [1..1]  1352
{Or     Code <Cd> [1..1] CodeSet 1352
Or}     Proprietary <Prtry> [1..1] ± 1352
   Amount <Amt> [0..1] Amount C2 1352
   Reason <Rsn> [0..1]  1353
{Or     Code <Cd> [1..1] CodeSet 1353
Or}     Proprietary <Prtry> [1..1] ± 1353
   UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1353
   Outstanding <Outsdng> [0..1] Indicator 1354
   Reference <Ref> [0..1] Text 1354
   AdditionalInformation <AddtlInf> [0..*] ± 1354
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1351 May 2026
```

