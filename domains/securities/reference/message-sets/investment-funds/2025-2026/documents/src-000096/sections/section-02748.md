---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.13 InterimProfitAmount <IntrmPrftAmt>"]
file_pages: [3877]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.13 InterimProfitAmount <IntrmPrftAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3877 to 3877.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3877

```text
• Meaning When True: Yes
• Meaning When False: No
55.4.5.19.13  InterimProfitAmount <IntrmPrftAmt>
Presence: [0..1]
Definition: Part of the price deemed as accrued income or profit rather than capital. The interim profit
amount is used for tax purposes.
InterimProfitAmount <IntrmPrftAmt> contains one of the following elements (see
"ProfitAndLoss2Choice" on page 5116 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Profit <Prft> [1..1] Amount C1, C13 5116
Or}   Loss <Loss> [1..1] Amount C1, C13 5116
55.4.5.19.14  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
55.4.5.19.15  Group1Or2Units <Grp1Or2Units>
Presence: [0..1]
Definition: Tax group to which the purchased investment fund units belong. The investor indicates to the
intermediary operating pooled nominees, which type of unit is to be sold.
Datatype: "UKTaxGroupUnit1Code" on page 5387
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
55.4.5.19.16  RequestedSettlementCurrency <ReqdSttlmCcy>
Presence: [0..1]
Definition: Currency requested for settlement of cash proceeds.
Impacted by: C2 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3877 May 2026
```

