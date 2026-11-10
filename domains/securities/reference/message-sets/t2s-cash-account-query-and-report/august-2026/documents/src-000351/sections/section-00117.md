---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.1 Account", "7.1.1.2 ProxyAccountIdentification1"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.1.2 ProxyAccountIdentification1

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 132 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  132
{Or     Code <Cd> [1..1] CodeSet 132
Or}     Proprietary <Prtry> [1..1] Text 132
   Identification <Id> [1..1] Text 132
7.1.1.2  ProxyAccountIdentification1
Definition: Information related to a proxy identification of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  132
{Or     Code <Cd> [1..1] CodeSet 132
Or}     Proprietary <Prtry> [1..1] Text 132
   Identification <Id> [1..1] Text 132
7.1.1.2.1  Type <Tp>
Presence: [0..1]
Definition: Type of the proxy identification.
Type <Tp> contains one of the following ProxyAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 132
Or}   Proprietary <Prtry> [1..1] Text 132
7.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalProxyAccountType1Code" on page 177
7.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 183
7.1.1.2.2  Identification <Id>
Presence: [1..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 132 August 2026
```

