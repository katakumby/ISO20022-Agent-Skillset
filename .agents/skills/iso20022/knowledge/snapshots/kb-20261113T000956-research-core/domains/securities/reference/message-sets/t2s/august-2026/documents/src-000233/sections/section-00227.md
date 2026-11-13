---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.9 InvoiceTotals <InvcTtls>"]
file_pages: [304]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.9 InvoiceTotals <InvcTtls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 304 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 304

```text
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
15.4.2.1.9  InvoiceTotals <InvcTtls>
Presence: [0..1]
Definition: Specifies totals related to the invoice.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 304 August 2026
```

