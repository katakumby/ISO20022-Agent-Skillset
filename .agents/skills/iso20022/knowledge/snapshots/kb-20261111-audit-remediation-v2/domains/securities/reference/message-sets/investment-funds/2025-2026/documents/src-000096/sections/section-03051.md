---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03", "60.4 Message Building Blocks", "60.4.7 OrderReferences <OrdrRefs>", "60.4.7.2 ClientReference <ClntRef>"]
file_pages: [4263, 4264]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.049.001.03"]
---

# 60.4.7.2 ClientReference <ClntRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4263 to 4264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4263

```text
60.4.7.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
60.4.7.3  DealReference <DealRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
60.4.7.4  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
60.4.7.5  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order confirmation cancellation, as assigned by
the confirming party.
Datatype: "Max35Text" on page 5403
60.4.7.6  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Reason for the cancellation of the confirmation.
CancellationReason <CxlRsn> contains one of the following elements (see
"CancellationReason31Choice" on page 5189 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5190
Or}   Proprietary <Prtry> [1..1] ± 5191
60.4.8 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Message is a copy.
Approved by the Securities SEG on 27 January 2026 setr.049.001.03
SubscriptionBulkOrderConfirmationCancellationInstr
uctionV03
Investment Funds - Maintenance 2025 - 2026 4263 May 2026
```

## File page 4264

```text
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
Approved by the Securities SEG on 27 January 2026 setr.049.001.03
SubscriptionBulkOrderConfirmationCancellationInstr
uctionV03
Investment Funds - Maintenance 2025 - 2026 4264 May 2026
```

