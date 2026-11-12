---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.10.7 ServiceItemTotals <SvcItmTtls>", "3.4.2.1.10.7.1 ItemType <ItmTp>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.10.7.1 ItemType <ItmTp>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
ServiceItemTotals <SvcItmTtls> contains the following ServiceItemTotals12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ItemType <ItmTp> [1..1] Text 92
   Description <Desc> [0..1] Text 92
   Quantity <Qty> [1..1] Quantity 92
   UnitPrice <UnitPric> [0..1] Amount C1, C4 93
   Tax <Tax> [0..*]  93
     Rate <Rate> [1..1] Rate 94
     Description <Desc> [0..1] Text 94
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 94
     TaxExemption <TaxXmptn> [0..*]  94
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 94
       Reason <Rsn> [0..1] Text 95
     Amount <Amt> [1..1] Amount C1, C4 95
     ChargesAndFees <ChrgsAndFees> [0..*]  95
       Type <Tp> [0..1] Text 96
       Description <Desc> [0..1] Text 96
       Rate <Rate> [0..1] Rate 96
       Amount <Amt> [0..1] Amount C1, C4 96
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  96
     Amount <Amt> [1..1] Amount C1, C4 97
     ForeignExchange <FX> [0..1] ± 97
3.4.2.1.10.7.1  ItemType <ItmTp>
Presence: [1..1]
Definition: Specifies a classification for the service items such as query, report, securities account,
etc….
Datatype: "Max20AlphaNumericText" on page 152
3.4.2.1.10.7.2  Description <Desc>
Presence: [0..1]
Definition: Description of the service item.
Datatype: "Max350Text" on page 153
3.4.2.1.10.7.3  Quantity <Qty>
Presence: [1..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 92 December 2025
```

