---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.1 AccountIdentification <AcctId>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.1 AccountIdentification <AcctId>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Description <Desc> [0..1] Text 66
           Rate <Rate> [0..1] Rate 66
           Amount <Amt> [0..1] Amount C1, C4 66
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  67
         Amount <Amt> [1..1] Amount C1, C4 67
         ForeignExchange <FX> [0..1] ± 67
     ServiceItemCorrection <SvcItmCrrctn> [0..*]  68
       ItemType <ItmTp> [1..1] Text 69
       Description <Desc> [0..1] Text 69
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 70
       Quantity <Qty> [1..1] Quantity 70
       BalanceCurrency <BalCcy> [0..1] CodeSet C1 70
       UnitPrice <UnitPric> [0..1] Amount C1, C4 70
       Tax <Tax> [0..*]  71
         Rate <Rate> [1..1] Rate 71
         Description <Desc> [0..1] Text 71
         TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 71
         TaxExemption <TaxXmptn> [0..*]  72
           ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 72
           Reason <Rsn> [0..1] Text 72
         Amount <Amt> [1..1] Amount C1, C4 72
         ChargesAndFees <ChrgsAndFees> [0..*]  73
           Type <Tp> [0..1] Text 73
           Description <Desc> [0..1] Text 73
           Rate <Rate> [0..1] Rate 73
           Amount <Amt> [0..1] Amount C1, C4 73
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  74
         Amount <Amt> [1..1] Amount C1, C4 74
         ForeignExchange <FX> [0..1] ± 74
3.4.2.1.8.1  AccountIdentification <AcctId>
Presence: [1..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 45 December 2025
```

