---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.9 Financial Instrument", "16.1.9.1 SecurityIdentification19", "16.1.9.1.2 OtherIdentification <OthrId>", "16.1.9.1.2.3 Type <Tp>"]
file_pages: [871]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.9.1.2.3 Type <Tp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 871 to 871.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 871

```text
16.1.9.1.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 879
Or}   Proprietary <Prtry> [1..1] Text 879
16.1.9.1.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 1249
16.1.10 Financial Instrument Quantity
16.1.10.1  QuantityToQuantityRatio1
Definition: Ratio expressed as a quotient of quantities.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
16.1.10.1.1  Quantity1 <Qty1>
Presence: [1..1]
Definition: Numerator of the quotient of quantities.
Datatype: "DecimalNumber" on page 1246
16.1.10.1.2  Quantity2 <Qty2>
Presence: [1..1]
Definition: Denominator of the quotient of quantities.
Datatype: "DecimalNumber" on page 1246
16.1.11 Foreign Exchange
16.1.11.1  ForeignExchangeTerms38
Definition: Provides information about the terms of the foreign exchange transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 871 February 2026
```

