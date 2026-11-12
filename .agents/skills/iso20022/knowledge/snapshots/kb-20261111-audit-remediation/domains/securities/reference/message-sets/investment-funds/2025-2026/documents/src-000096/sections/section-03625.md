---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.36 BreakdownByCountry2", "66.1.28.36.2 CashInForecast <CshInFcst>", "66.1.28.36.2.3 SubTotalUnitsNumber <SubTtlUnitsNb>"]
file_pages: [4875]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.36.2.3 SubTotalUnitsNumber <SubTtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4875 to 4875.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4875

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.28.36.2.3  SubTotalUnitsNumber <SubTtlUnitsNb>
Presence: [0..1]
Definition: Sub-total amount of the cash flow in, expressed as a number of units.
SubTotalUnitsNumber <SubTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.28.36.2.4  ExceptionalCashFlowIndicator <XcptnlCshFlowInd>
Presence: [0..1]
Definition: Indicates whether the estimated cash flow in is exceptional.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.36.2.5  CashInBreakdownDetails <CshInBrkdwnDtls>
Presence: [0..*]
Definition: Breakdown of cash in amounts by transaction and order type.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4875 May 2026
```

