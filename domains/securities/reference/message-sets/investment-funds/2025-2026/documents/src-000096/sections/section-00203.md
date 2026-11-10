---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.16 PerformanceDetails <PrfrmncDtls>", "14.4.10.1.16.2 CumulativeCorporateActionFactor <CmltvCorpActnFctr>"]
file_pages: [290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.16.2 CumulativeCorporateActionFactor <CmltvCorpActnFctr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 290 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 290

```text
Datatype: "DecimalNumber" on page 5400
14.4.10.1.16.2  CumulativeCorporateActionFactor <CmltvCorpActnFctr>
Presence: [0..1]
Definition: Value of the NAV before a corporate event, divided by the value of the NAV after the
corporate event, accumulated for a number of corporate events over the defined period of time.
Datatype: "DecimalNumber" on page 5400
14.4.10.1.16.3  AccumulationPeriod <AcmltnPrd>
Presence: [0..1]
Definition: Period of time for the calculation of the cumulative corporate action factor.
AccumulationPeriod <AcmltnPrd> contains the following elements (see "DatePeriod2" on page 4464
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 4464
   ToDate <ToDt> [1..1] Date 4464
14.4.10.1.16.4  NormalPerformance <NrmlPrfrmnc>
Presence: [0..1]
Definition: Normal performance value of the NAV.
Datatype: "DecimalNumber" on page 5400
14.4.11 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C16 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 290 May 2026
```

