---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.8.3.5 ServiceItemTotals <SvcItmTtls>", "3.4.2.1.8.3.5.1 ItemType <ItmTp>"]
file_pages: [62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.3.5.1 ItemType <ItmTp>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 62 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 62

```text
ServiceItemTotals <SvcItmTtls> contains the following ServiceItemTotals10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ItemType <ItmTp> [1..1] Text 62
   Description <Desc> [0..1] Text 62
   Quantity <Qty> [1..1] Quantity 63
   BalanceCurrency <BalCcy> [0..1] CodeSet C1 63
   UnitPrice <UnitPric> [0..1] Amount C1, C4 63
   Tax <Tax> [0..*]  63
     Rate <Rate> [1..1] Rate 64
     Description <Desc> [0..1] Text 64
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 64
     TaxExemption <TaxXmptn> [0..*]  65
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 65
       Reason <Rsn> [0..1] Text 65
     Amount <Amt> [1..1] Amount C1, C4 65
     ChargesAndFees <ChrgsAndFees> [0..*]  66
       Type <Tp> [0..1] Text 66
       Description <Desc> [0..1] Text 66
       Rate <Rate> [0..1] Rate 66
       Amount <Amt> [0..1] Amount C1, C4 66
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  67
     Amount <Amt> [1..1] Amount C1, C4 67
     ForeignExchange <FX> [0..1] ± 67
3.4.2.1.8.3.5.1  ItemType <ItmTp>
Presence: [1..1]
Definition: Specifies a classification for the service items such as query, report, securities account,
etc….
Datatype: "Max20AlphaNumericText" on page 152
3.4.2.1.8.3.5.2  Description <Desc>
Presence: [0..1]
Definition: Description of the service item.
Datatype: "Max350Text" on page 153
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 62 December 2025
```

