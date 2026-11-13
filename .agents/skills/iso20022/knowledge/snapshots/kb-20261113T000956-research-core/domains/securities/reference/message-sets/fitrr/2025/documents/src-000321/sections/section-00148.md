---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "11.4 Message Building Blocks", "11.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "11.4.2.7 AggregatedQuantitativeData <AggtdQttvData>", "11.4.2.7.3 Range <Rg>", "11.4.2.7.3.1 FromQuantity <FrQty>"]
file_pages: [183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.041.001.01"]
---

# 11.4.2.7.3.1 FromQuantity <FrQty>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 183 to 183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 183

```text
Range <Rg> contains the following FromToQuantityRange2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromQuantity <FrQty> [1..1] Quantity 183
   ToQuantity <ToQty> [1..1] Quantity 183
11.4.2.7.3.1  FromQuantity <FrQty>
Presence: [1..1]
Definition: Lower boundary of a range of quantity values.
Datatype: "DecimalNumber" on page 451
11.4.2.7.3.2  ToQuantity <ToQty>
Presence: [1..1]
Definition: Upper boundary of a range of quantity values.
Datatype: "DecimalNumber" on page 451
11.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C2 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.041.001.01
FinancialInstrumentReportingNonEquityTradingActi
vityReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
183 July 2025
```

