---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.10 Account <Acct>"]
file_pages: [304]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.10 Account <Acct>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 304 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 304

```text
ReportingSource <RptgSrc> contains one of the following elements (see "ReportingSource1Choice"
on page 845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 845
Or}   Proprietary <Prtry> [1..1] Text 845
3.4.2.10  Account <Acct>
Presence: [1..1]
Definition: Unambiguous identification of the account to which credit and debit entries are made.
Impacted by: C19 "IdentificationOrProxyPresenceRule", C17 "IdentificationAndProxyGuideline"
Account <Acct> contains the following CashAccount43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 304
   Type <Tp> [0..1] ± 305
   Currency <Ccy> [0..1] CodeSet C2 305
   Name <Nm> [0..1] Text 305
   Proxy <Prxy> [0..1] ± 305
   Owner <Ownr> [0..1] ± 306
   Servicer <Svcr> [0..1] ± 307
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or proxy must be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.2.10.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
304 March 2026
```

