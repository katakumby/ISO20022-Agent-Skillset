---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.1 Future <Futr>", "32.4.3.1.1.2.4.1.5 UnitOfMeasure <UnitOfMeasr>", "32.4.3.1.1.2.4.1.5.2 Proprietary <Prtry>"]
file_pages: [1915]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.1.5.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1915 to 1915.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1915

```text
CodeName Name Definition
SMIL SquareMillimetre Measure of a surface, one millimetre by
one millimetre.
SQYA SquareYard Measure of a surface, one yard by one
yard.
USBA USBarrel Unit of volume equal to 158, 9873 litre.
USFO USFluidOunce Unit of volume equal to 2, 957353
centilitre.
USGA USGallon Unit of volume that is equal to 8 pints.
USPI USPint Unit of volume that is equal to 473 cubic
centimetres.
USQA USQuart Unit of volume that is equal to 2 pints.
USTN USTon Measure of weight, in the US 2000 lb
(short ton).
YARD Yard Unit of length equal to 3 feet or 0.9144
metre.
GBOU GBOunce Unit of weight equal to a sixteenth of a
pound.
ACRE Acre Unit of measure equal to 4, 840 square
yards.
ARES Are Unit of measure equal to a 100 square
meters.
HECT Hectare Unit of measure that is equal to 10, 000
square meters.
32.4.3.1.1.2.4.1.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unit of measure expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.2.4.1.6  TimeUnit <TmUnit>
Presence: [0..1]
Definition: Used to indicate a time unit for the contract (for example days, weeks, months, etc.).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1915 August 2026
```

