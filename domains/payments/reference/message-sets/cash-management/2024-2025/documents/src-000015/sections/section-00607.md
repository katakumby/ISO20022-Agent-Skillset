---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.1 Account", "37.1.1.1 CashAccount40", "37.1.1.1.3 Currency <Ccy>"]
file_pages: [784]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.1.1.3 Currency <Ccy>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 784 to 784.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 784

```text
Definition: Specifies the nature, or use of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 786 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 786
Or}   Proprietary <Prtry> [1..1] Text 786
37.1.1.1.3  Currency <Ccy>
Presence: [0..1]
Definition: Identification of the currency in which the account is held.
Usage: Currency should only be used in case one and the same account number covers several
currencies
and the initiating party needs to identify which currency needs to be used for settlement on the account.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
37.1.1.1.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 890
37.1.1.1.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 784 February 2025
```

