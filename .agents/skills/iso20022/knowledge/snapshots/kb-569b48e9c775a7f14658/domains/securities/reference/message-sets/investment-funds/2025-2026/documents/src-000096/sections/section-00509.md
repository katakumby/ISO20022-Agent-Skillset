---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["29 sese.006.001.09 TransferInCancellationRequestV09", "29.3 Constraints"]
file_pages: [691]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.006.001.09"]
---

# 29.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 691 to 691.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 691

```text
29.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
29.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
29.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
29.4.2 PoolReference <PoolRef>
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
29.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
Approved by the Securities SEG on 27 January 2026 sese.006.001.09
TransferInCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 691 May 2026
```

