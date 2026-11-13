---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks"]
file_pages: [196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C21", "C22", "C23", "C24"], "until_heading": "10.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 196, "topic": "10.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00161.md"}]
---

# 10.4 Message Building Blocks

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 196 to 196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 196, C21–C24 before **10.4 Message Building Blocks** continue [10.3 Constraints](section-00161.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 196

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
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 196
   CreationDateTime <CreDtTm> [0..1] ± 196
   CopyDuplicate <CpyDplct> [0..1] CodeSet 197
   MessageOriginator <MsgOrgtr> [0..1] ± 197
   MessageRecipient <MsgRcpt> [0..1] ± 197
10.4.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned by the sender of the document.
Datatype: "Max35Text" on page 497
10.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the document (message) was created by the sender.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
196 March 2024
```

