---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.4 Message Building Blocks"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
C11 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C12 ModificationRequestPresenceRule
At least one modification request type element must be present.
C13 OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the
receiver.
C14 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C15 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C16 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account owner (or the
instructing party acting on its behalf).
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 154
   CreationDateTime <CreDtTm> [0..1] ± 155
   CopyDuplicate <CpyDplct> [0..1] CodeSet 155
   MessageOriginator <MsgOrgtr> [0..1] ± 155
   MessageRecipient <MsgRcpt> [0..1] ± 155
10.4.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned by the sender of the document.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 154 August 2026
```

