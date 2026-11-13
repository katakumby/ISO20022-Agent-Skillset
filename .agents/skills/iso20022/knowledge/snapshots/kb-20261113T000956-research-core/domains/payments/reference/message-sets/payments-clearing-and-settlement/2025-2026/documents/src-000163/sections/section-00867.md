---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.1 Account", "10.1.1.1 CashAccount40", "10.1.1.1.3 Currency <Ccy>"]
file_pages: [1162]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.1.1.3 Currency <Ccy>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1162 to 1162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1162

```text
Definition: Specifies the nature, or use of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 1164 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1164
Or}   Proprietary <Prtry> [1..1] Text 1164
10.1.1.1.3  Currency <Ccy>
Presence: [0..1]
Definition: Identification of the currency in which the account is held.
Usage: Currency should only be used in case one and the same account number covers several
currencies
and the initiating party needs to identify which currency needs to be used for settlement on the account.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 1224
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
10.1.1.1.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 1246
10.1.1.1.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1162 March 2026
```

