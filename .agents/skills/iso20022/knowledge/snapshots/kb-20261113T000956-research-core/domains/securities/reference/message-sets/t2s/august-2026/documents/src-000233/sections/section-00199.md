---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.1 AccountIdentification <AcctId>"]
file_pages: [274]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.1 AccountIdentification <AcctId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 274 to 274.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 274

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Description <Desc> [0..1] Text 295
           Rate <Rate> [0..1] Rate 295
           Amount <Amt> [0..1] Amount C1, C4 295
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  296
         Amount <Amt> [1..1] Amount C1, C4 296
         ForeignExchange <FX> [0..1] ± 296
     ServiceItemCorrection <SvcItmCrrctn> [0..*]  297
       ItemType <ItmTp> [1..1] Text 298
       Description <Desc> [0..1] Text 298
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 299
       Quantity <Qty> [1..1] Quantity 299
       BalanceCurrency <BalCcy> [0..1] CodeSet C1 299
       UnitPrice <UnitPric> [0..1] Amount C1, C4 299
       Tax <Tax> [0..*]  300
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
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  303
         Amount <Amt> [1..1] Amount C1, C4 303
         ForeignExchange <FX> [0..1] ± 303
15.4.2.1.8.1  AccountIdentification <AcctId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 274 August 2026
```

