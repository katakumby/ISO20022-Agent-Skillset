---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.2 LastDeliveryDate <LastDlvryDt>"]
file_pages: [325]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.2 LastDeliveryDate <LastDlvryDt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 325 to 325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 325

```text
7.1.19.35.2  LastDeliveryDate <LastDlvryDt>
Presence: [0..1]
Definition: Last date/time by which the option for physical delivery may still be exercised.
Datatype: "ISODateTime" on page 662
7.1.19.35.3  UnitOfMeasure <UnitOfMeasr>
Presence: [0..1]
Definition: Used to indicate the size of the underlying commodity on which the contract is based (e.g.,
2500 lbs of lean cattle, 1000 barrels of crude oil, 1000 bushels of corn, etc.).
Datatype: "UnitOfMeasure1Code" on page 657
CodeName Name Definition
PIEC Piece Standard length of cloth, wallpaper, as
an item for sale or amount of a
substance.
TONS Ton Measure of weight, in Britain 2240lb
(long ton)and in the US 2000lb (short
ton).
FOOT Foot Unit of length equal to 1/3 yard.
GBGA GBGallon Unit of volume that is equal to 8 pints.
USGA USGallon Unit of volume that is equal to 8 pints.
GRAM Gram Unit of measure that is equal to a 1,
000th of a kilo.
INCH Inch Measure of length equal to 2.54 cm.
KILO Kilogram Basic unit of mass in the SI system,
1000 grams.
PUND Pound Unit of weight equal to 0.454 kilograms.
METR Metre Unit of length in the metric system, equal
to 39.37 inches.
CMET Centimetre Unit of measure that is equal to one
hundredth of a metre.
MMET Millimetre Unit of measure that is a thousandth of
one metre.
LITR Litre Unit of volume that is equal to a
thousand cubic centimetres.
CELI Centilitre Unit of volume that is equal to one
hundredth of a litre.
MILI MilliLitre Unit of volume that is equal to one
thousandth of a litre.
GBOU GBOunce Unit of weight equal to a sixteenth of a
pound.
USOU USOunce Unit of weight equal to a sixteenth of a
pound.
GBQA GBQuart Unit of volume that is equal to 2 pints.
USQA USQuart Unit of volume that is equal to 2 pints.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 325 February 2025
```

