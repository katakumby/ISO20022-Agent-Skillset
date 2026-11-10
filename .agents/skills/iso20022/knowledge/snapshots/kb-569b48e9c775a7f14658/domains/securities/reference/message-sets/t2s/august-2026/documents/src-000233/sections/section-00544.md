---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.1 Future <Futr>", "27.4.2.2.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "27.4.2.2.4.1.7.1 AllocationPercentage <AllcnPctg>"]
file_pages: [716]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.1.7.1 AllocationPercentage <AllcnPctg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 716 to 716.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 716

```text
27.4.2.2.4.1.7.1  AllocationPercentage <AllcnPctg>
Presence: [0..1]
Definition: Percent of the strike price that this underlying represents.
Datatype: "PercentageRate" on page 3325
27.4.2.2.4.1.7.2  Quantity <Qty>
Presence: [0..1]
Definition: Unit amount of the underlying security.
Quantity <Qty> contains one of the following UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 716
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 716
27.4.2.2.4.1.7.2.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 3324
27.4.2.2.4.1.7.2.2  FaceAmount <FaceAmt>
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
27.4.2.2.4.1.7.3  SettlementType <SttlmTp>
Presence: [0..1]
Definition: Indicates order settlement period for the underlying instrument. Represents the number of
days until settlement; for example, 2 means T+1 settlement, 4 means T+3 settlement, 5 means T+4
settlement.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 716 August 2026
```

