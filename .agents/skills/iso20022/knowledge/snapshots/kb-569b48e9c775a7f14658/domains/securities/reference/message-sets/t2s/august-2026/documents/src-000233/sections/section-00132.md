---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.4 Message Building Blocks", "11.4.1 Identification <Id>", "11.4.1.1 Identification <Id>"]
file_pages: [179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.4.1.1 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 179 to 179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 179

```text
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 179
   CreationDateTime <CreDtTm> [0..1] ± 179
   CopyDuplicate <CpyDplct> [0..1] CodeSet 179
   MessageOriginator <MsgOrgtr> [0..1] ± 180
   MessageRecipient <MsgRcpt> [0..1] ± 180
11.4.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned by the sender of the document.
Datatype: "Max35Text" on page 3328
11.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the document (message) was created by the sender.
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
11.4.1.3  CopyDuplicate <CpyDplct>
Presence: [0..1]
Definition: Specifies if this document is a copy, a duplicate, or a duplicate of a copy.
Datatype: "CopyDuplicate1Code" on page 3221
CodeName Name Definition
CODU CopyDuplicate Message is being sent as a copy to a
party other than the account owner, for
information purposes and the message
is a duplicate of a message previously
sent.
COPY Copy Message is being sent as a copy to a
party other than the account owner, for
information purposes.
DUPL Duplicate Message is for information/confirmation
purposes. It is a duplicate of a message
previously sent.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 179 August 2026
```

