---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["61 setr.051.001.03 RedemptionOrderConfirmationCancellationInstructionV03", "61.4 Message Building Blocks", "61.4.2 PoolReference <PoolRef>"]
file_pages: [4267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.051.001.03"]
---

# 61.4.2 PoolReference <PoolRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4267 to 4267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4267

```text
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
61.4.2 PoolReference <PoolRef>
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
61.4.3 PreviousReference <PrvsRef>
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
61.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 setr.051.001.03
RedemptionOrderConfirmationCancellationInstructio
nV03
Investment Funds - Maintenance 2025 - 2026 4267 May 2026
```

