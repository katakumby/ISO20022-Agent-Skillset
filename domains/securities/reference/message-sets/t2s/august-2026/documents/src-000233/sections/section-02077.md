---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.1 Account", "82.1.1.1 CashAccount38", "82.1.1.1.4 Name <Nm>"]
file_pages: [2829]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.1.1.4 Name <Nm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2829 to 2829.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2829

```text
Definition: Identification of the currency in which the account is held.
Usage: Currency should only be used in case one and the same account number covers several
currencies
and the initiating party needs to identify which currency needs to be used for settlement on the account.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.1.1.1.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 3329
82.1.1.1.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 2829 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  2830
{Or     Code <Cd> [1..1] CodeSet 2830
Or}     Proprietary <Prtry> [1..1] Text 2830
   Identification <Id> [1..1] Text 2830
82.1.1.2  ProxyAccountIdentification1
Definition: Information related to a proxy identification of the account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2829 August 2026
```

