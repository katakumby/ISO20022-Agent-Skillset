---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.1 Account", "8.1.1.1 CashAccount38", "8.1.1.1.4 Name <Nm>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.1.1.4 Name <Nm>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
Definition: Identification of the currency in which the account is held.
Usage: Currency should only be used in case one and the same account number covers several
currencies
and the initiating party needs to identify which currency needs to be used for settlement on the account.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 72
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
8.1.1.1.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 79
8.1.1.1.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 56 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  57
{Or     Code <Cd> [1..1] CodeSet 57
Or}     Proprietary <Prtry> [1..1] Text 57
   Identification <Id> [1..1] Text 57
8.1.1.2  ProxyAccountIdentification1
Definition: Information related to a proxy identification of the account.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 56 December 2024
```

