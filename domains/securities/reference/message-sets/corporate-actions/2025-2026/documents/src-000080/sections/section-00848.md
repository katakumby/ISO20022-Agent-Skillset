---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.2 PriceFormat46Choice", "16.1.20.2.1 AmountPrice <AmtPric>"]
file_pages: [1066]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.2.1 AmountPrice <AmtPric>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1066 to 1066.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1066

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountPrice <AmtPric> [1..1] ± 1066
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1066
16.1.20.2.1  AmountPrice <AmtPric>
Presence: [1..1]
Definition: Price expressed as a currency and amount.
AmountPrice <AmtPric> contains the following elements (see "AmountPrice2" on page 831 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 831
   PriceValue <PricVal> [1..1] Amount C1 831
16.1.20.2.2  NotSpecifiedPrice <NotSpcfdPric>
Presence: [1..1]
Definition: Value of the price not specified.
Datatype: "PriceValueType10Code" on page 1231
CodeName Name Definition
UKWN Unknown Price is unknown by the sender or has
not been established.
16.1.20.3  PriceFormat61Choice
Definition: Choice between a percentage price or an amount price or an unspecified price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountPrice <AmtPric> [1..1]  1066
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1067
     PriceValue <PricVal> [1..1] Amount C1 1067
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1067
16.1.20.3.1  AmountPrice <AmtPric>
Presence: [1..1]
Definition: Price expressed as a currency and amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1066 February 2026
```

