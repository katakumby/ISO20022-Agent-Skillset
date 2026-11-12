---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.4 Tax <Tax>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.4 Tax <Tax>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
Definition: Identification of the customer which is invoiced.
BilledCustomerIdentification <BlldCstmrId> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
15.4.2.1.10.4  Tax <Tax>
Presence: [0..*]
Definition: Detailed information on tax applied.
Tax <Tax> contains the following BillingTaxRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [1..1] Rate 316
   Description <Desc> [0..1] Text 316
   TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 316
   TaxExemption <TaxXmptn> [0..*]  317
     ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 317
     Reason <Rsn> [0..1] Text 317
   Amount <Amt> [1..1] Amount C1, C4 318
   ChargesAndFees <ChrgsAndFees> [0..*]  318
     Type <Tp> [0..1] Text 318
     Description <Desc> [0..1] Text 318
     Rate <Rate> [0..1] Rate 319
     Amount <Amt> [0..1] Amount C1, C4 319
15.4.2.1.10.4.1  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 3325
15.4.2.1.10.4.2  Description <Desc>
Presence: [0..1]
Definition: Name used to describe the tax (such as the national value added tax).
Datatype: "Max40Text" on page 3328
15.4.2.1.10.4.3  TaxableAmount <TaxblAmt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 316 August 2026
```

