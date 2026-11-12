---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.8 PriceSource", "66.1.34.8.1 PriceSource <PricSrc>"]
file_pages: [5122]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.8.1 PriceSource <PricSrc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5122 to 5122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5122

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceSource <PricSrc> [1..1] CodeSet 5122
   Narrative <Nrrtv> [0..1] Text 5122
66.1.34.8.1  PriceSource <PricSrc>
Presence: [1..1]
Definition: Source of the price.
Datatype: "PriceSource1Code" on page 5344
CodeName Name Definition
FUND Fund Source of price quotation is a fund, eg,
transfer agent, fund itself.
THEO Theoretical Source of price quotation is a theoretical
value based on the market yield.
VEND Vendor Source of price quotation is an external
vendor.
66.1.34.8.2  Narrative <Nrrtv>
Presence: [0..1]
Definition: Additional information about the source of a price.
Datatype: "Max35Text" on page 5403
66.1.34.9  ValuationDealingProcessingCharacteristics3
Definition: Valuation dealing processing characteristics linked to the instrument, that is, not to the
market.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValuationFrequency <ValtnFrqcy> [0..1] CodeSet 5122
   ValuationFrequencyDescription <ValtnFrqcyDesc> [0..1] Text 5123
   ValuationTime <ValtnTm> [0..1] Time 5123
   DecimalisationUnits <DcmlstnUnits> [0..1] Quantity 5123
   DecimalisationPrice <DcmlstnPric> [0..1] Quantity 5123
   DualFundIndicator <DualFndInd> [0..1] Indicator 5123
   PriceMethod <PricMtd> [0..1] CodeSet 5124
   PriceCurrency <PricCcy> [0..*] CodeSet C1 5124
   AdditionalInformation <AddtlInf> [0..*] ± 5124
66.1.34.9.1  ValuationFrequency <ValtnFrqcy>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5122 May 2026
```

