---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.20 MaximumSubstitution <MaxSbstitn>"]
file_pages: [101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.20 MaximumSubstitution <MaxSbstitn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 101 to 101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 101

```text
MinimumDenomination <MinDnmtn> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
3.4.8.20  MaximumSubstitution <MaxSbstitn>
Presence: [0..1]
Definition: Maximum number of time the collateral can be substitute.
Datatype: "Number" on page 666
3.4.8.21  MinimumIncrement <MinIncrmt>
Presence: [0..1]
Definition: Indicates the minimum tradable increments of a security.
MinimumIncrement <MinIncrmt> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
3.4.8.22  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Indicates the periodic or regular cycle of interest payments.
Datatype: "Frequency1Code" on page 627
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 101 February 2025
```

