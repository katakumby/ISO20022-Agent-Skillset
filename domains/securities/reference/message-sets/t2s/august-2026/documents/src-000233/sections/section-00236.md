---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.10 ServiceCategoryTotals <SvcCtgyTtls>", "15.4.2.1.10.2 ParentAccountIdentification <PrntAcctId>"]
file_pages: [315]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.10.2 ParentAccountIdentification <PrntAcctId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 315 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 315

```text
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
15.4.2.1.10.2  ParentAccountIdentification <PrntAcctId>
Presence: [0..1]
Definition: Unique identification of a securities parent account or cash parent account belonging to billed
customer, when reporting on sub-accounts.
ParentAccountIdentification <PrntAcctId> contains one of the following
AccountIdentification38Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 315
Or}   CashAccountIdentification <CshAcctId> [1..1] ± 315
15.4.2.1.10.2.1  SecuritiesAccountIdentification <SctiesAcctId>
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
15.4.2.1.10.2.2  CashAccountIdentification <CshAcctId>
Presence: [1..1]
Definition: Unique identification of the cash account, as assigned by the account servicer.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
15.4.2.1.10.3  BilledCustomerIdentification <BlldCstmrId>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 315 August 2026
```

