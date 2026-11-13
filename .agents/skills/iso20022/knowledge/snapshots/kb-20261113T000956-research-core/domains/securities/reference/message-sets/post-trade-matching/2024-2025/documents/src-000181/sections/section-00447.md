---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.5 PriceInformation28"]
file_pages: [513]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.5 PriceInformation28

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 513 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 513

```text
CodeName Name Definition
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
VACT VariableCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
PRCT Percentage Price expressed as a percentage of par.
ACTU ActualAmount Price expressed as a currency and
amount per unit or per share.
7.1.22.5  PriceInformation28
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 513
   QuotationDate <QtnDt> [0..1] ± 514
   PriceCalculationPeriod <PricClctnPrd> [0..1]  514
{Or     FromDateTime <FrDtTm> [1..1] DateTime 514
Or     ToDateTime <ToDtTm> [1..1] DateTime 514
Or}     DateTimeRange <DtTmRg> [1..1] ± 514
   SourceOfPrice <SrcOfPric> [0..1] ± C16,
C23,
C33
515
7.1.22.5.1  Value <Val>
Presence: [1..1]
Definition: Value of the price, for instance, as a currency and value.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 513 February 2025
```

