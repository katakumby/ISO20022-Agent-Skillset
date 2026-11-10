---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "59.4 Message Building Blocks", "59.4.7 OrderReferences <OrdrRefs>", "59.4.7.2 ClientReference <ClntRef>"]
file_pages: [4257, 4258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.047.001.03"]
---

# 59.4.7.2 ClientReference <ClntRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4257 to 4258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4257

```text
59.4.7.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
59.4.7.3  DealReference <DealRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
59.4.7.4  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
59.4.7.5  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order confirmation cancellation, as assigned by
the confirming party.
Datatype: "Max35Text" on page 5403
59.4.7.6  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Reason for the cancellation of the confirmation.
CancellationReason <CxlRsn> contains one of the following elements (see
"CancellationReason31Choice" on page 5189 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5190
Or}   Proprietary <Prtry> [1..1] ± 5191
59.4.8 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Information provided when the message is a copy of a previous message.
Approved by the Securities SEG on 27 January 2026 setr.047.001.03
SubscriptionOrderConfirmationCancellationInstructi
onV03
Investment Funds - Maintenance 2025 - 2026 4257 May 2026
```

## File page 4258

```text
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
Approved by the Securities SEG on 27 January 2026 setr.047.001.03
SubscriptionOrderConfirmationCancellationInstructi
onV03
Investment Funds - Maintenance 2025 - 2026 4258 May 2026
```

