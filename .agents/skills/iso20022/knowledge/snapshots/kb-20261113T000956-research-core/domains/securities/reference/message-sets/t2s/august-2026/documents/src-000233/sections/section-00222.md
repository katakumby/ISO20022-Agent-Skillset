---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.8.3.6 ServiceItemCorrection <SvcItmCrrctn>", "15.4.2.1.8.3.6.3 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.3.6.3 CreditDebitIndicator <CdtDbtInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 299

```text
15.4.2.1.8.3.6.3  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the correction is a debit or credit.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
15.4.2.1.8.3.6.4  Quantity <Qty>
Presence: [1..1]
Definition: Sum of total number units per service item.
Datatype: "Number" on page 3324
15.4.2.1.8.3.6.5  BalanceCurrency <BalCcy>
Presence: [0..1]
Definition: Currency of the balance. Should be present only if quantity is a balance.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
15.4.2.1.8.3.6.6  UnitPrice <UnitPric>
Presence: [0..1]
Definition: Specifies the price per unit of the service item.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 299 August 2026
```

