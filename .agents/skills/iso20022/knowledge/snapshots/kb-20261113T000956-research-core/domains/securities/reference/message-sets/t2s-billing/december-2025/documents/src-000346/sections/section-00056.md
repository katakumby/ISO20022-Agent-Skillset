---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.9 InvoiceTotals <InvcTtls>", "3.4.2.1.9.2 Adjustment <Adjstmnt>"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.9.2 Adjustment <Adjstmnt>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.1.9.2  Adjustment <Adjstmnt>
Presence: [0..1]
Definition: Variance on invoice amount taking into account discounts, allowances and charges.
Adjustment <Adjstmnt> contains the following Adjustment5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Direction <Drctn> [1..1] CodeSet 80
   Amount <Amt> [1..1] Amount C1, C4 80
3.4.2.1.9.2.1  Direction <Drctn>
Presence: [1..1]
Definition: Specifies whether the adjustment must be substracted or added to the total amount.
Datatype: "AdjustmentDirection1Code" on page 144
CodeName Name Definition
ADDD Added Adjustment amount must be added to
the total amount.
SUBS Substracted Adjustment amount must be substracted
from the total amount.
3.4.2.1.9.2.2  Amount <Amt>
Presence: [1..1]
Definition: Specifies the monetary amount of the adjustment.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 143
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 80 December 2025
```

