---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.9 InvoiceTotals <InvcTtls>", "3.4.2.1.9.1 Tax <Tax>"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.9.1 Tax <Tax>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
InvoiceTotals <InvcTtls> contains the following InvoiceTotals7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Tax <Tax> [0..*]  76
     Rate <Rate> [1..1] Rate 77
     Description <Desc> [0..1] Text 77
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 77
     TaxExemption <TaxXmptn> [0..*]  78
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 78
       Reason <Rsn> [0..1] Text 78
     Amount <Amt> [1..1] Amount C1, C4 78
     ChargesAndFees <ChrgsAndFees> [0..*]  79
       Type <Tp> [0..1] Text 79
       Description <Desc> [0..1] Text 79
       Rate <Rate> [0..1] Rate 79
       Amount <Amt> [0..1] Amount C1, C4 79
   Adjustment <Adjstmnt> [0..1]  80
     Direction <Drctn> [1..1] CodeSet 80
     Amount <Amt> [1..1] Amount C1, C4 80
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  81
     Amount <Amt> [1..1] Amount C1, C4 81
     ForeignExchange <FX> [0..1] ± 81
   PaymentDueDate <PmtDueDt> [1..1] Date 82
   CashAccount <CshAcct> [0..1] ± 82
3.4.2.1.9.1  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 76 December 2025
```

