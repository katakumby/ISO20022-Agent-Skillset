---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.2 InvoiceTotals <InvcTtls>", "3.4.2.1.8.2.1 Tax <Tax>"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.2.1 Tax <Tax>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
InvoiceTotals <InvcTtls> contains the following InvoiceTotals7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Tax <Tax> [0..*]  47
     Rate <Rate> [1..1] Rate 48
     Description <Desc> [0..1] Text 48
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 48
     TaxExemption <TaxXmptn> [0..*]  49
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 49
       Reason <Rsn> [0..1] Text 49
     Amount <Amt> [1..1] Amount C1, C4 49
     ChargesAndFees <ChrgsAndFees> [0..*]  50
       Type <Tp> [0..1] Text 50
       Description <Desc> [0..1] Text 50
       Rate <Rate> [0..1] Rate 50
       Amount <Amt> [0..1] Amount C1, C4 50
   Adjustment <Adjstmnt> [0..1]  51
     Direction <Drctn> [1..1] CodeSet 51
     Amount <Amt> [1..1] Amount C1, C4 51
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  52
     Amount <Amt> [1..1] Amount C1, C4 52
     ForeignExchange <FX> [0..1] ± 52
   PaymentDueDate <PmtDueDt> [1..1] Date 53
   CashAccount <CshAcct> [0..1] ± 53
3.4.2.1.8.2.1  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 47 December 2025
```

