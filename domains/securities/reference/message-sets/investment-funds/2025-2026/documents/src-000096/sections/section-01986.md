---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "48.4 Message Building Blocks", "48.4.1 MessageIdentification <MsgId>", "48.4.5.1 OrderReference <OrdrRef>"]
file_pages: [2764, 2765]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.008.001.05"]
---

# 48.4.5.1 OrderReference <OrdrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2764 to 2765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2764

```text
OrderReferences <OrdrRefs> contains the following InvestmentFundOrder13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [1..1] Text 2764
   ClientReference <ClntRef> [0..1] Text 2764
   NonceIdentification <NonceId> [0..1] Text 2764
   CancellationReference <CxlRef> [0..1] Text 2764
   CancellationReason <CxlRsn> [0..1] ± 2764
48.4.5.1  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
48.4.5.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
48.4.5.3  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
48.4.5.4  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
48.4.5.5  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Reason for the cancellation.
Approved by the Securities SEG on 27 January 2026 setr.008.001.05
SubscriptionBulkOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 2764 May 2026
```

## File page 2765

```text
CancellationReason <CxlRsn> contains one of the following elements (see
"CancellationReason32Choice" on page 4869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 4869
Or}   Proprietary <Prtry> [1..1] ± 4869
48.4.6 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Information provided when the message is a copy of a previous message.
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
Approved by the Securities SEG on 27 January 2026 setr.008.001.05
SubscriptionBulkOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 2765 May 2026
```

