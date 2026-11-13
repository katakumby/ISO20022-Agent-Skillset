---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.29 OverAllotmentAmount <OverAlltmtAmt>"]
file_pages: [1885]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.29 OverAllotmentAmount <OverAlltmtAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1885 to 1885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1885

```text
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.1.2.3.29  OverAllotmentAmount <OverAlltmtAmt>
Presence: [0..1]
Definition: Amount for which a security can be overalloted (as in greenshoe option).
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
32.4.3.1.1.2.3.30  OverAllotmentRate <OverAlltmtRate>
Presence: [0..1]
Definition: Percentage for which a security can be overalloted (as in greenshoe option).
Datatype: "PercentageRate" on page 3325
32.4.3.1.1.2.3.31  AmortisableIndicator <AmtsblInd>
Presence: [0..1]
Definition: Indicates whether repayment is made via regular principal and interest payments over time.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.1.2.3.32  InterestCalculationMethod <IntrstClctnMtd>
Presence: [0..1]
Definition: Calculation method used to calculate interest and/or yield for a bond, for example, street
convention.
Datatype: "Max70Text" on page 3329
32.4.3.1.1.2.3.33  CapitalisedInterest <CptlsdIntrst>
Presence: [0..1]
Definition: Specifies whether the interest amount is capitalised until maturity date or paid out at each
interest payment date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1885 August 2026
```

