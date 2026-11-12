---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 camt.066.001.02 IntraBalanceMovementInstructionV02", "2.4 Message Building Blocks"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 2.4 Message Building Blocks

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

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
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account owner (or the
instructing party acting on its behalf).
Identification <Id> contains the following TransactionAndDocumentIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 15
   DocumentIdentification <DocId> [0..1] Text 15
   CreationDateTime <CreDtTm> [0..1] ± 16
   CopyDuplicate <CpyDplct> [0..1] CodeSet 16
   MessageOriginator <MsgOrgtr> [0..1] ± 16
   MessageRecipient <MsgRcpt> [0..1] ± 16
2.4.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 497
2.4.1.2  DocumentIdentification <DocId>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
15 March 2024
```

