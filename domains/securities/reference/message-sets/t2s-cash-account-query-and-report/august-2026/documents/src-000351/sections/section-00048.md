---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.1 References <Refs>", "3.4.1.1 RequestType <ReqTp>"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.1.1 RequestType <ReqTp>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
References <Refs> contains the following References5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RequestType <ReqTp> [1..1] CodeSet 55
   MessageIdentification <MsgId> [1..1] ± 55
   ProcessIdentification <PrcId> [1..1] ± 55
   AcknowledgedMessageIdentification <AckdMsgId> [0..*] ± 56
   Status <Sts> [0..1] Text 56
   AttachedDocumentName <AttchdDocNm> [0..*] Text 56
3.4.1.1  RequestType <ReqTp>
Presence: [1..1]
Definition: Identifies the type of acknowledged request.
Datatype: "UseCases1Code" on page 179
CodeName Name Definition
OPEN Opening Code indicating the opening of an
account.
MNTN Maintenance Code indicating the maintenance of an
account.
CLSG Closing Code indicating the closing of an
account.
VIEW View Code indicating the view of an account.
3.4.1.2  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Identifies a message by a unique identifier and the date and time when the message was
created by the sender.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 145 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   CreationDateTime <CreDtTm> [1..1] DateTime 145
3.4.1.3  ProcessIdentification <PrcId>
Presence: [1..1]
Definition: Identifies a process by a unique identifier and the date and time when the first message
belonging to the process was created by the sender. The process identification remains the same in all
messages belonging to the same process, from the initial request message to the final account report
closing the process.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 55 August 2026
```

