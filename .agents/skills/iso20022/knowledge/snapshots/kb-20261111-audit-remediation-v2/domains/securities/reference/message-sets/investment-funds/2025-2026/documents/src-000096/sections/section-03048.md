---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03", "60.2 Structure"]
file_pages: [4260]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.049.001.03"]
---

# 60.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4260 to 4260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4260

```text
H. CopyDetails
Message is a copy.
60.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SbcptBlkOrdrConfCxlInstr> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..*] ± 4261
   RelatedReference <RltdRef> [0..1] ± 0
   AmendmentIndicator <AmdmntInd> [1..1] Indicator 4262
   MasterReference <MstrRef> [0..1] Text 4262
   OrderReferences <OrdrRefs> [1..*]  4262
     OrderReference <OrdrRef> [1..1] Text 4262
     ClientReference <ClntRef> [0..1] Text 4263
     DealReference <DealRef> [0..1] Text 4263
     NonceIdentification <NonceId> [0..1] Text 4263
     CancellationReference <CxlRef> [0..1] Text 4263
     CancellationReason <CxlRsn> [0..1] ± 4263
   CopyDetails <CpyDtls> [0..1] ± 4263
60.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
60.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 27 January 2026 setr.049.001.03
SubscriptionBulkOrderConfirmationCancellationInstr
uctionV03
Investment Funds - Maintenance 2025 - 2026 4260 May 2026
```

