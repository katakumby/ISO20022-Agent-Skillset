---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.1 Account", "17.1.1.2 CashAccount40", "17.1.1.2.4 Name <Nm>"]
file_pages: [389]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.1.2.4 Name <Nm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 389 to 389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
17.1.1.2.4  Name <Nm>
Presence: [0..1]
Definition: Name of the account, as assigned by the account servicing institution, in agreement with the
account owner in order to provide an additional means of identification of the account.
Usage: The account name is different from the account owner name. The account name is used in
certain user communities to provide a means of identifying the account, in addition to the account
owner's identity and the account number.
Datatype: "Max70Text" on page 498
17.1.1.2.5  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 390 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  390
{Or     Code <Cd> [1..1] CodeSet 391
Or}     Proprietary <Prtry> [1..1] Text 391
   Identification <Id> [1..1] Text 391
17.1.1.3  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 389
   SchemeName <SchmeNm> [0..1]  390
{Or     Code <Cd> [1..1] CodeSet 390
Or}     Proprietary <Prtry> [1..1] Text 390
   Issuer <Issr> [0..1] Text 390
17.1.1.3.1  Identification <Id>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
389 March 2024
```

