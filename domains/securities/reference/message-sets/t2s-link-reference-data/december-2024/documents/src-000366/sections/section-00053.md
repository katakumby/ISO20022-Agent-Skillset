---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.1 Account", "8.1.1.2 ProxyAccountIdentification1", "8.1.1.2.1 Type <Tp>"]
file_pages: [57]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.1.2.1 Type <Tp>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 57 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  57
{Or     Code <Cd> [1..1] CodeSet 57
Or}     Proprietary <Prtry> [1..1] Text 57
   Identification <Id> [1..1] Text 57
8.1.1.2.1  Type <Tp>
Presence: [0..1]
Definition: Type of the proxy identification.
Type <Tp> contains one of the following ProxyAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 57
Or}   Proprietary <Prtry> [1..1] Text 57
8.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalProxyAccountType1Code" on page 74
8.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 78
8.1.1.2.2  Identification <Id>
Presence: [1..1]
Definition: Identification used to indicate the account identification under another specified name.
Datatype: "Max2048Text" on page 78
8.1.1.3  CashAccountType2Choice
Definition: Nature or use of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 57
Or}   Proprietary <Prtry> [1..1] Text 58
8.1.1.3.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 57 December 2024
```

