---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.4 AggregateBalancePerSafekeepingPlace4", "66.1.5.4.9 PriceDetails <PricDtls>"]
file_pages: [4366]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.4.9 PriceDetails <PricDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4366 to 4366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4366

```text
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormatChoice" on page 5133 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  C13 5133
     PlaceSafekeeping <PlcSfkpg> [1..1] CodeSet 5134
     Narrative <Nrrtv> [0..1] Text 5134
     Party <Pty> [0..1] ± 5134
Or   IdentificationAsDSS <IdAsDSS> [1..1] ± 5135
Or}   IdentificationAsCountry <IdAsCtry> [1..1] CodeSet C12 5135
66.1.5.4.9  PriceDetails <PricDtls>
Presence: [1..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C15 "ValueRule"
PriceDetails <PricDtls> contains the following elements (see "PriceInformation2" on page 5118 for
details)
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
66.1.5.4.10  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Currency exchange related to a securities order.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4366 May 2026
```

