---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.23 MinimumQuantity <MinQty>"]
file_pages: [102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.23 MinimumQuantity <MinQty>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 102 to 102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 102

```text
CodeName Name Definition
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
3.4.8.23  MinimumQuantity <MinQty>
Presence: [0..1]
Definition: Indicates the minimum tradable quantity of a security.
MinimumQuantity <MinQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
3.4.8.24  Production <Pdctn>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond, particularly an MBS, issued in
a particular year.
Datatype: "Max35Text" on page 669
3.4.8.25  RestrictedIndicator <RstrctdInd>
Presence: [0..1]
Definition: Identifies if the securities is restricted or not (as per Rule 144).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.8.26  PriceFrequency <PricFrqcy>
Presence: [0..1]
Definition: Indicates the frequency at which the bond is re-rated and therefore re-priced (bond attribute,
particularly of floating rate and index linked instruments).
Datatype: "Frequency1Code" on page 627
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 102 February 2025
```

