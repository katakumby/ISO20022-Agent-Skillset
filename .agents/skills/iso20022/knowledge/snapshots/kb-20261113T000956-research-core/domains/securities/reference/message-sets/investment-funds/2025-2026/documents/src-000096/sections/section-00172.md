---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.1 PriceType <PricTp>"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.1 PriceType <PricTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
Constraints
• CalculationBasisRule
If Type is not NonAdjustedUnpublished, then CalculationBasis is not allowed. If Type is
NonAdjustedUnpublished, then CalculationBasis may be present.
14.4.10.1.14.1  PriceType <PricTp>
Presence: [1..1]
Definition: Type and information about a price.
Impacted by: C18 "OtherCodeRule"
PriceType <PricTp> contains one of the following PriceType6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 258
Or}   Proprietary <Prtry> [1..1] Text 259
Constraints
• OtherCodeRule
If Structured is OTHR, then AdditionalInformation is mandatory.
14.4.10.1.14.1.1  Code <Cd>
Presence: [1..1]
Definition: Type and information about a price expressed as an ISO 20022 code.
Datatype: "TypeOfPrice9Code" on page 5386
CodeName Name Definition
BIDE Bid Price is the calculated bid price of a
dual-priced fund (offer-bid prices), that
is, the selling price of the units for the
investor.
OFFR Offer Price is the calculated offer price of a
dual-priced investment fund (offer-bid
prices), that is, the buying price of the
units for an investor.
NAVL NetAssetValue Price is the net asset value per unit that
is used either as a transacting price for a
single-priced investment fund class, or
as a notional price for the calculation of
other prices.
CREA Creation Price is the calculated creation price of a
dual-priced investment fund (creation-
cancellation prices) and the highest
possible buying price of the units before
the initial charge. The actual buying or
offer price, which includes charges, will
be higher.
CANC Cancellation Price is the calculated cancellation price
of a dual-priced investment fund
(creation-cancellation price), and the
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 258 May 2026
```

