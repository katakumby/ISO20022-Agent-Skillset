---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.107 PriceRateType3Code"]
file_pages: [1231]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.107 PriceRateType3Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1231 to 1231.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1231

```text
CodeName Name Definition
NAVF FinalAssetValue Final asset value at the liquidation of the
fund.
MIMP MidMarketPrice Price at a certain amount of time prior to
the date it is announced.
NAVA NetAssetValue Net value of an investment fund's assets
less its liabilities, divided by the number
of shares outstanding.
AVCL AverageClosingPrice Price of the asset at close of a given
day.
16.2.2.107  PriceRateType3Code
Definition: Specifies the type of price rate.
Type: CodeSet
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PRCT Percentage Price expressed as a percentage of par.
YIEL Yield Price expressed as a yield.
16.2.2.108  PriceValueType10Code
Definition: Specifies the value of a price.
Type: CodeSet
CodeName Name Definition
UKWN Unknown Price is unknown by the sender or has
not been established.
16.2.2.109  PriceValueType8Code
Definition: Specifies a type of price value.
Type: CodeSet
CodeName Name Definition
TBSP ToBeSpecified Price to be specified by account owner.
UNSP Unspecified Price is not required to be specified by
account owner.
UKWN Unknown Price is unknown by the sender or has
not been established.
NILP NilPayment Price will not be paid.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1231 February 2026
```

