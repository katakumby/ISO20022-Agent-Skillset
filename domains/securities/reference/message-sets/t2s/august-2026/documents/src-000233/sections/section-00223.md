---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.8.3.6 ServiceItemCorrection <SvcItmCrrctn>", "15.4.2.1.8.3.6.7 Tax <Tax>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.3.6.7 Tax <Tax>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
15.4.2.1.8.3.6.7  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Tax <Tax> contains the following BillingTaxRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [1..1] Rate 300
   Description <Desc> [0..1] Text 300
   TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 300
   TaxExemption <TaxXmptn> [0..*]  301
     ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 301
     Reason <Rsn> [0..1] Text 301
   Amount <Amt> [1..1] Amount C1, C4 301
   ChargesAndFees <ChrgsAndFees> [0..*]  302
     Type <Tp> [0..1] Text 302
     Description <Desc> [0..1] Text 302
     Rate <Rate> [0..1] Rate 302
     Amount <Amt> [0..1] Amount C1, C4 302
15.4.2.1.8.3.6.7.1  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 3325
15.4.2.1.8.3.6.7.2  Description <Desc>
Presence: [0..1]
Definition: Name used to describe the tax (such as the national value added tax).
Datatype: "Max40Text" on page 3328
15.4.2.1.8.3.6.7.3  TaxableAmount <TaxblAmt>
Presence: [1..1]
Definition: Amount subject to tax.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 300 August 2026
```

