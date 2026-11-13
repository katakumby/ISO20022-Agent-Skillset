---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.3 Date Period", "4.1.3.1 DatePeriod2", "4.1.3.1.1 FromDate <FrDt>"]
file_pages: [115]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.3.1.1 FromDate <FrDt>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 115 to 115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 115

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 115
   ToDate <ToDt> [1..1] Date 115
4.1.3.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 148
4.1.3.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 148
4.1.4 Foreign Exchange
4.1.4.1  ForeignExchangeTerms24
Definition: Provides information about the terms of the foreign exchange transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 115
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 116
   ExchangeRate <XchgRate> [1..1] Rate 116
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 116
4.1.4.1.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 115 December 2025
```

