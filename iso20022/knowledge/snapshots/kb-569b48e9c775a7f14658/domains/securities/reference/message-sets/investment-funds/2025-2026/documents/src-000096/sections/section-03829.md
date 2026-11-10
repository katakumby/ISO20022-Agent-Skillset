---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.7 PriceInformation2"]
file_pages: [5118]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.7 PriceInformation2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5118 to 5118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5118

```text
• Meaning When True: Yes
• Meaning When False: No
66.1.34.7  PriceInformation2
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 5118
   ValueType <ValTp> [0..1] CodeSet 5118
{Or   Type <Tp> [1..1] CodeSet 5119
Or}   ExtendedType <XtndedTp> [1..1] Text 5120
   SourceOfPrice <SrcOfPric> [0..1]  5120
{Or     LocalMarketPlace <LclMktPlc> [1..1] IdentifierSet 5120
Or     NonLocalMarketPlace <NonLclMktPlc> [1..1] ± 5120
Or}     PlaceAsDSS <PlcAsDSS> [1..1] ± 5121
   QuotationDate <QtnDt> [0..1] ± 5121
   Yielded <Yldd> [0..1] Indicator 5121
Constraints
• ValueRule
If Type is not MRKT, then Value may not be expressed with UnknownIndicator.
66.1.34.7.1  Value <Val>
Presence: [1..1]
Definition: Value of the price, eg, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmountOrUnknownChoice" on
page 5117 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 5117
Or   Amount <Amt> [1..1] Amount C2 5117
Or}   UnknownIndicator <UknwnInd> [1..1] Indicator 5117
66.1.34.7.2  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType2Code" on page 5344
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5118 May 2026
```

