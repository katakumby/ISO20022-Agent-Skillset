---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.1 References <Refs>", "2.4.1.2 ProcessIdentification <PrcId>"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.1.2 ProcessIdentification <PrcId>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
Definition: Identifies a message by a unique identifier and the date and time when the message was
created by the sender.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 145 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   CreationDateTime <CreDtTm> [1..1] DateTime 145
2.4.1.2  ProcessIdentification <PrcId>
Presence: [1..1]
Definition: Identifies a process by a unique identifier and the date and time when the first message
belonging to the process was created by the sender. The process identification remains the same in all
messages belonging to the same process, from the initial request message to the final account report
closing the process.
ProcessIdentification <PrcId> contains the following elements (see "MessageIdentification1" on
page 145 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   CreationDateTime <CreDtTm> [1..1] DateTime 145
2.4.1.3  AttachedDocumentName <AttchdDocNm>
Presence: [0..*]
Definition: File name of a document logically related to the request.
Datatype: "Max70Text" on page 185
2.4.2 From <Fr>
Presence: [0..1]
Definition: Identifies the business sender of the message, if it is not the account owner or account
servicing financial institution.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 10 August 2026
```

