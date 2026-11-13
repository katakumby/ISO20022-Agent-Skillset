---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>", "64.4.3.3 Confirmation <Conf>", "64.4.3.3.3 Status <Sts>"]
file_pages: [4292]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3.3.3 Status <Sts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4292 to 4292.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4292

```text
Constraints
• ReasonElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
64.4.3.3.3  Status <Sts>
Presence: [1..1]
Definition: Status of the order confirmation is accepted or received or sent to next party or there is a
communication problem with next party. There is no reason attached.
Datatype: "OrderConfirmationStatus1Code" on page 5332
CodeName Name Definition
STNP SentToNextParty Order confirmation or order confirmation
cancellation instruction or order
confirmation amendment has been sent
to the next party, eg, the next
intermediary.
CPNP CommunicationProblemNextParty Communication problems with the next
party.
COAC ConfirmationAccepted Order confirmation or order confirmation
amendment is accepted.
CREC ConfirmationReceived Order confirmation or order confirmation
amendment is received, ie, technical
validation of the message is ok, and the
message is now at the receiving side.
64.4.3.4  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of an order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
64.4.3.5  DealReference <DealRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
64.4.3.6  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
64.4.3.7  StatusInitiator <StsInitr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4292 May 2026
```

