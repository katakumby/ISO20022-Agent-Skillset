---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.7 ServiceItemTotals <SvcItmTtls>", "15.4.2.1.10.7.5 Tax <Tax>", "15.4.2.1.10.7.5.4 TaxExemption <TaxXmptn>", "15.4.2.1.10.7.5.4.2 Reason <Rsn>"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.7.5.4.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
15.4.2.1.10.7.5.4.2  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the tax exemption.
Datatype: "Max210Text" on page 3327
15.4.2.1.10.7.5.5  Amount <Amt>
Presence: [1..1]
Definition: Calculated tax amount.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
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
15.4.2.1.10.7.5.6  ChargesAndFees <ChrgsAndFees>
Presence: [0..*]
Definition: Further details on the charges and fees realted to the tax data.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 324 August 2026
```

