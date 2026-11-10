---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.23 Price", "82.1.23.5 PriceInformation20", "82.1.23.5.2 Value <Val>"]
file_pages: [3105]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.23.5.2 Value <Val>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3105 to 3105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3105

```text
82.1.23.5.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmountOrUnknown2Choice" on
page 3107 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3107
Or   Amount <Amt> [1..1] Amount C1 3107
Or}   UnknownIndicator <UknwnInd> [1..1] Indicator 3107
82.1.23.5.3  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
ValueType <ValTp> contains one of the following elements (see "YieldedOrValueType1Choice" on
page 3025 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 3025
Or}   ValueType <ValTp> [1..1] CodeSet 3025
82.1.23.5.4  SourceOfPrice <SrcOfPric>
Presence: [0..1]
Definition: Place from which the price was obtained.
SourceOfPrice <SrcOfPric> contains the following elements (see "MarketIdentification89" on
page 2969 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2969
   Type <Tp> [1..1]  2970
{Or     Code <Cd> [1..1] CodeSet 2970
Or}     Proprietary <Prtry> [1..1] ± 2970
82.1.23.5.5  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date on which the price is obtained. With an investment fund, this is as stated in the
prospectus.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3105 August 2026
```

