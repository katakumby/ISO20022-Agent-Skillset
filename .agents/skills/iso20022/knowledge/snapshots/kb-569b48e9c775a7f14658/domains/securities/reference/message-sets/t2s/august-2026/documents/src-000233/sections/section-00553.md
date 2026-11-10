---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.1 Future <Futr>", "27.4.2.2.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "27.4.2.2.4.1.7.11 EndValue <EndVal>"]
file_pages: [725]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.1.7.11 EndValue <EndVal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 725 to 725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 725

```text
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
27.4.2.2.4.1.7.11  EndValue <EndVal>
Presence: [0..1]
Definition: Currency value attributed to this collateral at the end of the agreement.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
27.4.2.2.4.1.7.12  AdjustedQuantity <AdjstdQty>
Presence: [0..1]
Definition: Unit amount of the underlying security (shares) adjusted for pending corporate action not yet
allocated.
AdjustedQuantity <AdjstdQty> contains one of the following UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 725
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 726
27.4.2.2.4.1.7.12.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 725 August 2026
```

