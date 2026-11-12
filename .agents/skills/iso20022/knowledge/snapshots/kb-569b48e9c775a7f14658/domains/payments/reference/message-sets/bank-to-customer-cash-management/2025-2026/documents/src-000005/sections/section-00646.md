---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.20 Price"]
file_pages: [879]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.20 Price

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 879 to 879.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 879

```text
6.1.20 Price
6.1.20.1  Price7
Definition: Type and information about a price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 879
   Value <Val> [1..1] ± 879
6.1.20.1.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the price type.
Type <Tp> contains one of the following elements (see "YieldedOrValueType1Choice" on page 856 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 857
Or}   ValueType <ValTp> [1..1] CodeSet 857
6.1.20.1.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 879
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 879
Or}   Amount <Amt> [1..1] Amount C1 880
6.1.20.2  PriceRateOrAmount3Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 879
Or}   Amount <Amt> [1..1] Amount C1 880
6.1.20.2.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
879 March 2026
```

