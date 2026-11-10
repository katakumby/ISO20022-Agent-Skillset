---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.29 OverAllotmentAmount <OverAlltmtAmt>"]
file_pages: [208]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.29 OverAllotmentAmount <OverAlltmtAmt>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 208 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 208

```text
Definition: Indicates whether the interest rate of an interest bearing instrument is reset periodically.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.29  OverAllotmentAmount <OverAlltmtAmt>
Presence: [0..1]
Definition: Amount for which a security can be overalloted (as in greenshoe option).
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.3.30  OverAllotmentRate <OverAlltmtRate>
Presence: [0..1]
Definition: Percentage for which a security can be overalloted (as in greenshoe option).
Datatype: "PercentageRate" on page 532
13.1.2.3.31  AmortisableIndicator <AmtsblInd>
Presence: [0..1]
Definition: Indicates whether repayment is made via regular principal and interest payments over time.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.32  InterestCalculationMethod <IntrstClctnMtd>
Presence: [0..1]
Definition: Calculation method used to calculate interest and/or yield for a bond, for example, street
convention.
Datatype: "Max70Text" on page 535
13.1.2.3.33  CapitalisedInterest <CptlsdIntrst>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 208 March 2024
```

