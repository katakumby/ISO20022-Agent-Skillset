---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.1 AccountIdentification <AcctId>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.1 AccountIdentification <AcctId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Type <Tp> [0..1] Text 331
         Description <Desc> [0..1] Text 331
         Rate <Rate> [0..1] Rate 331
         Amount <Amt> [0..1] Amount C1, C4 331
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  332
       Amount <Amt> [1..1] Amount C1, C4 332
       ForeignExchange <FX> [0..1] ± 332
15.4.2.1.10.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique identification of a securities account or cash account belonging to billed customer.
AccountIdentification <AcctId> contains one of the following AccountIdentification38Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 314
Or}   CashAccountIdentification <CshAcctId> [1..1] ± 314
15.4.2.1.10.1.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Unique identification of the securities account as assigned by the account servicer.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
15.4.2.1.10.1.2  CashAccountIdentification <CshAcctId>
Presence: [1..1]
Definition: Unique identification of the cash account, as assigned by the account servicer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 314 August 2026
```

