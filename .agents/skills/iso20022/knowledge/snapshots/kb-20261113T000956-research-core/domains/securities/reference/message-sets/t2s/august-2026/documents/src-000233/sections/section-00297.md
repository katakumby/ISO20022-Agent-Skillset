---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks"]
file_pages: [387]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C21", "C22", "C23", "C24"], "until_heading": "17.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 387, "topic": "17.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00296.md"}]
---

# 17.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 387 to 387.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 387, C21–C24 before **17.4 Message Building Blocks** continue [17.3 Constraints](section-00296.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 387

```text
C21 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C22 StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not
both.
C23 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C24 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
17.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
17.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 387
   CreationDateTime <CreDtTm> [0..1] ± 387
   CopyDuplicate <CpyDplct> [0..1] CodeSet 388
   MessageOriginator <MsgOrgtr> [0..1] ± 388
   MessageRecipient <MsgRcpt> [0..1] ± 388
17.4.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned by the sender of the document.
Datatype: "Max35Text" on page 3328
17.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the document (message) was created by the sender.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 387 August 2026
```

