---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.4 Message Building Blocks", "23.4.1 Identification <Id>", "23.4.1.3 CopyDuplicate <CpyDplct>"]
file_pages: [555]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.4.1.3 CopyDuplicate <CpyDplct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 555 to 555.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 555

```text
23.4.1.3  CopyDuplicate <CpyDplct>
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
23.4.1.4  MessageOriginator <MsgOrgtr>
Presence: [0..1]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
23.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
23.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 555 August 2026
```

