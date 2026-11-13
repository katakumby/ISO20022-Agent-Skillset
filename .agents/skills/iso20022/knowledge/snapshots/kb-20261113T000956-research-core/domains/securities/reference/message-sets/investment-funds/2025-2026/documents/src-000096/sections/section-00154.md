---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.16 PerformanceDetails <PrfrmncDtls>", "13.4.9.16.2 CumulativeCorporateActionFactor <CmltvCorpActnFctr>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.16.2 CumulativeCorporateActionFactor <CmltvCorpActnFctr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
Definition: Value of the NAV before all corporate events of the valuation date, divided by the value of
the NAV after the corporate event.
Datatype: "DecimalNumber" on page 5400
13.4.9.16.2  CumulativeCorporateActionFactor <CmltvCorpActnFctr>
Presence: [0..1]
Definition: Value of the NAV before a corporate event, divided by the value of the NAV after the
corporate event, accumulated for a number of corporate events over the defined period of time.
Datatype: "DecimalNumber" on page 5400
13.4.9.16.3  AccumulationPeriod <AcmltnPrd>
Presence: [0..1]
Definition: Period of time for the calculation of the cumulative corporate action factor.
AccumulationPeriod <AcmltnPrd> contains the following elements (see "DatePeriod2" on page 4464
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 4464
   ToDate <ToDt> [1..1] Date 4464
13.4.9.16.4  NormalPerformance <NrmlPrfrmnc>
Presence: [0..1]
Definition: Normal performance value of the NAV.
Datatype: "DecimalNumber" on page 5400
13.4.10 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C14 "ExtensionRule"
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
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 221 May 2026
```

