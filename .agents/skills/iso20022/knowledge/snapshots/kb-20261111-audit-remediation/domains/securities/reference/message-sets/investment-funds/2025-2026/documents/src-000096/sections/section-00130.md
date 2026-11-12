---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.14 ChargeDetails <ChrgDtls>", "13.4.9.14.14.3 CalculationBasis <ClctnBsis>"]
file_pages: [196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.14.3 CalculationBasis <ClctnBsis>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 196 to 196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 196

```text
ChargesFees <ChrgsFees> contains one of the following elements (see
"PriceRateOrAmount3Choice" on page 5114 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 5114
Or}   Amount <Amt> [1..1] Amount C2 5114
13.4.9.14.14.3  CalculationBasis <ClctnBsis>
Presence: [0..1]
Definition: Calculation basis for the charge or fee.
CalculationBasis <ClctnBsis> contains one of the following CalculationBasis2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 196
Or}   Proprietary <Prtry> [1..1] Text 196
13.4.9.14.14.3.1  Code <Cd>
Presence: [1..1]
Definition: Calculation basis expressed as an ISO 20022 code.
Datatype: "CalculationBasis2Code" on page 5279
CodeName Name Definition
AVER Average Average basis.
DAIL Daily Daily basis.
MNTH Monthly Monthly basis.
YEAR Annual Yearly basis.
13.4.9.14.14.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Calculation basis expressed as an extended code.
Datatype: "Max350Text" on page 5403
13.4.9.14.15  TaxLiabilityDetails <TaxLbltyDtls>
Presence: [0..*]
Definition: Information related to taxes that are due.
Impacted by: C4 "AmountAndOrRateRule"
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 196 May 2026
```

