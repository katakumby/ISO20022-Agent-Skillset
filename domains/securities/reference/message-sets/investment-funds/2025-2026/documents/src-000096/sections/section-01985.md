---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "48.2 Structure"]
file_pages: [2762, 2763]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.008.001.05"]
---

# 48.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2762 to 2763.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2762

```text
Information provided when the message is a copy of a previous message.
48.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SbcptBlkOrdrCxlReq> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 2762
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 0
   MasterReference <MstrRef> [0..1] Text 0
   OrderReferences <OrdrRefs> [1..*]  0
     OrderReference <OrdrRef> [1..1] Text 2764
     ClientReference <ClntRef> [0..1] Text 2764
     NonceIdentification <NonceId> [0..1] Text 2764
     CancellationReference <CxlRef> [0..1] Text 2764
     CancellationReason <CxlRsn> [0..1] ± 2764
   CopyDetails <CpyDtls> [0..1] ± 0
48.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
48.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
48.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 setr.008.001.05
SubscriptionBulkOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 2762 May 2026
```

## File page 2763

```text
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
48.4.2 PoolReference <PoolRef>
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
48.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
48.4.4 MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
48.4.5 OrderReferences <OrdrRefs>
Presence: [1..*]
Definition: Identification of the individual order to be cancelled.
Approved by the Securities SEG on 27 January 2026 setr.008.001.05
SubscriptionBulkOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 2763 May 2026
```

