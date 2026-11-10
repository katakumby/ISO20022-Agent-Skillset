---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.1 AccountIdentification <AcctId>", "3.4.2.1.8.1.1 SecuritiesAccountIdentification <SctiesAcctId>"]
file_pages: [46]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.1.1 SecuritiesAccountIdentification <SctiesAcctId>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 46 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
Definition: Unique identification of a securities account or cash account belonging to billed customer.
AccountIdentification <AcctId> contains one of the following AccountIdentification38Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 46
Or}   CashAccountIdentification <CshAcctId> [1..1] ± 46
3.4.2.1.8.1.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Unique identification of the securities account as assigned by the account servicer.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 112 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 112
   Type <Tp> [0..1] ± 112
   Name <Nm> [0..1] Text 112
3.4.2.1.8.1.2  CashAccountIdentification <CshAcctId>
Presence: [1..1]
Definition: Unique identification of the cash account, as assigned by the account servicer.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 114 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C4 114
Or}   Other <Othr> [1..1] ± 114
3.4.2.1.8.2  InvoiceTotals <InvcTtls>
Presence: [1..1]
Definition: Specifies totals related to the invoice.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 46 December 2025
```

