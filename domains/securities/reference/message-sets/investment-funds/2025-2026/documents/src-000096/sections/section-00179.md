---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.14 ChargeDetails <ChrgDtls>", "14.4.10.1.14.14.3 CalculationBasis <ClctnBsis>", "14.4.10.1.14.14.3.1 Code <Cd>"]
file_pages: [265]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.14.3.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 265 to 265.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 265

```text
Definition: Calculation basis for the charge or fee.
CalculationBasis <ClctnBsis> contains one of the following CalculationBasis2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 265
Or}   Proprietary <Prtry> [1..1] Text 265
14.4.10.1.14.14.3.1  Code <Cd>
Presence: [1..1]
Definition: Calculation basis expressed as an ISO 20022 code.
Datatype: "CalculationBasis2Code" on page 5279
CodeName Name Definition
AVER Average Average basis.
DAIL Daily Daily basis.
MNTH Monthly Monthly basis.
YEAR Annual Yearly basis.
14.4.10.1.14.14.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Calculation basis expressed as an extended code.
Datatype: "Max350Text" on page 5403
14.4.10.1.14.15  TaxLiabilityDetails <TaxLbltyDtls>
Presence: [0..*]
Definition: Information related to taxes that are due.
Impacted by: C4 "AmountAndOrRateRule"
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 265 May 2026
```

