---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "6.4 Message Building Blocks", "6.4.2 AccountIdentification <AcctId>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 6.4.2 AccountIdentification <AcctId>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 82 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 82
   CreationDateTime <CreDtTm> [0..1] DateTime 82
6.4.2 AccountIdentification <AcctId>
Presence: [1..1]
Definition: Identification of the securities account to be updated in the executing party system.
AccountIdentification <AcctId> contains the following elements (see "SecuritiesAccount19" on
page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 79
   Type <Tp> [0..1] ± 79
   Name <Nm> [0..1] Text 79
6.4.3 Modification <Mod>
Presence: [1..*]
Definition: Further details about the requested modification.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 50 December 2019
```

