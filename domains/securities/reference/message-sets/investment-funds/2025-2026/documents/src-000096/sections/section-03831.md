---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.7 PriceInformation2", "66.1.34.7.4 ExtendedType <XtndedTp>"]
file_pages: [5120]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.7.4 ExtendedType <XtndedTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5120 to 5120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5120

```text
CodeName Name Definition
redemptions, as an alternative to dilution
levy.
MIDD Mid Price is the average price between the
bid and offer prices.
RINV Reinvestment Price is the price used when reinvesting
units after distribution.
SWIC Switch Price is the price used when transferring
units between products.
MRKT Market Price is the current market price.
INDC Indicative Price is the estimated indicative price.
66.1.34.7.4  ExtendedType <XtndedTp>
Presence: [1..1]
Warning   Either Type or ExtendedType must be present, but not both.
Definition: Type and information about a price.
Datatype: "Extended350Code" on page 5402
66.1.34.7.5  SourceOfPrice <SrcOfPric>
Presence: [0..1]
Definition: Place from which the price was obtained.
SourceOfPrice <SrcOfPric> contains one of the following PriceSourceFormatChoice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   LocalMarketPlace <LclMktPlc> [1..1] IdentifierSet 5120
Or   NonLocalMarketPlace <NonLclMktPlc> [1..1] ± 5120
Or}   PlaceAsDSS <PlcAsDSS> [1..1] ± 5121
66.1.34.7.5.1  LocalMarketPlace <LclMktPlc>
Presence: [1..1]
Definition: Source of price quotation is the market, expressed as a Market Identifier Code (MIC).
Datatype: "MICIdentifier" on page 5396
66.1.34.7.5.2  NonLocalMarketPlace <NonLclMktPlc>
Presence: [1..1]
Definition: Source of a price quotation when it is not the local market.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5120 May 2026
```

