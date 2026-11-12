---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.10 Account <Acct>", "2.4.2.10.3 Currency <Ccy>"]
file_pages: [46]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.10.3 Currency <Ccy>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 46 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 799 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 799
Or}   Proprietary <Prtry> [1..1] Text 799
2.4.2.10.3  Currency <Ccy>
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
2.4.2.10.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 917
2.4.2.10.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 798 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  798
{Or     Code <Cd> [1..1] CodeSet 798
Or}     Proprietary <Prtry> [1..1] Text 798
   Identification <Id> [1..1] Text 798
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
46 March 2026
```

