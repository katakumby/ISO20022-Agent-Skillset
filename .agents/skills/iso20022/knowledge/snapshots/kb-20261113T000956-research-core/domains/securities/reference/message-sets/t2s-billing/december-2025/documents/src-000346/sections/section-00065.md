---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.10.5 TotalInvoiceAmount <TtlInvcAmt>", "3.4.2.1.10.5.2 ForeignExchange <FX>"]
file_pages: [91]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.10.5.2 ForeignExchange <FX>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 91 to 91.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 91

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.1.10.5.2  ForeignExchange <FX>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms24" on
page 115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 115
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 116
   ExchangeRate <XchgRate> [1..1] Rate 116
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 116
3.4.2.1.10.6  ServiceCategory <SvcCtgy>
Presence: [1..1]
Definition: Agreement under which or rules under which the transaction should be processed.
ServiceCategory <SvcCtgy> contains one of the following ServiceCategory1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 91
Or}   Proprietary <Prtry> [1..1] Text 91
3.4.2.1.10.6.1  Code <Cd>
Presence: [1..1]
Definition: Service category, as published in an external reason code list.
Datatype: "ExternalServiceCategory1Code" on page 147
3.4.2.1.10.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Service category, in a proprietary form.
Datatype: "Max4AlphaNumericText" on page 153
3.4.2.1.10.7  ServiceItemTotals <SvcItmTtls>
Presence: [0..*]
Definition: Totals related to the invoice.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 91 December 2025
```

