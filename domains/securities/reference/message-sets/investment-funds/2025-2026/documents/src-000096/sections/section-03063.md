---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "63.2 Structure"]
file_pages: [4278, 4279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.055.001.03"]
---

# 63.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4278 to 4279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4278

```text
Information provided when the message is a copy of a previous message.
63.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SwtchOrdrConfCxlInstr> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..*] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   AmendmentIndicator <AmdmntInd> [1..1] Indicator 0
   MasterReference <MstrRef> [0..1] Text 0
   OrderReferences <OrdrRefs> [1..*]  0
     OrderReference <OrdrRef> [1..1] Text 4280
     ClientReference <ClntRef> [0..1] Text 4281
     DealReference <DealRef> [0..1] Text 4281
     NonceIdentification <NonceId> [0..1] Text 4281
     CancellationReference <CxlRef> [0..1] Text 4281
     CancellationReason <CxlRsn> [0..1] ± 4281
   CopyDetails <CpyDtls> [0..1] ± 0
63.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
63.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
63.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.055.001.03
SwitchOrderConfirmationCancellationInstructionV03
Investment Funds - Maintenance 2025 - 2026 4278 May 2026
```

## File page 4279

```text
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
63.4.2 PoolReference <PoolRef>
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
63.4.3 PreviousReference <PrvsRef>
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
63.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 setr.055.001.03
SwitchOrderConfirmationCancellationInstructionV03
Investment Funds - Maintenance 2025 - 2026 4279 May 2026
```

