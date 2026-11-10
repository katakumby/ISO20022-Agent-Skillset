---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.1 Future <Futr>", "32.4.3.1.1.2.4.1.5 UnitOfMeasure <UnitOfMeasr>"]
file_pages: [1913, 1914]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.1.5 UnitOfMeasure <UnitOfMeasr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1913 to 1914.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1913

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
32.4.3.1.1.2.4.1.5  UnitOfMeasure <UnitOfMeasr>
Presence: [0..1]
Definition: Used to indicate the measurement unit of the underlying commodity on which the contract is
based (for example, 2500 lbs of lean cattle, 1000 barrels of crude oil, 1000 bushels of corn, etc.).
UnitOfMeasure <UnitOfMeasr> contains one of the following UnitOfMeasure7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1913
Or}   Proprietary <Prtry> [1..1] ± 1915
32.4.3.1.1.2.4.1.5.1  Code <Cd>
Presence: [1..1]
Definition: Unit of measure expressed as an ISO 20022 code.
Datatype: "UnitOfMeasure9Code" on page 3315
CodeName Name Definition
BAGG Bag Code for a bag.
BALE Bale Code for a bale.
BOTL Bottle Code for a bottle.
BOXX Box Code for a box.
CRTN Carton Code for a carton.
CELI Centilitre Unit of volume that is equal to one
hundredth of a litre.
CMET Centimetre Unit of measure that is equal to one
hundredth of a metre.
CNTR Container Code for a container.
CRAT Crate Code for a crate.
CBIN CubicInch Measure of a volume, one inch by one
inch by one inch.
CBME CubicMeters Unit of volume that is equal to one meter
in length, breadth and height or also
equal to 1000 liters.
CBML CubicMillimetre Unit of volume that is equal to one
thousandth of a litre.
PIEC Piece Standard length of cloth, wallpaper, as
an item for sale or amount of a
substance.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1913 August 2026
```

## File page 1914

```text
CodeName Name Definition
FOOT Foot Unit of length equal to 1/3 yard.
GBFO GBFuildOunce Unit of volume equal to 2, 841 306
centilitre.
GBGA GBGallon Unit of volume that is equal to 8 pints.
GBPI GBPint Unit of volume that is equal to 568 cubic
centimetres.
GBQA GBQuart Unit of volume that is equal to 2 pints.
GBTN GBTon Measure of weight, in Britain 2240 lb
(long ton).
GRAM Gram Unit of measure that is equal to a 1,
000th of a kilo.
INCH Inch Measure of length equal to 2.54 cm.
KILO Kilogram Basic unit of mass in the SI system,
1000 grams.
KMET Kilometre Unit of measure that is equal to 1, 000
meters.
LITR Litre Unit of volume that is equal to a
thousand cubic centimetres.
METR Metre Unit of length in the metric system, equal
to 39.37 inches.
TONE MetricTons Unit of mass equal to 1000 kilograms;
equivalent to approximately 2,204.6
pounds, 1.102 short tons (US) or 0.984
long tons (imperial).
MILE Mile Unit of length equal to 1, 760 yards.
MMET Millimetre Unit of measure that is a thousandth of
one metre.
MILI MilliLitre Unit of volume that is equal to one
thousandth of a litre.
PUND Pound Unit of weight equal to 0.454 kilograms.
USOU USOunce Unit of weight equal to a sixteenth of a
pound.
SCMT SquareCentimetre Measure of a surface, one centimetre by
one centimetre.
SQFO SquareFoot Measure of a surface, one foot by one
foot.
SQIN SquareInch Measure of a surface, one inch by one
inch.
SQKI SquareKilometre Measure of a surface, one kilometre by
one kilometre.
SMET SquareMetre Measure of a surface, one metre by one
metre.
SQMI SquareMile Measure of a surface, one mile by one
mile.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1914 August 2026
```

