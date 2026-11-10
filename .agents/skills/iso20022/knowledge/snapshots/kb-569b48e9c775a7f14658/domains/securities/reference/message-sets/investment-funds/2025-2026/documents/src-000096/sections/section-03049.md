---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03", "60.4 Message Building Blocks", "60.4.3 PreviousReference <PrvsRef>"]
file_pages: [4261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.049.001.03"]
---

# 60.4.3 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4261 to 4261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4261

```text
60.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
60.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
60.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
60.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 setr.049.001.03
SubscriptionBulkOrderConfirmationCancellationInstr
uctionV03
Investment Funds - Maintenance 2025 - 2026 4261 May 2026
```

