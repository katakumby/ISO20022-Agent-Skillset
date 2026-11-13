---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.3 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.8.3.1 BilledCustomerIdentification <BlldCstmrId>"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.3.1 BilledCustomerIdentification <BlldCstmrId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  303
       Amount <Amt> [1..1] Amount C1, C4 303
       ForeignExchange <FX> [0..1] ± 303
15.4.2.1.8.3.1  BilledCustomerIdentification <BlldCstmrId>
Presence: [0..1]
Definition: Identification of the customer which is invoiced.
BilledCustomerIdentification <BlldCstmrId> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
15.4.2.1.8.3.2  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Tax <Tax> contains the following BillingTaxRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [1..1] Rate 285
   Description <Desc> [0..1] Text 286
   TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 286
   TaxExemption <TaxXmptn> [0..*]  286
     ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 286
     Reason <Rsn> [0..1] Text 287
   Amount <Amt> [1..1] Amount C1, C4 287
   ChargesAndFees <ChrgsAndFees> [0..*]  287
     Type <Tp> [0..1] Text 288
     Description <Desc> [0..1] Text 288
     Rate <Rate> [0..1] Rate 288
     Amount <Amt> [0..1] Amount C1, C4 288
15.4.2.1.8.3.2.1  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 285 August 2026
```

