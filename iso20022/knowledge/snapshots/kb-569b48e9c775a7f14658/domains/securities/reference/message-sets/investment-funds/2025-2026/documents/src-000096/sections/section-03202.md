---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.6 FundConfirmedCashForecastReport3", "66.1.7.6.4 Extension <Xtnsn>"]
file_pages: [4434]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.6.4 Extension <Xtnsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4434 to 4434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4434

```text
ConsolidatedNetCashForecast <CnsltdNetCshFcst> contains the following elements (see
"NetCashForecast3" on page 4412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NetAmount <NetAmt> [0..1] Amount C2, C10 4412
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4412
   FlowDirection <FlowDrctn> [1..1] CodeSet 4413
66.1.7.6.4  Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C16 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
66.1.8 Charge
66.1.8.1  Fees2
Definition: Amount of money associated with a service.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4434 May 2026
```

