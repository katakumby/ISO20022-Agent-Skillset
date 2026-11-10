---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.24 UnderlyingAllocation <UndrlygAllcn>", "3.4.2.15.18.2.24.3 Account <Acct>"]
file_pages: [491]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.24.3 Account <Acct>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 491 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 491

```text
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.15.18.2.24.3  Account <Acct>
Presence: [1..1]
Definition: Unambiguous identification of the account to which the allocation is due or from.
Impacted by: C20 "IdentificationOrProxyPresenceRule", C18 "IdentificationAndProxyGuideline"
Account <Acct> contains the following elements (see "CashAccount40" on page 796 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 796
   Type <Tp> [0..1] ± 796
   Currency <Ccy> [0..1] CodeSet C1 797
   Name <Nm> [0..1] Text 797
   Proxy <Prxy> [0..1] ± 797
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.2.15.18.2.24.4  Purpose <Purp>
Presence: [1..1]
Definition: Underlying reason for the allocation.
Usage: This applies to the allocation only, this is not the underlying reason for the payment.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 851 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 851
Or}   Proprietary <Prtry> [1..1] Text 851
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
491 March 2026
```

