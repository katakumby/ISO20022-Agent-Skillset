---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.1 Account", "37.1.1.2 ProxyAccountIdentification1"]
file_pages: [785]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.1.2 ProxyAccountIdentification1

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 785 to 785.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 785

```text
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 785 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  785
{Or     Code <Cd> [1..1] CodeSet 785
Or}     Proprietary <Prtry> [1..1] Text 785
   Identification <Id> [1..1] Text 785
37.1.1.2  ProxyAccountIdentification1
Definition: Information related to a proxy identification of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  785
{Or     Code <Cd> [1..1] CodeSet 785
Or}     Proprietary <Prtry> [1..1] Text 785
   Identification <Id> [1..1] Text 785
37.1.1.2.1  Type <Tp>
Presence: [0..1]
Definition: Type of the proxy identification.
Type <Tp> contains one of the following ProxyAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 785
Or}   Proprietary <Prtry> [1..1] Text 785
37.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalProxyAccountType1Code" on page 855
37.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 889
37.1.1.2.2  Identification <Id>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 785 February 2025
```

