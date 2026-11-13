---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.33 TradingMethod <TradgMtd>", "28.4.2.1.1.2.33.1 Unit <Unit>"]
file_pages: [1146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.33.1 Unit <Unit>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1146 to 1146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1146

```text
TradingMethod <TradgMtd> contains one of the following UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1146
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 1146
28.4.2.1.1.2.33.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 3324
28.4.2.1.1.2.33.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, ie, the principal, of a debt
instrument.
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
28.4.2.1.1.2.34  TEFRARule <TEFRARule>
Presence: [0..1]
Definition: Indicates the TEFRA rule under which the security is issued.
TEFRARule <TEFRARule> contains one of the following TEFRARules3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1146
Or}   Proprietary <Prtry> [1..1] ± 1147
28.4.2.1.1.2.34.1  Code <Cd>
Presence: [1..1]
Definition: TEFRA rules expressed as an ISO 20022 code.
Datatype: "TEFRARules1Code" on page 3306
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1146 August 2026
```

