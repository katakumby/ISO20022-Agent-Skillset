---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.1 Quantity49Choice", "16.1.21.1.2 ProprietaryQuantity <PrtryQty>", "16.1.21.1.2.1 ShortLongPosition <ShrtLngPos>"]
file_pages: [1089]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.1.2.1 ShortLongPosition <ShrtLngPos>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1089 to 1089.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1089

```text
Definition: Proprietary quantity of security format.
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [0..1] CodeSet 1089
   Quantity <Qty> [1..1] Quantity 1089
   QuantityType <QtyTp> [1..1] Text 1089
   Issuer <Issr> [1..1] Text 1089
   SchemeName <SchmeNm> [0..1] Text 1089
16.1.21.1.2.1  ShortLongPosition <ShrtLngPos>
Presence: [0..1]
Definition: Sign of the quantity of security.
Datatype: "ShortLong1Code" on page 1242
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
16.1.21.1.2.2  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 1246
16.1.21.1.2.3  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 1248
16.1.21.1.2.4  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 1251
16.1.21.1.2.5  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 1251
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1089 February 2026
```

