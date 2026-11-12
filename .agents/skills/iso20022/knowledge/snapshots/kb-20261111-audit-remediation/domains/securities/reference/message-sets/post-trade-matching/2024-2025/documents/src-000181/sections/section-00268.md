---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.4 FutureDate <FutrDt>"]
file_pages: [326]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.4 FutureDate <FutrDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 326 to 326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 326

```text
CodeName Name Definition
GBPI GBPint Unit of volume that is equal to 568 cubic
centimetres.
USPI USPint Unit of volume that is equal to 473 cubic
centimetres.
MILE Mile Unit of length equal to 1, 760 yards.
KMET Kilometre Unit of measure that is equal to 1, 000
meters.
YARD Yard Unit of length equal to 3 feet or 0.9144
metre.
SQKI SquareKilometre Measure of a surface, one kilometre by
one kilometre.
HECT Hectare Unit of measure that is equal to 10, 000
square meters.
ARES Are Unit of measure equal to a 100 square
meters.
SMET SquareMetre Measure of a surface, one metre by one
metre.
SCMT SquareCentimetre Measure of a surface, one centimetre by
one centimetre.
SMIL SquareMillimetre Measure of a surface, one millimetre by
one millimetre.
SQMI SquareMile Measure of a surface, one mile by one
mile.
SQYA SquareYard Measure of a surface, one yard by one
yard.
SQFO SquareFoot Measure of a surface, one foot by one
foot.
SQIN SquareInch Measure of a surface, one inch by one
inch.
ACRE Acre Unit of measure equal to 4, 840 square
yards.
7.1.19.35.4  FutureDate <FutrDt>
Presence: [0..1]
Definition: Date on which future contracts settle.
Datatype: "ISODateTime" on page 662
7.1.19.35.5  MinimumSize <MinSz>
Presence: [0..1]
Definition: Specifies the minimum ratio or multiply factor used to convert from contracts to shares.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 611
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 326 February 2025
```

