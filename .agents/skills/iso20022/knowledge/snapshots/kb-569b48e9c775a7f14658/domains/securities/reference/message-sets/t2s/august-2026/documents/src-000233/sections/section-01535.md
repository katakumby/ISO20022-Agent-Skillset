---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "43.4 Message Building Blocks", "43.4.2 AccountIdentification <AcctId>"]
file_pages: [2157]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 43.4.2 AccountIdentification <AcctId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2157 to 2157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2157

```text
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
43.4.2 AccountIdentification <AcctId>
Presence: [1..1]
Definition: Identification of the securities account to be updated in the executing party system.
AccountIdentification <AcctId> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
43.4.3 Modification <Mod>
Presence: [1..*]
Definition: Further details about the requested modification.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2157 August 2026
```

