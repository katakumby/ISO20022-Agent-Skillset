---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.11 ModificationScope41", "66.1.26.11.2 InvestmentPlan <InvstmtPlan>", "66.1.26.11.2.6 IncomePreference <IncmPref>"]
file_pages: [4747]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.11.2.6 IncomePreference <IncmPref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4747 to 4747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4747

```text
66.1.26.11.2.6  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference2Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
SECU Securities Distribution in securities.
66.1.26.11.2.7  InitialAmount <InitlAmt>
Presence: [0..1]
Definition: Initial amount or number of initial instalments.
InitialAmount <InitlAmt> contains one of the following elements (see "InitialAmount1Choice" on
page 4344 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InitialNumberOfInstalments <InitlNbOfInstlmts> [1..1] Quantity 4344
Or}   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.26.11.2.8  TotalNumberOfInstalments <TtlNbOfInstlmts>
Presence: [0..1]
Definition: Total number of times the amount must be invested at the predefined frequency as of the
start date of the investment plan.
Datatype: "Number" on page 5400
66.1.26.11.2.9  RoundingDirection <RndgDrctn>
Presence: [0..1]
Definition: Indicates the rounding direction when an amount is to be spread over several funds.
Datatype: "RoundingDirection1Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
STAN RoundToNearest Round up or down to the nearest whole
number.
DIST IssueFraction Do not round.
66.1.26.11.2.10  SecurityDetails <SctyDtls>
Presence: [1..50]
Definition: Security that an investment plan invests in, or from which the investment plan divests.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4747 May 2026
```

