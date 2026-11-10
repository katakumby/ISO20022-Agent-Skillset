---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.34 PreferenceToIncome1Code"]
file_pages: [521]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.34 PreferenceToIncome1Code

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 521 to 521.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 521

```text
CodeName Name Definition
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
13.2.2.34  PreferenceToIncome1Code
Definition: Indicates the level of priority to claim on income and assets of
the company in case of the payment of dividends and in the event of a bankruptcy, eg, ordinary/
common stocks, preferred stocks, subordinated debt, etc.
Type: CodeSet
CodeName Name Definition
ORDN Ordinary Indicates an ordinary/common
preference to income.
PFRD Preferred Indicates a preferred claim upon income
and assets.
13.2.2.35  PriceValueType3Code
Definition: Specifies a type of value of the price.
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
PARV Par Price is the face amount.
YIEL Yield Price expressed as a yield.
SPRE Spread Difference between a market maker's bid
and asked price.
PEUN PerUnit Price expressed per unit.
ABSO Absolute Price is expressed as absolute.
TEDP TEDPrice Price is expressed as Treasury Euro
Dollar price.
TEDY TEDYield Price is expressed as Treasury Euro
Dollar yield.
FICT FixedCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 521 March 2024
```

