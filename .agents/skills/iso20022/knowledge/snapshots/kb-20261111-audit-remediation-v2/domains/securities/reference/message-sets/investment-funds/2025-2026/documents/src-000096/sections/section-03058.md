---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "62.2 Structure"]
file_pages: [4272]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.053.001.03"]
---

# 62.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4272 to 4272.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4272

```text
H. CopyDetails
Information provided when the message is a copy of a previous message.
62.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RedBlkOrdrConfCxlInstr> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 4273
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..*] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   AmendmentIndicator <AmdmntInd> [1..1] Indicator 0
   MasterReference <MstrRef> [0..1] Text 4274
   OrderReferences <OrdrRefs> [1..*]  0
     OrderReference <OrdrRef> [1..1] Text 4274
     ClientReference <ClntRef> [0..1] Text 4275
     DealReference <DealRef> [0..1] Text 4275
     NonceIdentification <NonceId> [0..1] Text 4275
     CancellationReference <CxlRef> [0..1] Text 4275
     CancellationReason <CxlRsn> [0..1] ± 4275
   CopyDetails <CpyDtls> [0..1] ± 4275
62.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
62.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 27 January 2026 setr.053.001.03
RedemptionBulkOrderConfirmationCancellationInstr
uctionV03
Investment Funds - Maintenance 2025 - 2026 4272 May 2026
```

