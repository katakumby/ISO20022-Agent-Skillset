---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks"]
file_pages: [527]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 527 to 527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 527

```text
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
22.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
22.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 527
   CreationDateTime <CreDtTm> [0..1] ± 527
   CopyDuplicate <CpyDplct> [0..1] CodeSet 527
   MessageOriginator <MsgOrgtr> [0..1] ± 528
   MessageRecipient <MsgRcpt> [0..1] ± 528
22.4.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned by the sender of the document.
Datatype: "Max35Text" on page 3328
22.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the document (message) was created by the sender.
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
22.4.1.3  CopyDuplicate <CpyDplct>
Presence: [0..1]
Definition: Specifies if this document is a copy, a duplicate, or a duplicate of a copy.
Datatype: "CopyDuplicate1Code" on page 3221
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 527 August 2026
```

