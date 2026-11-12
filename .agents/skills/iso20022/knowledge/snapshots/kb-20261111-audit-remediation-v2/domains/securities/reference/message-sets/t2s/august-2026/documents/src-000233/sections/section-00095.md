---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.4 Message Building Blocks"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C8", "C9", "C10"], "until_heading": "9.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 136, "topic": "9.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00094.md"}]
---

# 9.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 136, C8–C10 before **9.4 Message Building Blocks** continue [9.3 Constraints](section-00094.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 136

```text
C8 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C9 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 136
   CreationDateTime <CreDtTm> [0..1] ± 136
   CopyDuplicate <CpyDplct> [0..1] CodeSet 137
   MessageOriginator <MsgOrgtr> [0..1] ± 137
   MessageRecipient <MsgRcpt> [0..1] ± 137
9.4.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned by the sender of the document.
Datatype: "Max35Text" on page 3328
9.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the document (message) was created by the sender.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 136 August 2026
```

