---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.2 InvoiceTotals <InvcTtls>", "15.4.2.1.8.2.1 Tax <Tax>"]
file_pages: [276]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.2.1 Tax <Tax>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 276 to 276.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 276

```text
InvoiceTotals <InvcTtls> contains the following InvoiceTotals7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Tax <Tax> [0..*]  276
     Rate <Rate> [1..1] Rate 277
     Description <Desc> [0..1] Text 277
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 277
     TaxExemption <TaxXmptn> [0..*]  278
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 278
       Reason <Rsn> [0..1] Text 278
     Amount <Amt> [1..1] Amount C1, C4 278
     ChargesAndFees <ChrgsAndFees> [0..*]  279
       Type <Tp> [0..1] Text 279
       Description <Desc> [0..1] Text 279
       Rate <Rate> [0..1] Rate 279
       Amount <Amt> [0..1] Amount C1, C4 279
   Adjustment <Adjstmnt> [0..1]  280
     Direction <Drctn> [1..1] CodeSet 280
     Amount <Amt> [1..1] Amount C1, C4 280
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  281
     Amount <Amt> [1..1] Amount C1, C4 281
     ForeignExchange <FX> [0..1] ± 281
   PaymentDueDate <PmtDueDt> [1..1] Date 282
   CashAccount <CshAcct> [0..1] ± 282
15.4.2.1.8.2.1  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 276 August 2026
```

