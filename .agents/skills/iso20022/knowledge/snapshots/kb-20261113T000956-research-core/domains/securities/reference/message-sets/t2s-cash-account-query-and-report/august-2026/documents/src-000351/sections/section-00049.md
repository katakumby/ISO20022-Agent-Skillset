---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.1 References <Refs>", "3.4.1.4 AcknowledgedMessageIdentification <AckdMsgId>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.1.4 AcknowledgedMessageIdentification <AckdMsgId>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
ProcessIdentification <PrcId> contains the following elements (see "MessageIdentification1" on
page 145 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   CreationDateTime <CreDtTm> [1..1] DateTime 145
3.4.1.4  AcknowledgedMessageIdentification <AckdMsgId>
Presence: [0..*]
Definition: Reference to the message that is acknowledged.
AcknowledgedMessageIdentification <AckdMsgId> contains the following elements (see
"MessageIdentification1" on page 145 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   CreationDateTime <CreDtTm> [1..1] DateTime 145
3.4.1.5  Status <Sts>
Presence: [0..1]
Definition: Status of the request.
Datatype: "Max35Text" on page 183
3.4.1.6  AttachedDocumentName <AttchdDocNm>
Presence: [0..*]
Definition: File name of a document logically related to the request.
Datatype: "Max70Text" on page 185
3.4.2 AccountServicerIdentification <AcctSvcrId>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 56 August 2026
```

