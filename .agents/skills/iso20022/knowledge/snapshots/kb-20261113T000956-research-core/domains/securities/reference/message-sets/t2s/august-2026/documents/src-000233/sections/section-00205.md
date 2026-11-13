---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.2 InvoiceTotals <InvcTtls>", "15.4.2.1.8.2.2 Adjustment <Adjstmnt>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.2.2 Adjustment <Adjstmnt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
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
15.4.2.1.8.2.2  Adjustment <Adjstmnt>
Presence: [0..1]
Definition: Variance on invoice amount taking into account discounts, allowances and charges.
Adjustment <Adjstmnt> contains the following Adjustment5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Direction <Drctn> [1..1] CodeSet 280
   Amount <Amt> [1..1] Amount C1, C4 280
15.4.2.1.8.2.2.1  Direction <Drctn>
Presence: [1..1]
Definition: Specifies whether the adjustment must be substracted or added to the total amount.
Datatype: "AdjustmentDirection1Code" on page 3213
CodeName Name Definition
ADDD Added Adjustment amount must be added to
the total amount.
SUBS Substracted Adjustment amount must be substracted
from the total amount.
15.4.2.1.8.2.2.2  Amount <Amt>
Presence: [1..1]
Definition: Specifies the monetary amount of the adjustment.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 280 August 2026
```

