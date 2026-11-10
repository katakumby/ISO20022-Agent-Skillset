---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.8.3.1 BilledCustomerIdentification <BlldCstmrId>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.3.1 BilledCustomerIdentification <BlldCstmrId>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  74
       Amount <Amt> [1..1] Amount C1, C4 74
       ForeignExchange <FX> [0..1] ± 74
3.4.2.1.8.3.1  BilledCustomerIdentification <BlldCstmrId>
Presence: [0..1]
Definition: Identification of the customer which is invoiced.
BilledCustomerIdentification <BlldCstmrId> contains the following elements (see
"PartyIdentification136" on page 123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 123
   LEI <LEI> [0..1] IdentifierSet 123
3.4.2.1.8.3.2  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Tax <Tax> contains the following BillingTaxRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [1..1] Rate 56
   Description <Desc> [0..1] Text 57
   TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 57
   TaxExemption <TaxXmptn> [0..*]  57
     ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 57
     Reason <Rsn> [0..1] Text 58
   Amount <Amt> [1..1] Amount C1, C4 58
   ChargesAndFees <ChrgsAndFees> [0..*]  58
     Type <Tp> [0..1] Text 59
     Description <Desc> [0..1] Text 59
     Rate <Rate> [0..1] Rate 59
     Amount <Amt> [0..1] Amount C1, C4 59
3.4.2.1.8.3.2.1  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 56 December 2025
```

