---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.2 OtherPrices5", "7.1.22.2.15 ReferencePrice <RefPric>"]
file_pages: [511]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.2.15 ReferencePrice <RefPric>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 511 to 511.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 511

```text
Definition: Price used to differentiate from price on a confirmation of a marked up or marked down
principal trade.
ReportedPrice <RptdPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.15  ReferencePrice <RefPric>
Presence: [0..1]
Definition: Price of reference of the concerned financial instrument.
ReferencePrice <RefPric> contains the following elements (see "PriceInformation28" on page 513 for
details)
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
7.1.22.3  PriceRateOrAmount3Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 511
Or}   Amount <Amt> [1..1] Amount C2 511
7.1.22.3.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Datatype: "PercentageRate" on page 667
7.1.22.3.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 511 February 2025
```

