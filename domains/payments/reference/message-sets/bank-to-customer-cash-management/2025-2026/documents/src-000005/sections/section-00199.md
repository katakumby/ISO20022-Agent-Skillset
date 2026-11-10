---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.10 Account <Acct>", "3.4.2.10.6 Owner <Ownr>"]
file_pages: [306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.10.6 Owner <Ownr>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 306 to 306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 306

```text
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 798 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  798
{Or     Code <Cd> [1..1] CodeSet 798
Or}     Proprietary <Prtry> [1..1] Text 798
   Identification <Id> [1..1] Text 798
3.4.2.10.6  Owner <Ownr>
Presence: [0..1]
Definition: Party that legally owns the account.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
306 March 2026
```

