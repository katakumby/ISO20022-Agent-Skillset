---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.10 PriceFormat73Choice", "16.1.20.10.2 AmountPrice <AmtPric>"]
file_pages: [1086]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.10.2 AmountPrice <AmtPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1086 to 1086.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1086

```text
16.1.20.10.2  AmountPrice <AmtPric>
Presence: [1..1]
Definition: Price expressed as a currency and amount.
AmountPrice <AmtPric> contains the following elements (see "AmountPrice3" on page 1067 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1068
   PriceValue <PricVal> [1..1] Amount C1 1068
16.1.20.10.3  NotSpecifiedPrice <NotSpcfdPric>
Presence: [1..1]
Definition: Value of the price not specified.
Datatype: "PriceValueType10Code" on page 1231
CodeName Name Definition
UKWN Unknown Price is unknown by the sender or has
not been established.
16.1.20.10.4  IndexPoints <IndxPts>
Presence: [1..1]
Definition: Price expressed as an index points.
Datatype: "DecimalNumber" on page 1246
16.1.21 Quantity
16.1.21.1  Quantity49Choice
Definition: Choice between different quantity of security formats.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1086 February 2026
```

