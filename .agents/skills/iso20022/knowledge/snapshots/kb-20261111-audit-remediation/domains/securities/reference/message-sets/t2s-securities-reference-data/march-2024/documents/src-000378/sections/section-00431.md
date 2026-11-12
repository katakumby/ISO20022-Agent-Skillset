---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.49 TypeOfPrice1Code"]
file_pages: [526, 527, 528]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.49 TypeOfPrice1Code

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 526 to 528.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 526

```text
13.2.2.49  TypeOfPrice1Code
Definition: Specifies the type of price and information about the price.
Type: CodeSet
CodeName Name Definition
AVER Average Price is an average execution price.
AVOV AverageOverride Price is an override of the average price.
COMB Combined Price is composed of the combined
expenses (used in the UK market).
GREX GrossOfAll Price is a gross execution price. The
price is an all inclusive price, ie,
including all charges, fees, and taxes.
LIMI Limit Price is the limit price of a limit order, eg,
a customer might put in a limit order to
sell financial instruments at 67 or to buy
at 60.
NET2 Net Price is a net price, ie, net only of local
broker's commission, local fees and local
taxes.
NDIS NetDisclosed Price is net to the disclosed client.
NET1 NetOfAll Price is a net price, ie, net of all charges,
fees and taxes.
NUND NetUndisclosed Price is net to the client undisclosed
(used in the UK market).
NOGR NotionalGross Price is notional gross (used in the UK
market).
PARV ParValue Price is equal to the nominal or face
value of the instrument.
RDAV RoundedAverage Price is a rounded average price.
STOP Stop Price is a stop price used in an order to
buy. The order becomes a market order
when the financial instrument trades at
or above the stop price after the order is
submitted. In an order to sell the order
becomes a market order when the
financial instrument trades at or below
the stop price.
13.2.2.50  UnitOfMeasure9Code
Definition: Identifies the unit of measure by means of a code. The code is taken from UN/ECE
Recommendation 20.
Type: CodeSet
CodeName Name Definition
BAGG Bag Code for a bag.
BALE Bale Code for a bale.
BOTL Bottle Code for a bottle.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 526 March 2024
```

## File page 527

```text
CodeName Name Definition
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 527 March 2024
```

## File page 528

```text
CodeName Name Definition
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 528 March 2024
```

