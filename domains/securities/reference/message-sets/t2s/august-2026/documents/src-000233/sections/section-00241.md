---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.5 TotalInvoiceAmount <TtlInvcAmt>", "15.4.2.1.10.5.2 ForeignExchange <FX>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.5.2 ForeignExchange <FX>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
15.4.2.1.10.5.2  ForeignExchange <FX>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms24" on
page 2955 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 2955
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 2955
   ExchangeRate <XchgRate> [1..1] Rate 2956
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 2956
15.4.2.1.10.6  ServiceCategory <SvcCtgy>
Presence: [1..1]
Definition: Agreement under which or rules under which the transaction should be processed.
ServiceCategory <SvcCtgy> contains one of the following ServiceCategory1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 320
Or}   Proprietary <Prtry> [1..1] Text 320
15.4.2.1.10.6.1  Code <Cd>
Presence: [1..1]
Definition: Service category, as published in an external reason code list.
Datatype: "ExternalServiceCategory1Code" on page 3245
15.4.2.1.10.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Service category, in a proprietary form.
Datatype: "Max4AlphaNumericText" on page 3328
15.4.2.1.10.7  ServiceItemTotals <SvcItmTtls>
Presence: [0..*]
Definition: Totals related to the invoice.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 320 August 2026
```

