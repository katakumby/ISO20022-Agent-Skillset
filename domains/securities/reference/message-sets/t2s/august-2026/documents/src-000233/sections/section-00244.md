---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.7 ServiceItemTotals <SvcItmTtls>", "15.4.2.1.10.7.5 Tax <Tax>", "15.4.2.1.10.7.5.1 Rate <Rate>"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.7.5.1 Rate <Rate>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
15.4.2.1.10.7.5.1  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 3325
15.4.2.1.10.7.5.2  Description <Desc>
Presence: [0..1]
Definition: Name used to describe the tax (such as the national value added tax).
Datatype: "Max40Text" on page 3328
15.4.2.1.10.7.5.3  TaxableAmount <TaxblAmt>
Presence: [1..1]
Definition: Amount subject to tax.
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
15.4.2.1.10.7.5.4  TaxExemption <TaxXmptn>
Presence: [0..*]
Definition: Amount exempted from tax.
TaxExemption <TaxXmptn> contains the following TaxExemption1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 323
   Reason <Rsn> [0..1] Text 324
15.4.2.1.10.7.5.4.1  ExemptedAmount <XmptdAmt>
Presence: [1..1]
Definition: Amount exempted from tax.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 323 August 2026
```

