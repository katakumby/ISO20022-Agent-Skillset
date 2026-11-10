---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.8 ServiceItemCorrection <SvcItmCrrctn>", "15.4.2.1.10.8.1 ItemType <ItmTp>"]
file_pages: [327]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.8.1 ItemType <ItmTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 327 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 327

```text
ServiceItemCorrection <SvcItmCrrctn> contains the following ServiceItemTotals13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ItemType <ItmTp> [1..1] Text 327
   Description <Desc> [0..1] Text 327
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 328
   Quantity <Qty> [1..1] Quantity 328
   UnitPrice <UnitPric> [0..1] Amount C1, C4 328
   Tax <Tax> [0..*]  328
     Rate <Rate> [1..1] Rate 329
     Description <Desc> [0..1] Text 329
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 329
     TaxExemption <TaxXmptn> [0..*]  330
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 330
       Reason <Rsn> [0..1] Text 330
     Amount <Amt> [1..1] Amount C1, C4 330
     ChargesAndFees <ChrgsAndFees> [0..*]  331
       Type <Tp> [0..1] Text 331
       Description <Desc> [0..1] Text 331
       Rate <Rate> [0..1] Rate 331
       Amount <Amt> [0..1] Amount C1, C4 331
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  332
     Amount <Amt> [1..1] Amount C1, C4 332
     ForeignExchange <FX> [0..1] ± 332
15.4.2.1.10.8.1  ItemType <ItmTp>
Presence: [1..1]
Definition: Specifies a classification for the service items such as query, report, securities account,
etc….
Datatype: "Max20AlphaNumericText" on page 3327
15.4.2.1.10.8.2  Description <Desc>
Presence: [0..1]
Definition: Description of the service item.
Datatype: "Max350Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 327 August 2026
```

