---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.7 PriceInformation2", "66.1.34.7.5 SourceOfPrice <SrcOfPric>", "66.1.34.7.5.3 PlaceAsDSS <PlcAsDSS>"]
file_pages: [5121]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.7.5.3 PlaceAsDSS <PlcAsDSS>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5121 to 5121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5121

```text
NonLocalMarketPlace <NonLclMktPlc> contains the following elements (see "PriceSource" on
page 5121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceSource <PricSrc> [1..1] CodeSet 5122
   Narrative <Nrrtv> [0..1] Text 5122
66.1.34.7.5.3  PlaceAsDSS <PlcAsDSS>
Presence: [1..1]
Definition: Source of a price quotation expressed with a propriety identification scheme.
PlaceAsDSS <PlcAsDSS> contains the following elements (see "GenericIdentification5" on page 4549
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4549
   Information <Inf> [1..1] Text 4549
   Narrative <Nrrtv> [0..1] Text 4549
66.1.34.7.6  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date on which the price is obtained. With an investment fund, this is as stated in the
prospectus.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTimeChoice" on
page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.34.7.7  Yielded <Yldd>
Presence: [0..1]
Definition: Indicates whether the price is expressed as a yield. The absence of Yielded means it is not
applicable.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.34.8  PriceSource
Definition: Source of a price quotation when it is not the local market.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5121 May 2026
```

