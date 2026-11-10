---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.1 Account", "10.1.1.2 ProxyAccountIdentification1"]
file_pages: [1163]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.1.2 ProxyAccountIdentification1

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1163 to 1163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1163

```text
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 1163 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  1163
{Or     Code <Cd> [1..1] CodeSet 1163
Or}     Proprietary <Prtry> [1..1] Text 1163
   Identification <Id> [1..1] Text 1163
10.1.1.2  ProxyAccountIdentification1
Definition: Information related to a proxy identification of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  1163
{Or     Code <Cd> [1..1] CodeSet 1163
Or}     Proprietary <Prtry> [1..1] Text 1163
   Identification <Id> [1..1] Text 1163
10.1.1.2.1  Type <Tp>
Presence: [0..1]
Definition: Type of the proxy identification.
Type <Tp> contains one of the following ProxyAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1163
Or}   Proprietary <Prtry> [1..1] Text 1163
10.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalProxyAccountType1Code" on page 1232
10.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 1246
10.1.1.2.2  Identification <Id>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1163 March 2026
```

