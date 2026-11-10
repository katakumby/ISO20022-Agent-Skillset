---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.1 Account", "6.1.1.2 ProxyAccountIdentification1"]
file_pages: [798]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.1.2 ProxyAccountIdentification1

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 798 to 798.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 798

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
6.1.1.2  ProxyAccountIdentification1
Definition: Information related to a proxy identification of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  798
{Or     Code <Cd> [1..1] CodeSet 798
Or}     Proprietary <Prtry> [1..1] Text 798
   Identification <Id> [1..1] Text 798
6.1.1.2.1  Type <Tp>
Presence: [0..1]
Definition: Type of the proxy identification.
Type <Tp> contains one of the following ProxyAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 798
Or}   Proprietary <Prtry> [1..1] Text 798
6.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalProxyAccountType1Code" on page 899
6.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 916
6.1.1.2.2  Identification <Id>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
798 March 2026
```

