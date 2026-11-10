---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.31 InvestmentPlan17", "66.1.26.31.6 IncomePreference <IncmPref>"]
file_pages: [4794]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.31.6 IncomePreference <IncmPref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4794 to 4794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4794

```text
Definition: Indicates whether an ordered amount is a gross amount (including transaction overhead). If it
is not a gross amount, the ordered amount is a net amount (amount to be invested or redeemed from
the fund to which other elements will be added).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.31.6  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference2Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
SECU Securities Distribution in securities.
66.1.26.31.7  InitialAmount <InitlAmt>
Presence: [0..1]
Definition: Initial amount or number of initial instalments.
InitialAmount <InitlAmt> contains one of the following elements (see "InitialAmount1Choice" on
page 4344 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InitialNumberOfInstalments <InitlNbOfInstlmts> [1..1] Quantity 4344
Or}   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.26.31.8  TotalNumberOfInstalments <TtlNbOfInstlmts>
Presence: [0..1]
Definition: Total number of times the amount must be invested at the predefined frequency as of the
start date of the investment plan.
Datatype: "Number" on page 5400
66.1.26.31.9  RoundingDirection <RndgDrctn>
Presence: [0..1]
Definition: Indicates the rounding direction when an amount is to be spread over several funds.
Datatype: "RoundingDirection1Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4794 May 2026
```

