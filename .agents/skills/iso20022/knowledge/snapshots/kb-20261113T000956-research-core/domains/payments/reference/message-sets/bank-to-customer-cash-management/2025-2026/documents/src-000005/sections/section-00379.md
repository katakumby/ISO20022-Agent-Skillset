---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.10 Account <Acct>"]
file_pages: [564]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.10 Account <Acct>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 564 to 564.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 564

```text
4.4.2.10  Account <Acct>
Presence: [1..1]
Definition: Unambiguous identification of the account to which credit and debit entries are made.
Impacted by: C18 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
Account <Acct> contains the following CashAccount43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 564
   Type <Tp> [0..1] ± 564
   Currency <Ccy> [0..1] CodeSet C2 565
   Name <Nm> [0..1] Text 565
   Proxy <Prxy> [0..1] ± 565
   Owner <Ownr> [0..1] ± 566
   Servicer <Svcr> [0..1] ± 566
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
4.4.2.10.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C6 801
Or}   Other <Othr> [1..1] ± 801
4.4.2.10.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the nature, or use of the account.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
564 March 2026
```

