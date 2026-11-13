---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.10 Account <Acct>", "3.4.2.10.2 Type <Tp>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.10.2 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C6 801
Or}   Other <Othr> [1..1] ± 801
3.4.2.10.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the nature, or use of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 799 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 799
Or}   Proprietary <Prtry> [1..1] Text 799
3.4.2.10.3  Currency <Ccy>
Presence: [0..1]
Definition: Identification of the currency in which the account is held.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 887
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
3.4.2.10.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 917
3.4.2.10.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
305 March 2026
```

