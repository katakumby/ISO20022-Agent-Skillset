---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.2 InvoiceTotals <InvcTtls>", "3.4.2.1.8.2.1 Tax <Tax>", "3.4.2.1.8.2.1.4 TaxExemption <TaxXmptn>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.2.1.4 TaxExemption <TaxXmptn>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.1.8.2.1.4  TaxExemption <TaxXmptn>
Presence: [0..*]
Definition: Amount exempted from tax.
TaxExemption <TaxXmptn> contains the following TaxExemption1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 49
   Reason <Rsn> [0..1] Text 49
3.4.2.1.8.2.1.4.1  ExemptedAmount <XmptdAmt>
Presence: [1..1]
Definition: Amount exempted from tax.
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
3.4.2.1.8.2.1.4.2  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the tax exemption.
Datatype: "Max210Text" on page 152
3.4.2.1.8.2.1.5  Amount <Amt>
Presence: [1..1]
Definition: Calculated tax amount.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 49 December 2025
```

