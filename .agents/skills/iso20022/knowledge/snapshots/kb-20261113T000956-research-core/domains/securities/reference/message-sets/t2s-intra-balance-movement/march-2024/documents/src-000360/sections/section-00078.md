---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "6.4 Message Building Blocks"]
file_pages: [95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17"], "until_heading": "6.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 95, "topic": "6.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00077.md"}]
---

# 6.4 Message Building Blocks

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 95 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 95, C10–C17 before **6.4 Message Building Blocks** continue [6.3 Constraints](section-00077.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 95

```text
C10 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C11 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C12 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C13 ModificationRequestPresenceRule
At least one modification request type element must be present.
C14 OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the
receiver.
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
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
95 March 2024
```

