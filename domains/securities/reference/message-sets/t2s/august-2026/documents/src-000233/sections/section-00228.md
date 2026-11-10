---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.9 InvoiceTotals <InvcTtls>", "15.4.2.1.9.1 Tax <Tax>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.9.1 Tax <Tax>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
InvoiceTotals <InvcTtls> contains the following InvoiceTotals7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Tax <Tax> [0..*]  305
     Rate <Rate> [1..1] Rate 306
     Description <Desc> [0..1] Text 306
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 306
     TaxExemption <TaxXmptn> [0..*]  307
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 307
       Reason <Rsn> [0..1] Text 307
     Amount <Amt> [1..1] Amount C1, C4 307
     ChargesAndFees <ChrgsAndFees> [0..*]  308
       Type <Tp> [0..1] Text 308
       Description <Desc> [0..1] Text 308
       Rate <Rate> [0..1] Rate 308
       Amount <Amt> [0..1] Amount C1, C4 308
   Adjustment <Adjstmnt> [0..1]  309
     Direction <Drctn> [1..1] CodeSet 309
     Amount <Amt> [1..1] Amount C1, C4 309
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  310
     Amount <Amt> [1..1] Amount C1, C4 310
     ForeignExchange <FX> [0..1] ± 310
   PaymentDueDate <PmtDueDt> [1..1] Date 311
   CashAccount <CshAcct> [0..1] ± 311
15.4.2.1.9.1  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 305 August 2026
```

