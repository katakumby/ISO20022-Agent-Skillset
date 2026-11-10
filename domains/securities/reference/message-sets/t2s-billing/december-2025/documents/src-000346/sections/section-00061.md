---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "3.4.2.1.10.4 Tax <Tax>"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.10.4 Tax <Tax>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
Definition: Identification of the customer which is invoiced.
BilledCustomerIdentification <BlldCstmrId> contains the following elements (see
"PartyIdentification136" on page 123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 123
   LEI <LEI> [0..1] IdentifierSet 123
3.4.2.1.10.4  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Tax <Tax> contains the following BillingTaxRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [1..1] Rate 87
   Description <Desc> [0..1] Text 87
   TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 87
   TaxExemption <TaxXmptn> [0..*]  88
     ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 88
     Reason <Rsn> [0..1] Text 88
   Amount <Amt> [1..1] Amount C1, C4 89
   ChargesAndFees <ChrgsAndFees> [0..*]  89
     Type <Tp> [0..1] Text 89
     Description <Desc> [0..1] Text 89
     Rate <Rate> [0..1] Rate 90
     Amount <Amt> [0..1] Amount C1, C4 90
3.4.2.1.10.4.1  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 150
3.4.2.1.10.4.2  Description <Desc>
Presence: [0..1]
Definition: Name used to describe the tax (such as the national value added tax).
Datatype: "Max40Text" on page 153
3.4.2.1.10.4.3  TaxableAmount <TaxblAmt>
Presence: [1..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 87 December 2025
```

