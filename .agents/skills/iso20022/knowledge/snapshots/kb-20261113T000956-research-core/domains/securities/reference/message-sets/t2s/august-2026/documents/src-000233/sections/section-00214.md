---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.8.3.5 ServiceItemTotals <SvcItmTtls>", "15.4.2.1.8.3.5.1 ItemType <ItmTp>"]
file_pages: [291]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.3.5.1 ItemType <ItmTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 291 to 291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
ServiceItemTotals <SvcItmTtls> contains the following ServiceItemTotals10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ItemType <ItmTp> [1..1] Text 291
   Description <Desc> [0..1] Text 291
   Quantity <Qty> [1..1] Quantity 292
   BalanceCurrency <BalCcy> [0..1] CodeSet C1 292
   UnitPrice <UnitPric> [0..1] Amount C1, C4 292
   Tax <Tax> [0..*]  292
     Rate <Rate> [1..1] Rate 293
     Description <Desc> [0..1] Text 293
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 293
     TaxExemption <TaxXmptn> [0..*]  294
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 294
       Reason <Rsn> [0..1] Text 294
     Amount <Amt> [1..1] Amount C1, C4 294
     ChargesAndFees <ChrgsAndFees> [0..*]  295
       Type <Tp> [0..1] Text 295
       Description <Desc> [0..1] Text 295
       Rate <Rate> [0..1] Rate 295
       Amount <Amt> [0..1] Amount C1, C4 295
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  296
     Amount <Amt> [1..1] Amount C1, C4 296
     ForeignExchange <FX> [0..1] ± 296
15.4.2.1.8.3.5.1  ItemType <ItmTp>
Presence: [1..1]
Definition: Specifies a classification for the service items such as query, report, securities account,
etc….
Datatype: "Max20AlphaNumericText" on page 3327
15.4.2.1.8.3.5.2  Description <Desc>
Presence: [0..1]
Definition: Description of the service item.
Datatype: "Max350Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 291 August 2026
```

