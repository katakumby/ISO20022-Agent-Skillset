---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.10.8 ServiceItemCorrection <SvcItmCrrctn>", "3.4.2.1.10.8.3 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.10.8.3 CreditDebitIndicator <CdtDbtInd>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 99 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

```text
3.4.2.1.10.8.3  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the correction is a debit or credit.
Datatype: "CreditDebitCode" on page 145
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.1.10.8.4  Quantity <Qty>
Presence: [1..1]
Definition: Sum of total number units per service item.
Datatype: "Number" on page 150
3.4.2.1.10.8.5  UnitPrice <UnitPric>
Presence: [0..1]
Definition: Specifies the price per unit of the service item.
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
3.4.2.1.10.8.6  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 99 December 2025
```

