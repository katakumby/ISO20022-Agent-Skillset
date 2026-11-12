---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["7 camt.066.001.02 IntraBalanceMovementInstructionV02", "7.4 Message Building Blocks"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C14", "C15", "C16", "C17"], "until_heading": "7.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 98, "topic": "7.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00059.md"}]
---

# 7.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 98, C14–C17 before **7.4 Message Building Blocks** continue [7.3 Constraints](section-00059.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 98

```text
C14 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C15 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C16 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C17 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account owner (or the
instructing party acting on its behalf).
Identification <Id> contains the following TransactionAndDocumentIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 98
   DocumentIdentification <DocId> [0..1] Text 98
   CreationDateTime <CreDtTm> [0..1] ± 99
   CopyDuplicate <CpyDplct> [0..1] CodeSet 99
   MessageOriginator <MsgOrgtr> [0..1] ± 99
   MessageRecipient <MsgRcpt> [0..1] ± 99
7.4.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 3328
7.4.1.2  DocumentIdentification <DocId>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities 98 August 2026
```

